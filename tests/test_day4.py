import unittest
from adventofcode17.day4 import *


class Day4Test(unittest.TestCase):
    def test_passphrase_contains_no_duplicates(self):
        self.assertTrue(contains_no_duplicates(''))
        self.assertTrue(contains_no_duplicates('aa bb cc dd ee'))
        self.assertTrue(contains_no_duplicates('aa    bb  cc \n dd  \t ee'))
        self.assertTrue(contains_no_duplicates('aa bb cc dd aaa'))
        self.assertFalse(contains_no_duplicates('aa bb cc dd aa'))

    def test_passphrase_contains_no_anagrams(self):
        self.assertTrue(contains_no_anagrams(''))
        self.assertTrue(contains_no_anagrams('abcde fghij'))
        self.assertFalse(contains_no_anagrams('abcde xyz ecdab'))
        self.assertTrue(contains_no_anagrams('a ab abc abd abf abj'))
        self.assertTrue(contains_no_anagrams('iiii oiii ooii oooi oooo'))
        self.assertFalse(contains_no_anagrams('oiii ioii iioi iiio'))


if __name__ == '__main__':
    unittest.main()
