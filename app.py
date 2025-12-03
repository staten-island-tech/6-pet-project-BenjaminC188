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

    def spend(self, amount):
        self.money -= amount


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")

    def spend(self, amount):
        self.__balance -= amount
        print(f"{self.owner} has {self.__balance} left")


"""Jillian = Hero("Jillian", 150, ["Potion"])
Jillian.buy({"title": "Sword", "atk": 34})
Jillian.spend(50)
print(Jillian.__dict__)

ben = Hero("ben", 150, ["potion"])
ben.buy({"title": "Sword", "atk": 34})
print(ben.__dict__)"""

class Pet:
    def __init__(self, name, _happiness, _energy, _hunger):
        self.name = name
        self._happiness = _happiness
        self._energy = _energy
        self._hunger = _hunger

    def _status(self):
        self._happiness = max(0, min(self._happiness, 100))
        self._energy = max(0, min(self._energy, 100))
        self._hunger = max(0, min(self._hunger, 100))

    def play(self):
        print(f"{self.name} is playing")
        self._happiness += 25
        self._energy -= 40
        self._hunger -= 20
        self._status()
        print(self.__dict__)

    def rest(self):
        print(f"{self.name} is sleep")
        self._energy += 50
        self._hunger += 40
        self._happiness -= 50
        self._status()
        print(self.__dict__)

    def eat(self):
        print(f"{self.name} is eating")
        self._hunger += 70
        self._energy += 10
        self._status()
        print(self.__dict__)

    def show_status(self):
        print(f"{self.name} has {self._happiness} happiness, {self._energy} energy, and {self._hunger} hunger.")
        
        if self._energy <= 0 or self._hunger <= 0 or self._happiness <= 0:
            print(f"{self.name} is dead.")
        elif self._hunger <= 20:
            print(f"{self.name} is starving.")
        elif self._happiness <= 0:
            print(f"{self.name} is depressed.")
        elif self._energy <= 25:
            print(f"{self.name} is tired.")
        elif self._hunger >= 100:
            print(f"{self.name} is full.")
        elif self._energy >= 100:
            print(f"{self.name} is not tired.")
        else:
            print(f"{self.name} is normal.")

dog = Pet("dog", 50, 50, 50)
dog.play()
dog.rest()
dog.eat()
dog.show_status()
print(dog.__dict__)














































"""
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
    
class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id
    
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
    
class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"
    
class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
    
    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
    
    def manage_system(self):
        return f"{self.name} ({self.role}) is managing the system"
    


student = Student("Alice", "alice@example.com", "S12345")
teacher = Teacher("Mr. Smith", "smith@example.com", "Mathematics")
administrator = Administrator("Ms. Johnson", "johnson@example.com", "Principal")

print(student.display_info())  
print(teacher.display_info()) 
print(administrator.display_info()) 
    
admin = Administrator("Ms. Johnson", "johnsom@example.com", "Principal")
print(admin.manage_system())

class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Subject: {self.subject}"
    
my_teacher = Teacher("Mr.Brown", "brown@example.com", "Science")
print(my_teacher.display_info())
"""