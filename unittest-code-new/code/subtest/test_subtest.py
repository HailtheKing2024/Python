# subtest/test_subtest.py
import unittest


def is_even(num):
    return num % 2 == 0


class SubTestsTest(unittest.TestCase):
    def test_values(self):
        for num in [2, 4, -8, -10]:
            with self.subTest(num=num):
                self.assertTrue(is_even(num))

        for num in [1, 3, -7, -9]:
            with self.subTest(num=num):
                self.assertFalse(is_even(num))

    def test_failure(self):
        for num in [2, 4, -8, -11]:
            with self.subTest(num=num):
                self.assertTrue(is_even(num))
