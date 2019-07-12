import unittest
from adventofcode17.day3 import *


class Day3Puzzle1Test(unittest.TestCase):
    def test_find_ring_number(self):
        self.assertEqual(find_ring_number(1), 0)
        self.assertEqual(find_ring_number(2), 1)
        self.assertEqual(find_ring_number(17), 2)

    def test_find_location_distance(self):
        self.assertEqual(puzzle1(1), 0)
        self.assertEqual(puzzle1(2), 1)
        self.assertEqual(puzzle1(3), 2)
        self.assertEqual(puzzle1(4), 1)
        self.assertEqual(puzzle1(5), 2)
        self.assertEqual(puzzle1(6), 1)
        self.assertEqual(puzzle1(7), 2)
        self.assertEqual(puzzle1(8), 1)
        self.assertEqual(puzzle1(9), 2)
        self.assertEqual(puzzle1(10), 3)
        self.assertEqual(puzzle1(12), 3)
        self.assertEqual(puzzle1(23), 2)
        self.assertEqual(puzzle1(25), 4)
        self.assertEqual(puzzle1(1024), 31)


if __name__ == '__main__':
    unittest.main()
