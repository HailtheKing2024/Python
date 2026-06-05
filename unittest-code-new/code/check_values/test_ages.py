# check_values/test_age.py
from unittest import TestCase

from ages import categorize


class AgeTest(TestCase):
    def test_child(self):
        """Test for 'child'"""
        expected = "child"
        result = categorize(0)
        self.assertEqual(expected, result)

        result = categorize(9)
        self.assertEqual(expected, result)

    def test_teen(self):
        """Test for 'teen'"""
        expected = "teen"
        result = categorize(10)
        self.assertEqual(expected, result)

        result = categorize(18)
        self.assertEqual(expected, result)

    def test_adult(self):
        """Test for 'adult'"""
        expected = "adult"
        result = categorize(19)
        self.assertEqual(expected, result)

        result = categorize(150)
        self.assertEqual(expected, result)

    def test_age_error(self):
        """Test error handling"""
        expected = "invalid age "
        result = categorize(-1)
        self.assertEqual(expected + "-1", result)

        result = categorize(151)
        self.assertEqual(expected + "151", result)
