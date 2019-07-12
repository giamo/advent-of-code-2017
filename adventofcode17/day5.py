from adventofcode17.utils import get_file_path


def puzzle1(offsets):
    """Find the number of jumps before reaching the exit (rule 1)"""
    return find_jumps_to_exit(offsets, lambda o: o + 1)


def puzzle2(offsets):
    """Find the number of jumps before reaching the exit (rule 2)"""
    return find_jumps_to_exit(offsets, lambda o: o + 1 if o < 3 else o - 1)


def find_jumps_to_exit(offsets, get_offset_side_effect):
    idx = 0
    jumps = 0
    while True:
        try:
            idx = perform_jump(offsets, idx, get_offset_side_effect)
            jumps += 1
        except IndexError:
            break
    return jumps


def perform_jump(offsets, index, get_offset_side_effect):
    current_elem = offsets[index]
    offsets[index] = get_offset_side_effect(offsets[index])
    return index + current_elem


def main():
    with open(get_file_path('input_day5.txt'), 'rt') as f:
        offsets = [int(l) for l in f.readlines()]
        print('Solution for day 1, puzzle 1: %s' % puzzle1(offsets.copy()))
        print('Solution for day 1, puzzle 2: %s' % puzzle2(offsets.copy()))


if __name__ == '__main__':
    main()
