# ATM Design

* Bank Class
  * Has the Bank constructor, which generates a bank
  * Card_nums and pins can be added to the bank with add_entry() method
  * add_account() only works for existing card_nums, program will do nothing if it doesn't exist
  * check_pin() takes card_num and pin_num to verify, this ensures ATM doesn't receive pin from Bank
  * update_account() is used by ATM to change balances

* ATM Class
  * Constructor takes in a Bank obj and cash_bin
  * swipe() methods takes in card_num and pin to check if valid. 
  * A proper user interface would call this method after invoking user input for pin. 
  * account_select() lets user select their account if valid pin was entered
  * account_actions() method is the way balance/withdraw/deposit are implemented. 
  * __call__ function is the very basic driver of the ATM. 
    * It is a driver of ATM, that runs through a list of actions and returns messages
    * This is useful for testing
    * A user interface would behave similarly logic-wise (only entering actions after valid pin, etc), but would await user input
    * Another engineer can see from this function how to go about using swipe(), account_selection(), and account_actions()
  
 ### Testing the Program
 This program can be tested by simply running:
 
 ```python3 test_ATM.py ```
 
 in the command line
 