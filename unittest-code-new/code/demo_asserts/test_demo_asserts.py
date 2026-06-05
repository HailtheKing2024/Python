# demo_asserts/test_demo_asserts.py
from unittest import TestCase


class DemoAssertsTest(TestCase):
    def test_one(self):
        self.assertEqual(42, 42)
        self.assertNotEqual(42, 13)
        self.assertTrue(True)
        self.assertFalse(False)

        nums = [1, 2, 3]
        ref = nums
        self.assertIs(nums, ref)

        more_nums = [1, 2, 3]
        self.assertEqual(nums, more_nums)
        self.assertIsNot(nums, more_nums)

        self.assertIsNone(None)
        self.assertIsNotNone(42)

        self.assertIn(42, [42, 13])
        self.assertNotIn(42, [1, 2, 3])

        self.assertIsInstance(nums, list)
        self.assertNotIsInstance(nums, str)

        class ChildStr(str):
            pass

        self.assertIsSubclass(ChildStr, str)
        self.assertNotIsSubclass(ChildStr, list)

    def test_fail(self):
        self.assertEqual(42, 13)

    def test_fail_long(self):
        self.assertEqual(42, 13, "this is more information about 42!=13")

    def test_raises(self):
        with self.assertRaises(ValueError):
            raise ValueError("You should NOT see this error")

    def test_fail_raises(self):
        with self.assertRaises(ValueError):
            raise AttributeError("This will fail!!!")
