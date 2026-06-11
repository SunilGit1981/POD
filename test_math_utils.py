import unittest
from math_utils import factorial

class TestFactorial(unittest.TestCase):

    # Test cases for valid non-negative integer inputs

    def test_factorial_of_zero(self):
        """
        Test that factorial(0) correctly returns 1 as per definition.
        """
        self.assertEqual(factorial(0), 1, "Factorial of 0 should be 1")

    def test_factorial_of_one(self):
        """
        Test that factorial(1) correctly returns 1 as per definition.
        """
        self.assertEqual(factorial(1), 1, "Factorial of 1 should be 1")

    def test_factorial_of_two(self):
        """
        Test factorial(2) which should be 2.
        """
        self.assertEqual(factorial(2), 2, "Factorial of 2 should be 2")

    def test_factorial_of_three(self):
        """
        Test factorial(3) which should be 6.
        """
        self.assertEqual(factorial(3), 6, "Factorial of 3 should be 6")

    def test_factorial_of_five(self):
        """
        Test factorial(5) which should be 120.
        """
        self.assertEqual(factorial(5), 120, "Factorial of 5 should be 120")

    def test_factorial_of_ten(self):
        """
        Test factorial(10) which should be 3,628,800.
        """
        self.assertEqual(factorial(10), 3628800, "Factorial of 10 should be 3,628,800")

    # Test cases for invalid inputs (error handling)

    def test_factorial_of_negative_number(self):
        """
        Test that factorial raises ValueError for negative inputs.
        """
        with self.assertRaisesRegex(ValueError, "Factorial is not defined for negative numbers."):
            factorial(-1)
        with self.assertRaisesRegex(ValueError, "Factorial is not defined for negative numbers."):
            factorial(-5)

    def test_factorial_with_float_input(self):
        """
        Test that factorial raises TypeError for float inputs.
        """
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial(3.5)
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial(0.0) # Even for 0.0, it's a float

    def test_factorial_with_string_input(self):
        """
        Test that factorial raises TypeError for string inputs.
        """
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial("5")
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial("hello")

    def test_factorial_with_none_input(self):
        """
        Test that factorial raises TypeError for None input.
        """
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial(None)

    def test_factorial_with_list_input(self):
        """
        Test that factorial raises TypeError for list input.
        """
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial([5])
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial([])

    def test_factorial_with_boolean_input(self):
        """
        Test that factorial raises TypeError for boolean input.
        (Note: In Python, bool is a subclass of int, so False is 0 and True is 1.
         The function might return 1 for False and 1 for True due to this.
         If the intention is strictly 'int' and not 'bool-as-int', then this test
         might need to be adjusted or the function logic tightened if bool is
         to be explicitly disallowed as an 'int'. Given the current type check,
         isinstance(True, int) is True and isinstance(False, int) is True,
         so these would pass the type check and return 1.)
        """
        # Based on current `isinstance(n, int)` check, Booleans pass as integers.
        # False is equivalent to 0, True to 1.
        self.assertEqual(factorial(True), 1, "Factorial of True (1) should be 1")
        self.assertEqual(factorial(False), 1, "Factorial of False (0) should be 1")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)