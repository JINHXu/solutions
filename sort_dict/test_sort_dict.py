#!/usr/bin/env/python3

import unittest
import timeit
from pathlib import Path

from sort_dict import string_sort

class TestDictOrder(unittest.TestCase):

    def test_small(self):
        with open(Path("sort_dict/data/mini_vocab.txt"), encoding='utf8', mode='r') as in_f:
            word_list = [line.strip() for line in in_f]
            sorted_word_list = sorted(word_list)

            result = string_sort(word_list)

            self.assertEqual(result, sorted_word_list)

    def test_large(self):
            loops = 10
            setup = """
from pathlib import Path
from sort_dict import string_sort
with open(Path("sort_dict/data/words_alpha.txt"), encoding='utf8', mode='r') as in_f:
    word_list = [line.strip() for line in in_f]
string_sort(word_list)"""
            time = timeit.timeit(setup, number=loops)
            print("\nTiming " + str(loops) + " loops of string_sort: " , time)


