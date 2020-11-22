class Bank:
    def __init__(self):
        self.bank_data = {}

    def add_entry(self, card_num, pin_num, acc, bal):
        self.bank_data[card_num] = {"pin":pin_num, "account":{acc:bal}}

    def add_account(self, card_num, acc, bal):
        if card_num in self.bank_data:
            self.bank_data[card_num]["account"][acc] = bal

    def check_pin(self, card_num, entered_pin):
        if card_num in self.bank_data and self.bank_data[card_num]["pin"] == entered_pin:
            return self.bank_data[card_num]["account"]
        else:
            return None

    def update_account(self, card_num, acc, amt):
        if self.bank_data[card_num]["account"][acc] in self.bank_data[card_num]["account"]:
            self.bank_data[card_num]["account"][acc] = amt
            return True
        else:
            return False
