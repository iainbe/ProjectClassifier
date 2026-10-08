"""Tests for check E4 (method current) in tools/eligibility_report.py.

Run:  python3 -I tests/test_eligibility_e4.py
The earlier behaviour is asserted unchanged (UNKNOWN with no method rows, PASS with applied rows, FAIL with a
superseded method row); the 26/10/08 extension is asserted additive (FAIL only when a linked statement is SUPERSEDED).
"""
import csv, os, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'tools'))
sys.dont_write_bytecode = True
import eligibility_report

PROJ = ['project_id', 'canonical_name', 'client', 'lifecycle_status', 'client_accepted', 'citation_status', 'programme_status', 'contracting_role', 'prime_contractor']
CLAIM = ['claim_id', 'project_id', 'claim_type', 'effect_family', 'option_state', 'fifth_sector_role', 'outcome_status']
METH = ['method_id', 'project_id', 'method_status', 'statement_id']

def write(path, header, rows):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(header); w.writerows(rows)

class E4(unittest.TestCase):
    def run_fixture(self, methods, statements):
        d = tempfile.mkdtemp(); old = os.getcwd(); os.chdir(d)
        try:
            ids = ['PA', 'PB', 'PC', 'PD', 'PE', 'PF']
            write('01_projects.csv', PROJ, [[i, 'Project ' + i, 'Client', 'COMPLETED', 'Y', 'DELIVERED_WORK', '', 'DIRECT', ''] for i in ids])
            write('04_claims.csv', CLAIM, [])
            write('03_methods.csv', METH, methods)
            os.makedirs('method_statements')
            for sid, status in statements.items():
                open('method_statements/%s_x.md' % sid, 'w').write('---\nstatement_id: %s\nstatus: %s\n---\n' % (sid, status))
            eligibility_report.main()
            return {r['project_id']: r for r in csv.DictReader(open('eligibility_report.csv', newline='', encoding='utf-8'))}
        finally:
            os.chdir(old)

    def test_all_cases(self):
        r = self.run_fixture(
            [['M1', 'PB', 'APPLIED', ''],                  # PB: applied, no statement
             ['M2', 'PC', 'SUPERSEDED', ''],               # PC: superseded method row
             ['M3', 'PD', 'APPLIED', 'MS-1'],              # PD: linked statement SUPERSEDED (new FAIL)
             ['M4', 'PE', 'APPLIED', 'MS-2'],              # PE: linked statement DRAFT (PASS with note)
             ['M5', 'PF', 'APPLIED', 'MS-9']],             # PF: linked statement missing (PASS with note)
            {'MS-1': 'SUPERSEDED', 'MS-2': 'DRAFT'})
        self.assertEqual(r['PA']['E4_method_current'], 'UNKNOWN')   # no method rows: unchanged
        self.assertEqual(r['PB']['E4_method_current'], 'PASS')      # applied: unchanged
        self.assertEqual(r['PC']['E4_method_current'], 'FAIL')      # superseded row: unchanged
        self.assertEqual(r['PD']['E4_method_current'], 'FAIL')      # new
        self.assertIn('SUPERSEDED', r['PD']['E4_note'])
        self.assertEqual(r['PE']['E4_method_current'], 'PASS')      # draft statement never fails the check
        self.assertIn('DRAFT', r['PE']['E4_note'])
        self.assertEqual(r['PF']['E4_method_current'], 'PASS')      # missing statement never fails the check
        self.assertIn('not found', r['PF']['E4_note'])

if __name__ == '__main__':
    unittest.main()
