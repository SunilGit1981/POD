import unittest
from math_utils import factorial

class TestFactorial(unittest.TestCase):

    # --- Test cases for valid non-negative integer inputs ---

    def test_factorial_zero(self):
        """Test that factorial(0) correctly returns 1 as per definition."""
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        """Test that factorial(1) correctly returns 1 as per definition."""
        self.assertEqual(factorial(1), 1)

    def test_factorial_two(self):
        """Test that factorial(2) correctly returns 2 (2*1)."""
        self.assertEqual(factorial(2), 2)

    def test_factorial_three(self):
        """Test that factorial(3) correctly returns 6 (3*2*1)."""
        self.assertEqual(factorial(3), 6)

    def test_factorial_five(self):
        """Test that factorial(5) correctly returns 120 (5*4*3*2*1)."""
        self.assertEqual(factorial(5), 120)

    def test_factorial_ten(self):
        """Test that factorial(10) correctly returns 3,628,800."""
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_thirteen(self):
        """Test factorial with a slightly larger number (13!), which is 6,227,020,800."""
        self.assertEqual(factorial(13), 6227020800)

    # --- Test cases for invalid negative integer inputs ---

    def test_factorial_negative_one_raises_value_error(self):
        """Test that factorial(-1) raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "Factorial is not defined for negative numbers."):
            factorial(-1)

    def test_factorial_negative_large_raises_value_error(self):
        """Test that factorial with a larger negative number (e.g., -10) raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "Factorial is not defined for negative numbers."):
            factorial(-10)

    # --- Test cases for invalid non-integer type inputs ---

    def test_factorial_float_raises_type_error(self):
        """Test that factorial with a float (e.g., 2.5) raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial(2.5)
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial(0.0) # Even 0.0 is a float

    def test_factorial_string_raises_type_error(self):
        """Test that factorial with a string (e.g., "hello") raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial("hello")
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial("5")

    def test_factorial_none_raises_type_error(self):
        """Test that factorial with None raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial(None)

    def test_factorial_list_raises_type_error(self):
        """Test that factorial with a list raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial([1, 2])
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial([])

    def test_factorial_tuple_raises_type_error(self):
        """Test that factorial with a tuple raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial((1,))
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial(())

    def test_factorial_set_raises_type_error(self):
        """Test that factorial with a set raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial({1, 2})
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial(set())

    def test_factorial_dictionary_raises_type_error(self):
        """Test that factorial with a dictionary raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial({'a': 1})
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            factorial({})

    # --- Test cases for boolean inputs (which are subclasses of int) ---

    def test_factorial_true_boolean(self):
        """Test that factorial(True) returns 1 (as True evaluates to 1 in int contexts)."""
        self.assertEqual(factorial(True), 1)

    def test_factorial_false_boolean(self):
        """Test that factorial(False) returns 1 (as False evaluates to 0 in int contexts, and 0! is 1)."""
        self.assertEqual(factorial(False), 1)

if __name__ == '__main__':
    unittest.main()