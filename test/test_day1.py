import unittest
from adventofcode17.day1 import puzzle1, puzzle2


class Day1Puzzle1Test(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(puzzle1(''), 0)

    def test_no_matches(self):
        self.assertEqual(puzzle1('1'), 0)
        self.assertEqual(puzzle1('12345'), 0)

    def test_matches(self):
        self.assertEqual(puzzle1('112345'), 1)
        self.assertEqual(puzzle1('112233'), 6)
        self.assertEqual(puzzle1('111234'), 2)

    def test_match_last_digit(self):
        self.assertEqual(puzzle1('552345'), 10)
        self.assertEqual(puzzle1('987659'), 9)
        self.assertEqual(puzzle1('66'), 12)

    def test_not_a_digit(self):
        with self.assertRaises(ValueError):
            puzzle1('abc123')


class Day1Puzzle2Test(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(puzzle2(''), 0)

    def test_no_matches(self):
        self.assertEqual(puzzle2('12'), 0)
        self.assertEqual(puzzle2('1221'), 0)

    def test_matches(self):
        self.assertEqual(puzzle2('1212'), 6)
        self.assertEqual(puzzle2('123425'), 4)
        self.assertEqual(puzzle2('123123'), 12)
        self.assertEqual(puzzle2('12131415'), 4)

    def test_not_a_digit(self):
        with self.assertRaises(ValueError):
            puzzle2('abc123')

    def test_odd_number_of_elements(self):
        with self.assertRaises(ValueError):
            puzzle2('1')
            puzzle2('123')
            puzzle2('12345')



if __name__ == '__main__':
    unittest.main()
