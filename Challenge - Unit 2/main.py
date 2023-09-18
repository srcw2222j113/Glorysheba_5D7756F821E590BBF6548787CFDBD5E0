class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount. Amount must be greater than 0."

    def withdraw(self, amount):
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
            else:
                return "Insufficient funds."
        else:
            return "Invalid withdrawal amount. Amount must be greater than 0."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name} (Account #: {self.__account_number}): ${self.__account_balance}"


# Get user input for creating an account
account_number = input("Enter account number: ")
account_holder_name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))

# Create an instance of the BankAccount class
account = BankAccount(account_number, account_holder_name, initial_balance)

# Perform transactions based on user input
while True:
    print("\nOptions:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")
    
    choice = input("Select an option (1/2/3/4): ")
    
    if choice == '1':
        amount = float(input("Enter the deposit amount: "))
        print(account.deposit(amount))
    elif choice == '2':
        amount = float(input("Enter the withdrawal amount: "))
        print(account.withdraw(amount))
    elif choice == '3':
        print(account.display_balance())
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
