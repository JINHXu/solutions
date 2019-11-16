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
