import re
from adventofcode17.utils import get_file_path


def puzzle1(passphrases):
    """Find the number of passphrases that do not contain duplicates"""
    return count_valid_passphrases(passphrases, contains_no_duplicates)


def puzzle2(passphrases):
    """Find the number of passphrases that do not contain anagrams"""
    return count_valid_passphrases(passphrases, contains_no_anagrams)


def count_valid_passphrases(passphrases, validator):
    return len([p for p in passphrases if validator(p)])


def contains_no_duplicates(passphrase):
    passphrase_words = re.split('\s+', passphrase)
    return len(passphrase_words) == len(set(passphrase_words))


def contains_no_anagrams(passphrase):
    passphrase_words = [''.join(sorted(w)) for w in re.split('\s+', passphrase)]
    return len(passphrase_words) == len(set(passphrase_words))


def main():
    with open(get_file_path('input_day4.txt'), 'rt') as f:
        lines = f.readlines()
        print('Solution for day 1, puzzle 1: %s' % puzzle1(lines))
        print('Solution for day 1, puzzle 2: %s' % puzzle2(lines))


if __name__ == '__main__':
    main()
