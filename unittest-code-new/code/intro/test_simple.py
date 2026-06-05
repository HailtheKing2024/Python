# intro/test_simple.py
from unittest import TestCase

from simple import say_hello


class SimpleTestCase(TestCase):
    def test_say_hello(self):
        say_hello()
