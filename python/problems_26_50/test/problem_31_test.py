import unittest
from problem_31 import coin_sum_combos

class Problem31Test(unittest.TestCase):
    '''
    test class for the implementation of 
    problem Euler problem 31
    '''

    def test_2_pence_known_case(self):
        '''
        test the known case for 2 pence

        2 pence only has a limited combination of coin combos:

        2p
        1p + 1p
        '''
        self.assertEqual(coin_sum_combos(2), 2)


    def test_5_pence_known_case(self):
        '''
        test the known case for 5 pence
        
        5 pence only has a limited combination of coin combos:

        5p
        2p + 2p + 1p
        2p + 1p + 1p + 1p
        1p + 1p + 1p + 1p + 1p

        So that's 4 different combinations
        '''
        self.assertEqual(coin_sum_combos(5), 4)

