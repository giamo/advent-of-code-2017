from adventofcode17.utils import get_file_path


def puzzle1(digits):
    """Find the sum of all digits that match the next digit in the list"""
    return sum_matches(digits, lambda i: i + 1 if i < len(digits) - 1 else 0)


def puzzle2(digits):
    """Find the sum of all digits that match the digit halfway around the circular list"""
    if len(digits) % 2 != 0:
        raise ValueError('the list of digits should have an even number of elements')

    half_len = len(digits) // 2
    return sum_matches(digits, lambda i: i + half_len if i < half_len else i + half_len - len(digits))


def sum_matches(digits, get_digit_to_compare_idx):
    """Find the sum of the values in digits that match the digit returned by get_digit_to_compare_idx"""
    matches = 0
    for idx in range(len(digits)):
        other_idx = get_digit_to_compare_idx(idx)
        if idx != other_idx and int(digits[idx]) == int(digits[other_idx]):
            matches += int(digits[idx])
    return matches


def main():
    with open(get_file_path('input_day1.txt'), 'rt') as f:
        digits = f.readline().rstrip()
        print('Solution for day 1, puzzle 1: %s' % puzzle1(digits))
        print('Solution for day 1, puzzle 2: %s' % puzzle2(digits))


if __name__ == '__main__':
    main()
