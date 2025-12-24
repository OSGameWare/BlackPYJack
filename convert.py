
import usrinfo

def convert_menu():
    print("\033c")
    while True:
        print(f"\nYour chips: {usrinfo.chips}")
        try:
            amount = int(input("How many chips would you like to convert to money? "))
            if usrinfo.sell_chips(amount):
                print(f"Successfully converted {amount} chips to ${amount}!")
                input("\nPress Enter to continue...")
                return
            else:
                print("Invalid amount!")
        except ValueError:
            print("Please enter a valid number!")
