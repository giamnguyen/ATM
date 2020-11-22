import unittest
import Bank
import ATM

class TestATM(unittest.TestCase):

    def test_empty_bank(self):
        empty_bank = Bank.Bank()
        empty_atm = ATM.ATM(empty_bank, 0)
        valid, message = empty_atm.swipe(0, 0)
        self.assertEqual(valid, 0)

    def test_bank_1(self):
        test_bank = Bank.Bank()
        test_bank.add_entry(123456789, 1234, "checking", 1000)
        test_bank.add_account(123456789, "savings", 1000)
        test_bank.add_entry(987654321, 7321, "checking", 5000)
        test_atm = ATM.ATM(test_bank, 10000)
        action_list = [("See Balance",0), ("Withdraw", 40), ("Withdraw", 1000), ("Deposit", 100)]

        # These next test should be a correctly executing test case
        self.assertEqual(test_atm(987654321, 7321, "checking", action_list), "Actions completed")

        # Tests whether ATM handles overdraft attempt without crashing
        self.assertEqual(test_atm(123456789, 1234, "checking", action_list), "Actions completed")

        # Test incorrect PIN number
        self.assertEqual(test_atm(987654321, 1234, "checking", action_list), "Invalid Card or Incorrect Pin!")

        # Test incorrect Account number
        self.assertEqual(test_atm(876504321, 1234, "checking", action_list), "Invalid Card or Incorrect Pin!")
    
    def test_bank_2(self):
        test_bank = Bank.Bank()
        test_bank.add_entry(123456789, 1234, "checking", 1000)
        test_bank.add_account(123456789, "savings", 1000)
        test_bank.add_entry(987654321, 7321, "checking", 5000)
        test_atm = ATM.ATM(test_bank, 10000)
        cash_bin_over_action = [("See Balance", 0), ("Withdraw", 30000)]

        # Tests cash bin excess handling on account balance
        self.assertEqual(test_atm(987654321, 7321, "checking", cash_bin_over_action), "Actions completed")

        exit_action = [("See Balance", 0), ("Leave", 0)]
        self.assertEqual(test_atm(987654321, 7321, "checking", exit_action), "Gracefully departed")

if __name__ == '__main__':
    unittest.main()