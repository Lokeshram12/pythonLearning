import unittest
from palindrome import is_palindrome  # Assuming is_palindrome is defined in palindrome.py

class TestIsPalindrome(unittest.TestCase):

    def test_palindrome_odd_length(self):
        self.assertTrue(is_palindrome("radar"))

    def test_palindrome_even_length(self):
        self.assertTrue(is_palindrome("madam"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_palindrome_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_palindrome_case_insensitive(self):
        self.assertTrue(is_palindrome("Racecar"))

    def test_palindrome_with_whitespace(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

if __name__ == '__main__':
    unittest.main()
