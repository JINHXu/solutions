#!/usr/bin/env/python3

import unittest
import random

from rand_quicksort import randomized_inplace_quick_sort

class TestRandQuickSort(unittest.TestCase):

    def test_sorted_sequence(self):
        sorted_seq = [i for i in range(100000)]
        sorted_seq_copy = sorted_seq[:]

        randomized_inplace_quick_sort(sorted_seq, 0, len(sorted_seq)-1)

        self.assertEqual(sorted_seq, sorted_seq_copy)
        
    def test_random_sequence(self):
        sorted_seq = [i for i in range(100000)]
        random_seq = sorted_seq[:]
        random.shuffle(random_seq)

        randomized_inplace_quick_sort(random_seq, 0, len(random_seq)-1)

        self.assertEqual(sorted_seq, random_seq)