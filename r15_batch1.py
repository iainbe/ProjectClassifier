#!/usr/bin/env python3
"""R1.5 generalised: document inventory and metadata extraction for any project.
Read-only: no files are moved, modified or deleted.
Usage: python3 r15_inventory.py <project_id> <project_root_relative_to_drive>
"""
import os, sys, json, datetime

DRIVE = "/Users/iainbe/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive"
OUT = os.path.join(DRIVE, "Website 2026/spillover-toolkit/version_metadata")

def get_file_info(filepath):
    stat = os.stat(filepath)
    return {
        "path": os.path.relpath(filepath, DRIVE),
        "filename": os.path.basename(filepath),
        "size_bytes": stat.st_size,
        "modified": datetime.datetime.fromtimestamp(stat.st_mtime).isoformat(),
        "created": datetime.datetime.fromtimestamp(stat.st_ctime).isoformat(),
        "extension": os.path.splitext(filepath)[1].lower(),
    }

def extract_docx_metadata(filepath):
    try:
        from docx import Document
        doc = Document(filepath)
        cp = doc.core_properties
        title_lines = []
        for p in doc.paragraphs[:50]:
            if p.text.strip():
                title_lines.append(p.text.strip())
            if len(title_lines) >= 15:
                break
        return {
            "internal_title": cp.title or "",
            "internal_author": cp.author or "",
            "internal_last_modified_by": cp.last_modified_by or "",
            "internal_created": cp.created.isoformat() if cp.created else "",
            "internal_modified": cp.modified.isoformat() if cp.modified else "",
            "internal_revision": cp.revision or "",
            "paragraph_count": len(doc.paragraphs),
            "table_count": len(doc.tables),
            "title_page_text": title_lines,
        }
    except Exception as e:
        return {"error": str(e)}

def extract_pdf_metadata(filepath):
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(filepath)
        meta = reader.metadata or {}
        first_page_text = ""
        if reader.pages:
            first_page_text = reader.pages[0].extract_text() or ""
        return {
            "pdf_title": meta.get("/Title", ""),
            "pdf_author": meta.get("/Author", ""),
            "page_count": len(reader.pages),
            "first_page_text": first_page_text[:1000],
        }
    except Exception as e:
        return {"error": str(e)}

def extract_xlsx_metadata(filepath):
    try:
        from openpyxl import load_workbook
        wb = load_workbook(filepath, data_only=True, read_only=True)
        return {"sheet_names": wb.sheetnames, "sheet_count": len(wb.sheetnames)}
    except Exception as e:
        return {"error": str(e)}

def extract_pptx_metadata(filepath):
    try:
        from pptx import Presentation
        prs = Presentation(filepath)
        return {"slide_count": len(prs.slides)}
    except Exception as e:
        return {"error": str(e)}

def run_inventory(project_id, project_root_rel):
    project_root = os.path.join(DRIVE, project_root_rel)
    if not os.path.exists(project_root):
        print(f"ERROR: project root not found: {project_root}")
        return
    
    results = []
    for root, dirs, files in os.walk(project_root):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            filepath = os.path.join(root, f)
            info = get_file_info(filepath)
            ext = info["extension"]
            if ext == ".docx":
                info["doc_metadata"] = extract_docx_metadata(filepath)
            elif ext == ".pdf":
                info["pdf_metadata"] = extract_pdf_metadata(filepath)
            elif ext == ".xlsx":
                info["xlsx_metadata"] = extract_xlsx_metadata(filepath)
            elif ext == ".pptx":
                info["pptx_metadata"] = extract_pptx_metadata(filepath)
            results.append(info)
    
    results.sort(key=lambda x: x["modified"])
    
    os.makedirs(OUT, exist_ok=True)
    out_file = os.path.join(OUT, f"{project_id}_inventory.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False, default=str)
    
    print(f"\n=== {project_id}: {project_root_rel} ===")
    print(f"Total files: {len(results)}")
    print(f"Output: {out_file}")
    print()
    print("--- Report-like files (.docx, .pdf, .xlsx, .pptx, .rtf) by date ---")
    for r in results:
        ext = r["extension"]
        if ext not in (".docx", ".pdf", ".xlsx", ".pptx", ".rtf"):
            continue
        fname = r["filename"]
        mod = r["modified"][:10]
        size_kb = r["size_bytes"] // 1024
        
        indicators = []
        fl = fname.lower()
        if "final" in fl: indicators.append("FINAL")
        if "draft" in fl: indicators.append("DRAFT")
        if "v2" in fl or "v3" in fl or "v1" in fl: indicators.append("VERSIONED")
        if "update" in fl: indicators.append("UPDATE")
        if "revision" in fl or "revised" in fl: indicators.append("REVISION")
        if "tracked" in fl: indicators.append("TRACKED")
        if "comments" in fl: indicators.append("COMMENTS")
        
        internal = ""
        if "doc_metadata" in r:
            dm = r["doc_metadata"]
            if "error" not in dm:
                rev = dm.get("internal_revision", "")
                auth = dm.get("internal_author", "")
                mod_by = dm.get("internal_last_modified_by", "")
                int_mod = dm.get("internal_modified", "")[:10] if dm.get("internal_modified") else ""
                paras = dm.get("paragraph_count", 0)
                tables = dm.get("table_count", 0)
                internal = f" | rev={rev} auth='{auth}' mod_by='{mod_by}' int_mod={int_mod} paras={paras} tables={tables}"
        elif "pdf_metadata" in r:
            pm = r["pdf_metadata"]
            if "error" not in pm:
                internal = f" | pages={pm.get('page_count', 0)}"
        elif "xlsx_metadata" in r:
            xm = r["xlsx_metadata"]
            if "error" not in xm:
                internal = f" | sheets={xm.get('sheet_count', 0)}"
        elif "pptx_metadata" in r:
            pm = r["pptx_metadata"]
            if "error" not in pm:
                internal = f" | slides={pm.get('slide_count', 0)}"
        
        ind_str = " ".join(indicators) if indicators else "-"
        print(f"{mod} {size_kb:>6}KB [{ind_str:>20}] {fname}{internal}")

# Batch 1: P02-FGTG, P03-MITIH, P04-GBSLEP
projects = [
    ("P02-FGTG", "Archive projects/2024 Projects/2024 Man Met From Good to Great"),
    ("P03-MITIH", "Archive projects/2025 Projects/2025 MITIH Createch ecosystem"),
    ("P04-GBSLEP", "Archive projects/2017 Projects/2017 GBSLEP creative economy mapping"),
]

for pid, root in projects:
    run_inventory(pid, root)
