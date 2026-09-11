#!/usr/bin/env python3
"""R1.5 NES pilot: document inventory and metadata extraction.
Read-only: no files are moved, modified or deleted."""
import os, sys, json, datetime
from pathlib import Path

DRIVE = "/Users/iainbe/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive"
NES_ROOT = os.path.join(DRIVE, "Active projects/2025 NE Scotland/2025 NE Scotland reporting")
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
        # First 30 non-empty paragraphs for title page text
        title_lines = []
        for p in doc.paragraphs[:50]:
            if p.text.strip():
                title_lines.append(p.text.strip())
            if len(title_lines) >= 30:
                break
        return {
            "internal_title": cp.title or "",
            "internal_author": cp.author or "",
            "internal_last_modified_by": cp.last_modified_by or "",
            "internal_created": cp.created.isoformat() if cp.created else "",
            "internal_modified": cp.modified.isoformat() if cp.modified else "",
            "internal_revision": cp.revision or "",
            "internal_subject": cp.subject or "",
            "internal_keywords": cp.keywords or "",
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
        # First page text
        first_page_text = ""
        if reader.pages:
            first_page_text = reader.pages[0].extract_text() or ""
        return {
            "pdf_title": meta.get("/Title", ""),
            "pdf_author": meta.get("/Author", ""),
            "pdf_creator": meta.get("/Creator", ""),
            "pdf_producer": meta.get("/Producer", ""),
            "pdf_creation_date": str(meta.get("/CreationDate", "")),
            "pdf_mod_date": str(meta.get("/ModDate", "")),
            "page_count": len(reader.pages),
            "first_page_text": first_page_text[:2000],
        }
    except Exception as e:
        return {"error": str(e)}

def extract_xlsx_metadata(filepath):
    try:
        from openpyxl import load_workbook
        wb = load_workbook(filepath, data_only=True, read_only=True)
        return {
            "sheet_names": wb.sheetnames,
            "sheet_count": len(wb.sheetnames),
        }
    except Exception as e:
        return {"error": str(e)}

# Inventory all files in NES root and subfolders
results = []
for root, dirs, files in os.walk(NES_ROOT):
    # Skip .claude and other hidden dirs
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for f in files:
        filepath = os.path.join(root, f)
        info = get_file_info(filepath)
        
        # Extract document metadata for report-like files
        ext = info["extension"]
        if ext == ".docx":
            info["doc_metadata"] = extract_docx_metadata(filepath)
        elif ext == ".pdf":
            info["pdf_metadata"] = extract_pdf_metadata(filepath)
        elif ext == ".xlsx":
            info["xlsx_metadata"] = extract_xlsx_metadata(filepath)
        elif ext in (".rtf",):
            # RTF: read first 500 chars for title markers
            try:
                with open(filepath, 'r', encoding='utf-8', errors='replace') as rf:
                    info["rtf_preview"] = rf.read(500)
            except:
                pass
        
        results.append(info)

# Sort by modified date
results.sort(key=lambda x: x["modified"])

# Output JSON
os.makedirs(OUT, exist_ok=True)
out_file = os.path.join(OUT, "NES_inventory.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False, default=str)

# Print summary
print(f"Total files found: {len(results)}")
print(f"Output: {out_file}")
print()
print("=== FILES BY DATE (report-like only: .docx, .pdf, .xlsx, .rtf) ===")
print()
for r in results:
    ext = r["extension"]
    if ext not in (".docx", ".pdf", ".xlsx", ".rtf"):
        continue
    fname = r["filename"]
    mod = r["modified"][:10]
    size_kb = r["size_bytes"] // 1024
    
    # Version indicators from filename
    indicators = []
    fname_lower = fname.lower()
    if "final" in fname_lower: indicators.append("FINAL")
    if "draft" in fname_lower: indicators.append("DRAFT")
    if "v2" in fname_lower or "v3" in fname_lower: indicators.append("VERSIONED")
    if "update" in fname_lower: indicators.append("UPDATE")
    if "revision" in fname_lower or "revised" in fname_lower: indicators.append("REVISION")
    if "tracked" in fname_lower: indicators.append("TRACKED")
    if "comments" in fname_lower: indicators.append("COMMENTS")
    if "appendix" in fname_lower or "appendices" in fname_lower: indicators.append("APPENDIX")
    
    # Internal metadata
    internal = ""
    if "doc_metadata" in r:
        dm = r["doc_metadata"]
        if "error" not in dm:
            rev = dm.get("internal_revision", "")
            auth = dm.get("internal_author", "")
            title = dm.get("internal_title", "")
            mod_by = dm.get("internal_last_modified_by", "")
            int_mod = dm.get("internal_modified", "")[:10] if dm.get("internal_modified") else ""
            paras = dm.get("paragraph_count", 0)
            tables = dm.get("table_count", 0)
            internal = f" | int_title='{title}' int_author='{auth}' int_mod_by='{mod_by}' int_mod={int_mod} rev={rev} paras={paras} tables={tables}"
    
    ind_str = " ".join(indicators) if indicators else "-"
    print(f"{mod} {size_kb:>6}KB [{ind_str:>20}] {fname}{internal}")
