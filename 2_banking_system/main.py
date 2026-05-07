class Account:
    def __init__(self,balance):
        self.__balance = balance
        self.history = []
    def deposit(self, amount):
        self.__balance += amount
        self.history.append(f"Deposited : {amount}")
    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            self.history.append(f"Withdrew : {amount}")
    def check_balance(self):
        return self.__balance
    def show_history(self):
        print(self.history) 
    
class SavingsAccount(Account):
    def interest(self, rate, time):
        Interest = self.check_balance() * rate * time 
        print(Interest)
    
class CurrentAccount(Account):
    def __init__(self, balance, limit):
        super().__init__(balance)
        self.limit = limit
    def withdraw(self, amount):
        if amount <= self.check_balance() + self.limit:
            new_balance = self.check_balance() - amount
            self._Account__balance = new_balance
        else:
            print("Overdraft limit exceeded")
            

acc1 = SavingsAccount(1000)
acc1.deposit(100)
acc1.withdraw(50)
acc1.withdraw(500)
acc1.interest(0.05, 1)
acc1.show_history()
acc2 = CurrentAccount(1000,500)
acc2.withdraw(1200)
acc2.withdraw(500)
