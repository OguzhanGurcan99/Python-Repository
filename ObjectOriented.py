class Bank_Account:
    def __init__(self,owner,age,gender,balance=967569):
        if age<21:
            print(f"You are not allowed to open a bank account {owner}!")
        else:
            self.owner = owner
            self.age = age
            self.gender = gender
            self.balance = balance

            if gender == "Female":
                if age>21 and age<30:
                    self.balance += 5000
    def deposit(self,*x):
        for i in x:
            self.balance += i
    def withdraw(self,*x):
        for i in x:
            if self.balance>i:
                self.balance -= i
            else:
                print("Out of balance limit!!")
                print(f"Maximum balance to withdraw:{self.balance}")

    def check_balance(self):
        print(self.balance)


person1= Bank_Account("John",30,"Male")
person1.deposit(700,300,1000)
person1.withdraw(600,400)
person1.check_balance()

person2 = Bank_Account("Elly",27,"Female")
person2.deposit(700,300,1000)
person2.withdraw(600,400)
person2.check_balance()

person3= Bank_Account("Micheal",45,"Male",500)
person3.deposit(700,300,1000)
person3.withdraw(5600,400)



