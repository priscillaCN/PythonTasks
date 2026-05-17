import unittest
import pybank

class ValidateEmailFunction(unittest.TestCase):
    
    def test_that_validate_email_function_exists(self):
        pybank.validate_email('priscilla@mail.com')
        
             
    def test_that_validate_email_function_can_count_length_of_email_characters(self):
        actual = pybank.validate_email('priscilla@mail.com')
        expected = 'valid email'
        self.assertEqual(expected, actual)
        

    def test_that_email_with_at_least_8_characters_returns_true(self):
        is_valid = pybank.validate_email('priscilla@mail.com')
        self.assertTrue(is_valid)
        
        
    def test_that_email_with_less_than_8_characters_returns_false(self):
        is_invalid = pybank.validate_email('pris@')
        self.assertTrue(is_invalid)
        
                
    def test_that_email_that_contains_the_at_symbol_returns_valid_email_message(self):
        actual = pybank.validate_email('priscilla@mail.com')
        expected = 'valid email'
        self.assertEqual(actual, expected)
        
        
    def test_that_email_that_does_not_contain_the_at_symbol_returns_invalid_email_message(self):
        actual = pybank.validate_email('priscillamail.com')
        expected = 'invalid email'
        self.assertEqual(actual, expected)
        
        
    def test_that_email_that_starts_with_the_at_symbol_returns_invalid_email_message(self):
        actual = pybank.validate_email('@priscillamail.com')
        expected = 'valid email'
        self.assertEqual(actual, expected)
        
        
    def test_that_email_that_ends_with_the_at_symbol_returns_invalid_email_message(self):
        actual = pybank.validate_email('priscillamail.com@')
        expected = 'valid email'
        self.assertEqual(actual, expected)
        


class CalculateBalanceFunction(unittest.TestCase):
    
    def test_that_calculate_balance_function_returns_accurate_balance_in_two_decimal_places(self):
        actual = pybank.calculate_balance([20000, 5000])
        expected = 25000.00
        self.assertEqual(actual, expected)
        
        actual = pybank.calculate_balance([20000, -5000])
        expected = 15000.00
        self.assertEqual(actual, expected)
        
        actual = pybank.calculate_balance([20000, -5000 -2.50 + 22.25])
        expected = 15019.75
        self.assertEqual(actual, expected)
        
        
    def test_that_calculate_balance_function_returns_zero_balance_given_that_transactions_is_empty(self):
        actual = pybank.calculate_balance([])
        expected = 0.00
        self.assertEqual(actual, expected)
        
        
    def test_that_calculate_balance_function_returns_insufficient_balance_message_given_that_total_is_less_than_zero(self):
        actual = pybank.calculate_balance([20000, -21000])
        expected = 'insufficient balance'
        self.assertEqual(actual, expected)
        
        

class PasswordStrengthFunction(unittest.TestCase):
    
    def test_that_password_strength_function_returns_strong_password_message_given_that_password_length_is_more_than_eight_characters(self):
        actual = pybank.password_strength('password')
        expected = 'strong password'
        self.assertEqual(actual, expected)
        
        
        def test_that_password_strength_function_returns_weak_password_message_given_that_password_length_is_less_than_eight_characters(self):
            actual = pybank.password_strength('passwo')
            expected = 'weak password'
            self.assertEqual(actual, expected)
            
            
class CalculateInterestFunction(unittest.TestCase):
    
    def test_that_apply_interest_function_returns_accurate_compound_interest_in_two_decimal_places(self):
        actual = pybank.apply_interest(50000, 0.10, 5)
        expected = 80525.50
        self.assertEqual(actual, expected)
        
        
    def test_that_apply_interest_function_rate_cannot_be_less_than_zero(self):
        with self.assertRaises(ValueError):
            pybank.apply_interest(50000, -0.10, 5)
    
    
    def test_that_apply_interest_function_years_cannot_be_less_than_one(self):
        with self.assertRaises(ValueError):
            pybank.apply_interest(50000, 0.10, 0.5)
    

class GetTransactionSummary(unittest.TestCase):

    def test_that_get_transaction_summary_function_returns_accurate_total_credit_of_20000_from_the_given_transaction_input(self):
        actual = pybank.get_transaction_summary([['credit', 2000], ['credit', 10000], ['credit', 5000], ['credit', 3000]])
        expected = 20000.00
        self.assertEqual(actual, expected)