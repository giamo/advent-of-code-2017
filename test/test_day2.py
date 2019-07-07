import unittest
from adventofcode17.day2 import *


class Day1Puzzle1Test(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(puzzle1([]), 0)
        self.assertEqual(puzzle1(['']), 0)

    def test_checksum_one_row(self):
        self.assertEqual(puzzle1(['1 16 9']), 15)
        self.assertEqual(puzzle1(['236 234 235']), 2)
        self.assertEqual(puzzle1(['1234']), 0)
        self.assertEqual(puzzle1(['55 55']), 0)

    def test_checksum_multiple_rows(self):
        self.assertEqual(puzzle1([
            '12 3 4 5',  # 12 - 3 = 9
            '1 2',  # 2 -1 = 1
            '100',  # 100 - 100 = 0
            '123 145 90 15'  # 145 - 15 = 130
        ]),
            140  # 9 + 1 + 0 + 130
        )
        self.assertEqual(puzzle1(['', '  ', '  \n']), 0)

    def test_not_a_number(self):
        with self.assertRaises(ValueError):
            puzzle1(['abc123 50'])
            puzzle1(['1,2 3'])


class Day1Puzzle2Test(unittest.TestCase):
    def test_even_division(self):
        self.assertEqual(even_division(8, 2), 4)
        self.assertEqual(even_division(100, 5), 20)

    def test_not_even_division(self):
        self.assertEqual(even_division(8, 3), 0)
        self.assertEqual(even_division(100, 6), 0)
        self.assertEqual(even_division(17, 4), 0)

    def test_row_result(self):
        self.assertEqual(find_row_even_division([5, 9, 2, 8]), 4)
        self.assertEqual(find_row_even_division([9, 4, 7, 3]), 3)
        self.assertEqual(find_row_even_division([3, 8, 6, 5]), 2)
        self.assertEqual(find_row_even_division([3, 5, 7]), 0)


if __name__ == '__main__':
    unittest.main()
