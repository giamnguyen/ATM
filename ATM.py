class ATM:
    def __init__(self, bank, cash_bin):
        self.bank = bank
        self.cash_bin = cash_bin
        self.accounts = None

    def swipe(self, card_num, pin):
        self.accounts = self.bank.check_pin(card_num, pin)
        if self.accounts is None:
            return 0, "Invalid Card or Incorrect Pin!"
        else:
            return 1, "Welcome!"

    def account_select(self, acc):
        if acc in self.accounts:
            return True
        else:
            return False

    def account_actions(self, card_num, acc, action, amt=0):
        if action == "See Balance":
            return self.accounts[acc], 1
        elif action == "Withdraw":
            if self.accounts[acc] >= amt and self.cash_bin >= amt:
                new_balance = self.accounts[acc] - amt
                self.accounts[acc] = new_balance
                self.bank.update_account(card_num, acc, new_balance)
                return self.accounts[acc], 1
            else:
                return self.accounts[acc], 0
        elif action == "Deposit":
            new_balance = self.accounts[acc] + amt
            self.cash_bin += amt
            self.accounts[acc] = new_balance
            self.bank.update_account(card_num, acc, new_balance)
            return self.accounts[acc], 1
        else:
            return self.accounts[acc], 2

    # This is a method to test functionality
    def __call__(self, card_num, pin, acc, action_list):
        leave = False
        while leave is not True:
            v, m = self.swipe(card_num, pin)
            if v == 0:
                return "Invalid Card or Incorrect Pin!"
            check = self.account_select(acc)
            if check is False:
                return "Invalid Account!"
            for action in action_list:
                if action[0] == "Leave":
                    return "Gracefully departed"
                balance, bit = self.account_actions(card_num, acc, action[0], action[1])
                if bit == 0:
                    continue
                elif bit == 2:
                    return "Invalid action"
                else:
                    continue
            return "Actions completed"
