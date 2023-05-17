from django.test import TestCase


class TestLorenzoBarone(TestCase):
    print("-----------------------------------------------------------------------")

    def test_basic_addition(self):
        # Basic addition test
        result = 1 + 2
        print("1 + 1 =", result)
        self.assertEqual(result, 2, "1 + 1 = 2")
        print("-----------------------------------------------------------------------")

    def test_negative_numbers(self):
        # Test negative numbers
        result = -5 + 10
        print("-5 + 10 =", result)
        self.assertEqual(result, 5, "-5 + 10 = 5")
        print("-----------------------------------------------------------------------")

    def test_addition_with_zero(self):
        # Test zero
        result = 0 + 100
        print("0 + 100 =", result)
        self.assertEqual(result, 100, "0 + 100 = 100")
        print("-----------------------------------------------------------------------")

    def test_large_numbers(self):
        # Test large numbers
        result = 999999999 + 1
        print("999999999 + 1 =", result)
        self.assertEqual(result, 1000000000, "999999999 + 1 = 1000000000")
        print("-----------------------------------------------------------------------")

    def test_floating_point_addition(self):
        # Test floating-point addition
        result = 1.5 + 2.3
        print("1.5 + 2.3 =", result)
        self.assertAlmostEqual(result, 3.8, places=2, msg="1.5 + 2.3 = 3.8")
        print("-----------------------------------------------------------------------")

    def test_string_concatenation(self):
        # Test string concatenation
        result = "Hello" + " " + "World"
        print("'Hello' + ' ' + 'World' =", result)
        self.assertEqual(result, "Hello World", "'Hello' + ' ' + 'World' = 'Hello World'")
