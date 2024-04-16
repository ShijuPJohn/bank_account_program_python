import random


class Bank:
    def __init__(self):
        self.accounts = {}
        f = open('accounts_info.txt', 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            ac_info_list = line.split()
            self.accounts[ac_info_list[0]] = {'Name': ac_info_list[1], 'Balance': int(ac_info_list[2])}

    def create_account(self, name):
        account_number = self.generate_account_number()
        self.accounts[account_number] = {'Name': name, 'Balance': 0}
        print('Account created successfully.')
        print("Account number:", account_number)
        print('Account holder name:', name)
        print('Opening balance: INR 0')

    def generate_account_number(self):
        return str(random.randint(100000, 999999))

    def display_account_details(self, account_number):
        if account_number in self.accounts:
            print('Account Number:', account_number)
            print('Account Holder Name', self.accounts[account_number]['Name'])
            print('Account Balance:', 'INR.' + str(self.accounts[account_number]['Balance']))
        else:
            print("Account not found!")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['Balance'] += amount
            print('Deposit successful')
            print('New Balance:', 'INR.' + str(self.accounts[account_number]['Balance']))
        else:
            print('Account not found!')

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]['Balance'] - amount > 500:
                self.accounts[account_number]['Balance'] -= amount
                print('Withdrawal successful')
                print('New balance:', 'INR.', str(self.accounts[account_number]["Balance"]))
            else:
                print("Insufficient balance. Minimum balance of Rs.500 must be maintained")
        else:
            print('Account not found')

    def save(self):
        f = open('accounts_info.txt', 'w')
        for account_number in self.accounts:
            f.write(
                f"{account_number} {self.accounts[account_number]['Name']} {self.accounts[account_number]['Balance']}\n")
        f.close()


bank = Bank()

print('WELCOME')

while True:
    print('1 Create New Account')
    print('2 Display Account Details')
    print('3 Deposit')
    print('4 Withdraw')
    print('5 Quit')

    choice = input('Enter you choice:')

    if choice == '1':
        name = input("Enter your name:")
        bank.create_account(name)
    elif choice == '2':
        account_number = input("Enter account number:")
        bank.display_account_details(account_number)
    elif choice == '3':
        account_number = input('Enter account number:')
        amount = int(input("Enter amount to be deposited: "))
        bank.deposit(account_number, amount)
    elif choice == '4':
        account_number = input("Enter account number: ")
        amount = int(input("Enter amount to withdraw:"))
        bank.withdraw(account_number, amount)
    elif choice == '5':
        print("Thank you, See You Again")
        bank.save()
        break
    else:
        print('Invalid Please try again')
