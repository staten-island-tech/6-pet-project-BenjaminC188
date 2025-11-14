class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

    def _money(self, money):
        self.money += money

    

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")

class Pet:
    def __init__(self, name, _happiness):
        self.name = name
        self._happiness = _happiness

    def play(self):
        self._happiness += 2

    def show_status(self):
        print(f"{self.name} has {self._happiness} happiness")


ben = Hero("ben", 150, ["potion"])
ben.buy({"title": "Sword", "atk": 34})
print(ben.__dict__)

dog = Pet("dog", 10)
dog.play()
print(dog.__dict__)


