"""
    Author: LeeTuah
    Team: Dillusioners
    Time: 11:38 a.m. IST
    For: League
"""

import random
import os
import json
import getpass

class Automobile:
    def __init__(self):
        self.id: int = 0
        self.isLoggedIn: bool = False
        self.data: dict = {}
        self.clr: str = ""

        if(os.name == 'posix'):
            self.clr = 'clear'
        else:
            self.clr = 'cls'

        if not os.path.exists('ids'):
            os.mkdir('ids')
    
    def register(self):
        os.system(self.clr)
        print("Welcome to the Register menu!\nPlease Enter Answers to the questions accordingly!")
        try:
            name: str = input("What is your name? ")
            age: int = int(input("What is your age? "))
            email: str = input("Enter your E-Main: ")
            password: str = getpass.getpass(prompt="Enter a password for your account (Must be more than 8 characters): ")
            _id: int = 0

            for _ in range(10):
                _id = (10 * _id) + random.randint(1, 9)

            _data: dict = {
                "name": name,
                "age": age,
                "email": email,
                "pass": password,
                "ID": _id
            }

            with open(f'ids/{_id}.json', 'w') as file:
                file.write(json.dumps(_data))
            
            print(f"Your ID is {_id}. This is important and make sure you donot forget it!")
            _ = input("Enter any value to return to main menu: ")

        except Exception as ex:
            print(ex)
    
    def login(self):
        os.system(self.clr)
        if(self.isLoggedIn):
            print("You are already logged in!!")
        
        else:
            _data: dict = {}
            try:
                _id: int = int(input("Enter your ID: "))
                with open(f'ids/{_id}.json', 'r') as file:
                    _data = json.load(file)

                _password: str = getpass.getpass(prompt="Enter your pass to know it's really you: ")
                if(_password == _data["pass"]):
                    print("You have logged in!")
                    self.isLoggedIn = True
                    self.data = _data
                    self.id = -_data["ID"]
                
                else:
                    print("Wrong password!")

            except Exception as ex:
                print(ex)
        
        _ = input("Enter any value to leave the login menu: ")

    def book(self):
        os.system(self.clr)
        print("Book an Auto\n")

        start = input("Enter starting destination: ")
        end = input("Enter ending destination: ")
        try:
            pas: int = int(input("How many passengers? "))
            dist: int = int(input("Distance between two places in kms: "))
            print(f"The price for auto is ${dist*10*pas}")
            sure = input("Are you sure about this?(Y/n): ")
            if(sure[0] == 'y' or sure[0] == 'Y'):
                print("Placed order!")

            else:
                print("Cancelling order!")
                
        except Exception as ex:
            print(ex)


    def menu(self):
        os.system(self.clr)
        running: bool = True
        print("Welcome to Dillusioner's Automobile Store")

        while running:
            os.system(self.clr)
            print("\nChoose any one of the following choices: ")
            print("1. Register\n2. Login\n3. Book an Auto\n4. Exit")

            try:
                choice: int = int(input(">> "))
            except Exception as ex:
                print(ex)
                continue

            if(choice == 4):
                print("Thanks for checking out the Automobile App")
                running = False

            elif(choice == 1):
                self.register()
            
            elif(choice == 2):
                self.login()

            elif(choice == 3):
                self.book()




def main():
    var: Automobile = Automobile()
    var.menu()

if __name__ == '__main__':
    main()