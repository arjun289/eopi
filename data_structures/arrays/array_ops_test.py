import unittest
from array_ops import *

class TestArrayOps(unittest.TestCase):
  def test_can_reach_end(self):
    arr = [3, 3, 1, 0, 2, 0, 1]
    self.assertEqual(can_reach_end(arr), True)
    arr = [3, 2, 0, 0, 2, 0, 1]
    self.assertEqual(can_reach_end(arr), False)

  def test_remove_duplicates(self):
    arr = []
    self.assertEqual(remove_duplicates(arr), 0)
    arr = [2, 3, 5, 5, 7, 7, 7, 11, 11, 13]
    self.assertEqual(remove_duplicates(arr), 6)


if __name__ == "__main__":
    unittest.main()
