from django.test import TestCase

class lorenzo_baroneTestCase(TestCase):
    def test_basic_addition(self):
        # Basic addition test
        result = 1 + 1
        self.assertEqual(result, 2, "Addition result is incorrect")

    def test_negative_numbers(self):
        # Test negative numbers
        result = -5 + 10
        self.assertEqual(result, 5, "Addition of negative numbers is incorrect")

    def test_addition_with_zero(self):
        # Test zero
        result = 0 + 100
        self.assertEqual(result, 100, "Addition with zero is incorrect")

    def test_large_numbers(self):
        # Test large numbers
        result = 999999999 + 1
        self.assertEqual(result, 1000000000, "Addition of large numbers is incorrect")

    def test_floating_point_addition(self):
        # Test floating-point addition
        result = 1.5 + 2.3
        self.assertAlmostEqual(result, 3.8, places=2, msg="Floating-point addition is incorrect")

    def test_string_concatenation(self):
        # Test string concatenation
        result = "Hello" + " " + "World"
        self.assertEqual(result, "Hello World", "String concatenation is incorrect")
