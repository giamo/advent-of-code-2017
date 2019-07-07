import re
from adventofcode17.utils import get_file_path


def puzzle1(lines):
    """Find the checksum of a spreadsheet file"""
    return sum([compute_row_maxmin_difference(parse_row(row)) for row in lines])


def puzzle2(lines):
    """Find the sum of each row's result"""
    return sum([find_row_even_division(parse_row(row)) for row in lines])


def parse_row(row):
    """Parse a file row into a list of integers"""
    return [int(e) for e in re.split('\s+', row) if e]


def compute_row_maxmin_difference(row):
    """Calculate the difference between the max and min value in the row list"""
    return max(row, default=0) - min(row, default=0)


def even_division(a, b):
    """Return a/b if evenly divisible, 0 otherwise"""
    return a // b if a % b == 0 else 0


def find_row_even_division(row):
    """Find the result the division of the only evenly divisible numbers"""
    for a in row:
        for b in row:
            r = even_division(a, b)
            if (a is not b) and r != 0:
                return r
    return 0


def main():
    with open(get_file_path('input_day2.txt'), 'rt') as f:
        lines = f.readlines()
        print('Solution for day 1, puzzle 1: %s' % puzzle1(lines))
        print('Solution for day 1, puzzle 2: %s' % puzzle2(lines))


if __name__ == '__main__':
    main()
