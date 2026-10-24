from unittest import TestCase

from credit_card_validator import get_credit_card_type,check_card_validity

class TestCreditCard(TestCase):

    def test_that_any_credit_lessthan_13_or_greaterthan_19(self):
        credit_card_type = "Invalid"
        credit_card_number = "9906758453"
        credit_card_digit_length = "10"
        credit_card_validity_status = "Invalid"
        
        self.assertEqual(len(credit_card_type), 10)
