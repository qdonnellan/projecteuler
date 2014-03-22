from problems_01_25.problem_04 import  largest_palindrome
import unittest

class Problem04Test(unittest.TestCase):
    """
    test the implementation of problem 04
    """

    def test_product_of_two_digit_numbers(self):
        """
        the largest palindrome which is the product of 2, 2 digit
        numbers is 9009: 99 x 91
        """
        self.assertEqual(largest_palindrome(2), 9009)

    @unittest.skip('this test takes a while!')
    def test_product_of_four_digit_numbers(self):
        """
        the largest palindrome which is the product 2, 4 digit
        numbers is 99000099
        """
        self.assertEqual(largest_palindrome(4), 99000099)
