import unittest
from adventofcode17.day5 import *

rule1 = lambda i: i + 1
rule2 = lambda i: i + 1 if i < 3 else i - 1


class Day5Test(unittest.TestCase):

    def test_jump_changes_offset_rule1(self):
        input1 = [0, 3]
        perform_jump(input1, 0, rule1)
        self.assertEqual(input1[0], 1)

        input2 = [-2, -2]
        perform_jump(input2, 0, rule1)
        self.assertEqual(input2[0], -1)

    def test_jump_moves_index(self):
        input = [3, 3, 0, -1, -3]

        new_idx = perform_jump(input, 0, rule1)
        self.assertEqual(new_idx, 3)

        new_idx = perform_jump(input, 3, rule2)
        self.assertEqual(new_idx, 2)

    def test_jumps_to_exit_puzzle1(self):
        self.assertEqual(puzzle1([]), 0)
        self.assertEqual(puzzle1([0]), 2)
        self.assertEqual(puzzle1([0, 3, 0, 1, -3]), 5)

    def test_jump_changes_offset_rule2(self):
        input1 = [3, 3]
        perform_jump(input1, 0, rule2)
        self.assertEqual(input1[0], 2)

        input2 = [6, -2]
        perform_jump(input2, 0, rule2)
        self.assertEqual(input2[0], 5)

        input3 = [2, -2]
        perform_jump(input3, 0, rule2)
        self.assertEqual(input3[0], 3)

    def test_jumps_to_exit_puzzle2(self):
        self.assertEqual(puzzle2([]), 0)
        self.assertEqual(puzzle2([0]), 2)
        self.assertEqual(puzzle2([0, 3, 0, 1, -3]), 10)


if __name__ == '__main__':
    unittest.main()
