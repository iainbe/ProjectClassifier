import importlib.util, os, unittest
spec = importlib.util.spec_from_file_location('cl', os.path.join(os.path.dirname(__file__), '..', 'tools', 'check_lifecycle.py'))
cl = importlib.util.module_from_spec(spec); spec.loader.exec_module(cl)

def row(life, notes='', cit='LIVE_WORK'): return {'project_id': 'PX', 'lifecycle_status': life, 'notes': notes, 'citation_status': cit}
HOLD = 'ON HOLD: paused by the client; since 25; resume by unknown'

class LifecycleVocab(unittest.TestCase):
    def test_completed_and_in_progress_pass(self):
        self.assertEqual(cl.check([row('COMPLETED', cit='DELIVERED_WORK'), row('IN_PROGRESS')])[0], [])
    def test_on_hold_with_note_passes_and_prompts_when_old(self):
        bad, prompts = cl.check([row('ON_HOLD', HOLD)], '26/10/08')
        self.assertEqual(bad, []); self.assertEqual(len(prompts), 1)
    def test_on_hold_without_note_fails(self):
        self.assertEqual(len(cl.check([row('ON_HOLD', 'paused')])[0]), 1)
    def test_on_hold_cited_as_delivered_fails(self):
        self.assertEqual(len(cl.check([row('ON_HOLD', HOLD, 'DELIVERED_WORK')])[0]), 1)
    def test_typo_and_empty_fail(self):
        self.assertEqual(len(cl.check([row('ON-HOLD'), row('')])[0]), 2)

if __name__ == '__main__': unittest.main()
