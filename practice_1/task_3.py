class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Пополнение: +{amount} сом")
        else:
            print("Сумма пополнения должна быть положительной!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Снятие: -{amount} сом")
        else:
            print("Недостаточно средств для снятия!")

    def show_balance(self):
        print(f"Баланс: {self.balance} сом")

    def __del__(self):
        print(f"Счёт владельца {self.owner} закрыт.")


# Пример использования
account = BankAccount("Hikmatulloh")
account.deposit(200)
account.withdraw(50)
account.show_balance()

del account  # вызовет __del__
