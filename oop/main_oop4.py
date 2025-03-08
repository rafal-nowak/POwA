class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute
        self.__balance = balance  # Private attribute

    # Public method to access private attribute
    def get_balance(self):
        return self.__balance

    # Public method to update private attribute
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


if __name__ == '__main__':
    account = BankAccount("12345", 1000)
    print("Account Balance:", account.get_balance())
    account.deposit(500)
    print("Updated Balance:", account.get_balance())