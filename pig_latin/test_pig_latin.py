#!/usr/bin/env/python3

import unittest
import filecmp
import timeit
from pathlib import Path

from pig_latin import PigLatinEncoder

class TestPigLatinEncoder(unittest.TestCase):

    def test_encode_string(self):
        word = "string"
        correct_encoding = "ingstray"

        ple = PigLatinEncoder()
        result = ple.encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_latin(self):
        word = "latin"
        correct_encoding = "atinlay"

        ple = PigLatinEncoder()
        result = ple.encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_idle(self):
        word = "idle"
        correct_encoding = "idleay"

        ple = PigLatinEncoder()
        result = ple.encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_empty(self):
        word = ""
        correct_encoding = ""

        ple = PigLatinEncoder()
        result = ple.encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_no_vowels(self):
        word = "str"
        correct_encoding = "stray"

        ple = PigLatinEncoder()
        result = ple.encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_titlecase(self):
        word = "Look"
        correct_encoding = "Ooklay"

        ple = PigLatinEncoder()
        result = ple.encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_uppercase(self):
        word = "LOOK"
        correct_encoding = "OOKLAY"

        ple = PigLatinEncoder()
        result = ple.encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_punct(self):
        word = "air,"
        correct_encoding = "airay,"

        ple = PigLatinEncoder()
        result = ple.encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_punct2(self):
        word = "What???"
        correct_encoding = "Atwhay???"

        ple = PigLatinEncoder()
        result = ple.encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_punct3(self):
        word = "***"
        correct_encoding = "ay***"

        ple = PigLatinEncoder()
        result = ple.encode_word(word)

        self.assertEqual(result, correct_encoding)

    def test_encode_file_1(self):
        md_ch1 = Path("pig_latin/data/2701-0-ch1.txt")
        pl_md_ch1 = Path("pig_latin/data/2701-0-ch1-pl.txt")
        result1_md_ch1 = Path("pig_latin/data/2701-0-ch1-pl-result-1.txt")

        ple = PigLatinEncoder()
        ple.encode_file_1(md_ch1, result1_md_ch1)

        self.assertEqual(filecmp.cmp(result1_md_ch1, pl_md_ch1), True)

    def test_encode_file_2(self):
        md_ch1 = Path("pig_latin/data/2701-0-ch1.txt")
        pl_md_ch1 = Path("pig_latin/data/2701-0-ch1-pl.txt")
        result2_md_ch1 = Path("pig_latin/data/2701-0-ch1-pl-result-2.txt")

        ple = PigLatinEncoder()
        ple.encode_file_2(md_ch1, result2_md_ch1)

        self.assertEqual(filecmp.cmp(result2_md_ch1, pl_md_ch1), True)

    def test_speed(self):
        loops = 20

        setup1 = """\
from pathlib import Path
from pig_latin import PigLatinEncoder
md_ch1 = Path("pig_latin/data/2701-0.txt")
result1_md_ch1 = Path("pig_latin/data/2701-0-result-1-speed.txt")
ple = PigLatinEncoder()
ple.encode_file_1(md_ch1, result1_md_ch1)"""
        time1 = timeit.timeit(setup1, number=loops)
        print("\nTiming " + str(loops) + " loops of encode_file_1: " , time1)

        setup2 = """\
from pathlib import Path
from pig_latin import PigLatinEncoder
md_ch1 = Path("pig_latin/data/2701-0.txt")
result2_md_ch1 = Path("pig_latin/data/2701-0-result-2-speed.txt")
ple = PigLatinEncoder()
ple.encode_file_2(md_ch1, result2_md_ch1)"""
        time2 = timeit.timeit(setup2, number=loops)
        print("\nTiming " + str(loops) + " loops of encode_file_2: " , time2)

