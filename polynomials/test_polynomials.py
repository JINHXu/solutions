#!/usr/bin/env/python3

import unittest

from polynomials import polynomial_one, polynomial_two, polynomial_three

class TestPolynomials(unittest.TestCase):

    def test_polynomial_a(self):
        # computing x^2 + 2 + 5
        # x = 2, result should be 4 + 4 + 5 = 13

        result_one = polynomial_one(2, 2, [1, 2, 5])
        result_two = polynomial_two(2, 2, [1, 2, 5])
        result_three = polynomial_three(2, 2, [1, 2, 5])

        self.assertEqual(result_one, 13)
        self.assertEqual(result_two, 13)
        self.assertEqual(result_three, 13)

    def test_polynomial_b(self):
        # computing 5x + 1
        # x = 3, result should be 15 + 1 = 16

        result_one = polynomial_one(3, 1, [5, 1])
        result_two = polynomial_two(3, 1, [5, 1])
        result_three = polynomial_three(3, 1, [5, 1])

        self.assertEqual(result_one, 16)
        self.assertEqual(result_two, 16)
        self.assertEqual(result_three, 16)

    def test_polynomial_c(self):
        # computing 11x^9 + 9x^7 + 5x^3 + 3x
        # x = 2, result should be 11*512 + 9*128 + 7*32 + 5*8 + 6 = 7054

        result_one = polynomial_one(2, 9, [11, 0, 9, 0, 7, 0, 5, 0, 3, 0])
        result_two = polynomial_two(2, 9, [11, 0, 9, 0, 7, 0, 5, 0, 3, 0])
        result_three = polynomial_three(2, 9, [11, 0, 9, 0, 7, 0, 5, 0, 3, 0])

        self.assertEqual(result_one, 7054)
        self.assertEqual(result_two, 7054)
        self.assertEqual(result_three, 7054)
        