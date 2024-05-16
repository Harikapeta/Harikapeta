class ATM:
    def __init__(self):
        self.users = {
            'krishna': {'password': 'abc123', 'pin': 1234, 'balance': 2000},
            'kumar': {'password': 'ab12', 'pin': 2345, 'balance': 2000},
            'kaushik': {'password': 'abc12', 'pin': 3456, 'balance': 2000}
        }
        self.current_user = None
        self.login_attempts = 0
        self.MENU_OPTIONS = {
            1: 'Withdraw',
            2: 'Deposit',
            3: 'Balance',
            4: 'Change Password',
            5: 'Exit'
        }

    def login(self):
        username = input("Enter your username: ")
        if username not in self.users:
            print("Invalid username")
            return
        password = input("Enter your password: ")
        if password != self.users[username]['password']:
            print("Invalid password")
            return
        self.current_user = username
        self.login_attempts = 0
        self.show_menu()

    def show_menu(self):
        print("\n")
        print("Menu:")
        for option, description in self.MENU_OPTIONS.items():
            print(f"{option} --> {description}")
        while True:
            try:
                option = int(input("Enter your option: "))
                if 1 <= option <= 5:
                    self.handle_option(option)
                    break
                else:
                    print("Invalid option. Please choose a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def handle_option(self, option):
        if option == 1:
            self.withdraw()
        elif option == 2:
            self.deposit()
        elif option == 3:
            self.show_balance()
        elif option == 4:
            self.change_password()
        elif option == 5:
            self.exit()

    def withdraw(self):
        while True:
            try:
                amount = int(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Invalid amount. Please enter a positive number.")
                    continue
                pin = int(input("Enter your PIN: "))
                if pin != self.users[self.current_user]['pin']:
                    print("Invalid PIN")
                    continue
                if amount > self.users[self.current_user]['balance']:
                    print("Insufficient balance")
                    continue
                self.users[self.current_user]['balance'] -= amount
                print("Withdrawal successful")
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        self.show_menu()

    def deposit(self):
        while True:
            try:
                amount = int(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Invalid amount. Please enter a positive number.")
                    continue
                pin = int(input("Enter your PIN: "))
                if pin != self.users[self.current_user]['pin']:
                    print("Invalid PIN")
                    continue
                self.users[self.current_user]['balance'] += amount
                print("Deposit successful")
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        self.show_menu()

    def show_balance(self):
        while True:
            try:
                pin = int(input("Enter your PIN: "))
                if pin != self.users[self.current_user]['pin']:
                    print("Invalid PIN")
                    continue
                print(f"Your balance is {self.users[self.current_user]['balance']}")
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        self.show_menu()

    def change_password(self):
        while True:
            try:
                pin = int(input("Enter your PIN: "))
                if pin != self.users[self.current_user]['pin']:
                    print("Invalid PIN")
                    continue
                current_password = input("Enter your current password: ")
                if current_password != self.users[self.current_user]['password']:
                    print("Invalid password")
                    continue
                new_password = input("Enter your new password: ")
                confirm_password = input("Confirm your new password: ")
                if new_password != confirm_password:
                    print("Passwords do not match")
                    continue
                self.users[self.current_user]['password'] = new_password
                print("Password changed successfully")
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        self.show_menu()

    def exit(self):
        print("Thank you for using our ATM system")
        exit()

atm = ATM()
atm.login()
