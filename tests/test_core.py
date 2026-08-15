import unittest
from data_freshness_monitor.core import monitor
class T(unittest.TestCase):
 def test_fresh(self): self.assertEqual(monitor([{"id":"x","observed_at":"2026-01-01T00:00:00Z"}],now="2026-01-01T00:10:00Z")["datasets"][0]["status"],"fresh")
 def test_stale(self): self.assertEqual(monitor([{"id":"x","observed_at":"2026-01-01T00:00:00Z"}],now="2026-01-01T02:00:00Z")["datasets"][0]["status"],"stale")
 def test_unknown(self): self.assertEqual(monitor([{"id":"x"}],now="2026-01-01T00:00:00Z")["datasets"][0]["status"],"blocked")
 def test_future(self): self.assertEqual(monitor([{"id":"x","observed_at":"2026-01-02T00:00:00Z"}],now="2026-01-01T00:00:00Z")["datasets"][0]["status"],"stale")
 def test_degraded(self): self.assertEqual(monitor([{"id":"x"}],now="2026-01-01T00:00:00Z")["status"],"degraded")
if __name__=="__main__": unittest.main()

