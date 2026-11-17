import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from backlog_prioritizer import BacklogItem, load_from_csv, prioritize  # noqa: E402

SAMPLE = Path(__file__).resolve().parents[1] / "examples" / "sample_backlog.csv"


class TestWSJF(unittest.TestCase):
    def test_score(self):
        item = BacklogItem("X", "x", 8, 5, 3, 2)
        self.assertEqual(item.cost_of_delay, 16)
        self.assertEqual(item.wsjf_score, 8.0)

    def test_rejects_non_fibonacci(self):
        with self.assertRaises(ValueError):
            BacklogItem("X", "x", 4, 5, 3, 2)

    def test_order_and_tiebreak(self):
        a = BacklogItem("A", "a", 5, 5, 5, 3)   # 5.0, size 3
        b = BacklogItem("B", "b", 2, 2, 1, 1)   # 5.0, size 1
        c = BacklogItem("C", "c", 13, 13, 13, 3)
        self.assertEqual([i.id for i in prioritize([a, b, c])], ["C", "B", "A"])

    def test_sample_file(self):
        ranked = prioritize(load_from_csv(SAMPLE))
        self.assertEqual(len(ranked), 8)
        self.assertEqual(ranked[0].id, "US-104")
        self.assertEqual(ranked[-1].id, "US-108")


if __name__ == "__main__":
    unittest.main()
