import unittest
import highestoccuringnumber

class CheckHighestOccuringNumber(unittest.TestCase):
    
    def test_that_highest_occuring_number_function_gives_an_expected_result_of_the_frequency_of_the_highest_occuring_number_in_an_array(self):
        actual =highestoccuringnumber.highest_occuring_number({1, 2, 2, 2, 3})
        expected = 3
        self.assertEqual(actual, expected)
        
        actual =highestoccuringnumber.highest_occuring_number({1, 5, 5, 6, 4})
        expected = 2
        self.assertEqual(actual, expected)
      
        
        