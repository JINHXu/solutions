#!/usr/bin/env/python3

import unittest
import timeit

from sort_dict import string_sort
from rand_quicksort import randomized_inplace_quick_sort

class TestSortDict(unittest.TestCase):

    def test_small(self):
        with open("sort_dict/data/mini_vocab.txt", encoding='utf8', mode='r') as in_f:
            word_list = [line.strip() for line in in_f]
            sorted_word_list = sorted(word_list)
            # test to see if rand_quick work:test result: OK(this part not required in the exercise)
            # randomized_inplace_quick_sort(word_list, 0, len(word_list)-1)
            # self.assertEqual(word_list, sorted_word_list)

            result = string_sort(word_list)

            self.assertEqual(result, sorted_word_list)

    def test_large(self):
            loops = 10
            setup = """
from sort_dict import string_sort
from rand_quicksort import randomized_inplace_quick_sort
with open("sort_dict/data/words_alpha.txt", encoding='utf8', mode='r') as in_f:
    word_list = [line.strip() for line in in_f]
"""
            time = timeit.timeit("string_sort(word_list)", setup, number=loops)
            print("\nTiming ", loops, " loops of string_sort: ", time)

            #Extension of the function: 
            time = timeit.timeit("randomized_inplace_quick_sort(word_list, 0, len(word_list)-1)", setup, number=loops)
            print("\nTiming ", loops, " loops of string_sort: ", time)


