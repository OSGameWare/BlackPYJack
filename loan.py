
import usrinfo

def process_loan():
    print("\033c")
    usrinfo.apply_interest()  # Check and apply interest if needed
    
    while True:
        try:
            amount = int(input(f"\nYour money: ${usrinfo.money:.2f}\nLoan amount: ${usrinfo.loan:.2f}\nHow much would you like to borrow? $"))
            if amount > 0:
                if usrinfo.take_loan(amount):
                    print(f"Successfully borrowed ${amount:.2f}!")
                else:
                    print("You need $1000 in your account and no existing loans to qualify!")
            break
        except ValueError:
            print("Please enter a valid number!")
    
    input("\nPress Enter to continue...")

def process_payment():
    print("\033c")
    usrinfo.apply_interest()  # Check and apply interest if needed
    
    while True:
        try:
            amount = int(input(f"\nYour money: ${usrinfo.money:.2f}\nLoan amount: ${usrinfo.loan:.2f}\nHow much would you like to pay? $"))
            if amount > 0:
                if usrinfo.pay_loan(amount):
                    print(f"Successfully paid ${amount:.2f}!")
                else:
                    print("Invalid payment amount!")
            break
        except ValueError:
            print("Please enter a valid number!")
    
    input("\nPress Enter to continue...")
