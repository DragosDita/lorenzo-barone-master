from django.test import TestCase


class TestLorenzoBarone(TestCase):
    def test_basic_addition(self):
        # Basic addition test
        result = 1 + 1
        self.assertEqual(result, 2, "1 + 1 = 2")

    def test_negative_numbers(self):
        # Test negative numbers
        result = -5 + 10
        self.assertEqual(result, 5, "-5 + 10 = 5")

    def test_addition_with_zero(self):
        # Test zero
        result = 0 + 100
        self.assertEqual(result, 100, "0 + 100 = 100")

    def test_large_numbers(self):
        # Test large numbers
        result = 999999999 + 1
        self.assertEqual(result, 1000000000, "999999999 + 1 = 1000000000")

    def test_floating_point_addition(self):
        # Test floating-point addition
        result = 1.5 + 2.3
        self.assertAlmostEqual(result, 3.8, places=2, msg="1.5 + 2.3 = 3.8")

    def test_string_concatenation(self):
        # Test string concatenation
        result = "Hello" + " " + "World"
        self.assertEqual(result, "Hello World", "'Hello' + ' ' + 'World' = 'Hello World'")
