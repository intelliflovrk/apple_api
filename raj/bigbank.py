import json


class Bigbank:

    def __init__(self):
        self.balance = 0
        self.retry = 3

    def log_in_page(self):
        print("Welcome to Big Bank !")
        login_or_register_resp = str(input("Enter '1' for Login [or] Enter '2' for Register."))
        if login_or_register_resp == '1':
            self.login()
        elif login_or_register_resp == '2':
            self.register()
        else:
            print("Invalid Input#.")
            self.log_in_page()

    def register(self):
        print("Oops, Registration service is not available yet.")
        """# firstname = str(input("Enter Firstname"))
        # lastname = str(input("Enter Lastname:"))
        # dob = str(input("Enter DOB [dd/mm/yyy]:"))
        # age = str(input("Enter Age:"))
        # email = str(input("Enter Email:"))
        # username = str(input("Enter Username:"))
        # password = str(input("Enter Password:"))
        # confirm_password = str(input("Confirm Password:"))"""
        self.log_in_page()

    def login(self):
        username = str(input("Enter Username:"))
        password = str(input("Enter Password:"))
        self.verify_login_credentials(username, password)
        return self

    def verify_login_credentials(self, username, password):
        with open('../credentials.json') as file:
            credentials = json.load(file)
            if username in credentials.keys():
                stored_password = credentials[username]
                if stored_password == password:
                    self.main_menu()
            else:
                if self.retry == 0:
                    print("Your account is blocked. Contact customer service.")
                    exit()
                print("Wrong credentials try again. \n You have", self.retry, "chance left.")
                while self.retry >= 1:
                    self.retry -= 1
                    self.login()
        return self

    def main_menu(self):
        print('===============================\n WELCOME TO BIG BANK \n Please Choose an Option \n Option 1: Withdrawl'
              ' \n Option 2: Deposit \n Option 3: Check_Balance \n Option 5: Exit \n ===============================')
        option = int(input('Choose an Option:'))
        if option == 1:
            self.withdraw()
        elif option == 2:
            self.deposit()
        elif option == 3:
            self.check_balance()
        elif option == 5:
            print("Thank you for visiting Big Bank.")
            exit()
        else:
            print('Invalid Input')
            self.main_menu()
        return self

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)
        print("\n Net Available Balance=", self.balance, "\n")
        self.exit_option()

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
            print("\n Net Available Balance=", self.balance)
        else:
            print("\nInsufficient balance\n")
        self.exit_option()

    def check_balance(self):
        print("\n Net Available Balance=", self.balance, "\n")
        self.exit_option()

    def exit_option(self):
        print("Enter '1' Main Menu")
        print("Enter '2' Exit")
        exit_option = str(input())
        if exit_option == '1':
            self.main_menu()
        elif exit_option == '2':
            print("Thank you for visiting Big Bank.")
            exit()
        else:
            print("Invalid option!")
            self.exit_option()
        return self


if __name__ == '__main__':
    b1 = Bigbank()
    b1.log_in_page()




