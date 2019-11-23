#!/usr/bin/env/python3

import unittest
import filecmp
import timeit

from pig_latin import encode_word, encode_file_1, encode_file_2

class TestPigLatinEncoder(unittest.TestCase):

    def test_encode_string(self):
        word = "string"
        correct_encoding = "ingstray"
        result = encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_latin(self):
        word = "latin"
        correct_encoding = "atinlay"
        result = encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_idle(self):
        word = "idle"
        correct_encoding = "idleay"
        result = encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_empty(self):
        word = ""
        correct_encoding = ""
        result = encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_no_vowels(self):
        word = "str"
        correct_encoding = "stray"
        result = encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_titlecase(self):
        word = "Look"
        correct_encoding = "Ooklay"
        result = encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_uppercase(self):
        word = "LOOK"
        correct_encoding = "OOKLAY"
        result = encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_punct(self):
        word = "air,"
        correct_encoding = "airay,"
        result = encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_punct2(self):
        word = "What???"
        correct_encoding = "Atwhay???"
        result = encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_punct3(self):
        word = "***"
        correct_encoding = "ay***"
        result = encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_file_1(self):

        md_ch1 = "pig_latin/data/2701-0-ch1.txt"
        pl_md_ch1 = "pig_latin/data/2701-0-ch1-pl.txt"
        result1_md_ch1 = "pig_latin/data/2701-0-ch1-pl-result-1.txt"

        encode_file_1(md_ch1, result1_md_ch1)

        self.assertEqual(filecmp.cmp(result1_md_ch1, pl_md_ch1), True)

    def test_encode_file_2(self):
        
        md_ch1 = "pig_latin/data/2701-0-ch1.txt"
        pl_md_ch1 = "pig_latin/data/2701-0-ch1-pl.txt"
        result2_md_ch1 = "pig_latin/data/2701-0-ch1-pl-result-2.txt"

        encode_file_2(md_ch1, result2_md_ch1)

        self.assertEqual(filecmp.cmp(result2_md_ch1, pl_md_ch1), True)

    def test_speed(self):
        loops = 20

        setup1 = """\
from pig_latin import encode_file_1
md_ch1 = "pig_latin/data/2701-0.txt"
result1_md_ch1 = "pig_latin/data/2701-0-result-1-speed.txt"
"""
        time1 = timeit.timeit("encode_file_1(md_ch1, result1_md_ch1)", setup1, number=loops)
        print("\nTiming ", loops, " loops of encode_file_1: ", time1)

        setup2 = """\
from pig_latin import encode_file_2
md_ch1 = "pig_latin/data/2701-0.txt"
result2_md_ch1 = "pig_latin/data/2701-0-result-2-speed.txt"
"""
        time2 = timeit.timeit("encode_file_2(md_ch1, result2_md_ch1)", setup2, number=loops)
        print("\nTiming ", loops, " loops of encode_file_2: ", time2)
        