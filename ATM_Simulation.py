user_account = {
    "balance": 100000,
    "pin": "4554",
    "transactions": []
}

def atm_menu():
    """Displays the ATM menu options."""
    print("\nWelcome to the ATM!")
    print("1. Balance Inquiry")
    print("2. Cash Withdrawal")
    print("3. Cash Deposit")
    print("4. Change PIN")
    print("5. Transaction History")
    print("6. Exit")

def balance_inquiry():
    """Display the current balance."""
    print(f"\nYour current balance is: ₹{user_account['balance']}")

def cash_withdrawal():
    """Withdraw cash from the account."""
    amount = int(input("\nEnter the amount to withdraw: ₹"))
    if amount <= user_account["balance"]:
        user_account["balance"] -= amount
        user_account["transactions"].append(f"Withdrawn: ₹{amount}")
        print(f"Transaction successful! ₹{amount} withdrawn.")
    else:
        print("Insufficient balance!")

def cash_deposit():
    """Deposit cash into the account."""
    amount = int(input("\nEnter the amount to deposit: ₹"))
    user_account["balance"] += amount
    user_account["transactions"].append(f"Deposited: ₹{amount}")
    print(f"Transaction successful! ₹{amount} deposited.")

def change_pin():
    """Change the user's PIN."""
    old_pin = input("\nEnter your current PIN: ")
    if old_pin == user_account["pin"]:
        new_pin = input("Enter your new PIN: ")
        confirm_pin = input("Confirm your new PIN: ")
        if new_pin == confirm_pin:
            user_account["pin"] = new_pin
            print("PIN successfully changed!")
        else:
            print("New PIN and confirmation do not match.")
    else:
        print("Incorrect current PIN!")

def transaction_history():
    """Display the transaction history."""
    if user_account["transactions"]:
        print("\nTransaction History:")
        for transaction in user_account["transactions"]:
            print(f" - {transaction}")
    else:
        print("No transactions found.")
def main():
    while True:
        atm_menu()
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            balance_inquiry()
        elif choice == "2":
            cash_withdrawal()
        elif choice == "3":
            cash_deposit()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            transaction_history()
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()
