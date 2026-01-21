class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner      # Приватное имя владельца
        self.__balance = balance  # Приватный баланс

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("You cannot deposit negative amount")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough money")
        elif amount <= 0:
            print("Amount must be positive")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

B1=BankAccount("Nick", 100)
B2=BankAccount("Iden", 5000)
B3=BankAccount("Grey", 3000)
B3.withdraw(3200)
print(B3.get_balance())