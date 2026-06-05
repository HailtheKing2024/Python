# setup/test_setup.py
import unittest


class DemoSetupTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setup class")
        cls.common_data = (1, 2, 3)

    @classmethod
    def tearDownClass(cls):
        print("Teardown class")

    def setUp(self):
        print("  setUp", self.common_data, hasattr(self, "specific_data"))
        self.specific_data = (4, 5, 6)

    def tearDown(self):
        print("  tearDown")

    def assertAndDisplay(self, name):
        self.assertTrue(True)
        print(f"    {name} {self.common_data} {self.specific_data}")

    def test_ex1(self):
        self.assertAndDisplay("ONE")

    def test_ex2(self):
        self.assertAndDisplay("TWO")

    def test_ex3(self):
        self.assertAndDisplay("THREE")
