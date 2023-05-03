class VK_Account:
    def __init__(self, user_id):
        print('__init__ called')
        self.user_id = user_id

    @staticmethod
    def validate(user_id):
        if len(user_id) > 7:
            return True
        else:
            return False
        

account_numbers = ['8' * 12, "7" * 12, "001", "2222"*2, "23435" ]

for element in account_numbers:
    if VK_Account.validate(element):
        print("we can use", element, "to create a vk account")
    else:
        print("The account number", element, "is invalid")