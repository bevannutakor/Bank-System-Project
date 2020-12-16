import random
from random import randint

global userPins
userPins = ['0001', '0002', '0003', '0004']

class BankAccount():
    def __init__(self, users=[], checkings=0, savings=0, business=0):
        self.users = users
        self.checkings = checkings
        self.savings = savings
        self.business = business
    
    def userAccount(self):
        print("------Bank Information-----")
        print("Checkings balance: ${}".format(self.checkings))
        print("Savings balance: ${}".format(self.savings))
        print("Business Account: ${}".format(self.business))


        withdraw_or_deposit = input("Press 'W' to withdraw money or press 'D' to deposit money or press any other button to exit: ")

        if withdraw_or_deposit == 'W':
            self.withdraw()
            self.userAccount()
        elif withdraw_or_deposit == 'D':
            self.deposit()
            self.userAccount()
        else:
            return None

    def withdraw(self):
        withdraw_account = input("choose which account you want to draw from: ")

        withdraw_amt = int(input("How much would you like to withdraw: "))

        if withdraw_account == "checkings":
            self.checkings = self.checkings - withdraw_amt
            print("You now have ${} in your checkings".format(self.checkings))

        elif withdraw_account == "savings":
            self.savings = self.savings - withdraw_amt
            print("You now have ${} in your checkings".format(self.savings))

        elif withdraw_account == "business":
            self.business = self.business - withdraw_amt
            print("You now have ${} in your checkings".format( self.business))



    def deposit(self):
        deposit_account = input("choose which account you want to draw from: ")

        deposit_amt = int(input("How much would you like to deposit: "))

        if deposit_account == "checkings":
            self.checkings = self.checkings + deposit_amt
            print("You now have ${} in your checkings".format(self.checkings))

        elif deposit_account == "savings":
            self.savings = self.savings + deposit_amt
            print("You now have ${} in your checkings".format(self.savings))

        elif deposit_account == "business":
            self.business = self.business + deposit_amt
            print("You now have ${} in your checkings".format( self.business))

    def signup(self):
        global new_name
        global new_pin
        new_name = input("Enter your name: ")

        new_pin = input("Enter your account pin: ")

        self.users.append(new_name)
        userPins.append(new_pin)
        print(self.users)
        print(userPins)


    def login(self):
        print("------Login------")
        login_input = input("What is your username: ")
        login_pin = input("What is your pin: ")

        if login_input == self.users[0] and login_pin == userPins[0]:
            self.userAccount()
        elif login_input == self.users[1] and login_pin == userPins[1]:
            self.userAccount()
        elif login_input == self.users[2] and login_pin == userPins[2]:
            self.userAccount()
        elif login_input == self.users[3] and login_pin == userPins[3]:
            self.userAccount()
        elif login_input == self.users[4] and login_pin == userPins[4]:
            self.userAccount()
        else:
            return print("Error")


       

    def start(self):

        login_signup_user = input("Type 'login' or 'signup': ")

        if login_signup_user == "login":
            self.login()

        elif login_signup_user == 'signup':
            self.signup()
            self.login()

        else:
            return print("The correct options were not chosen")

def main():
    checkValues = randint(1000, 1000000)
    savingValues = randint(1000, 1000000)
    businessValues = randint(1000, 1000000)
    account_user = BankAccount(["Jill", "Scott", "Mandy", "Billy"], checkValues, savingValues, businessValues)

    account_user.start()

main()