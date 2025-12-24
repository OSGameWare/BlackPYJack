
import usrinfo

def buy_chips_menu():
    print("\033c")
    while True:
        try:
            amount = int(input(f"\nYour money: ${usrinfo.money}\nHow many chips would you like to buy? $"))
            if usrinfo.buy_chips(amount):
                print(f"Successfully bought {amount} chips!")
                input("\nPress Enter to continue...")
                return
            else:
                print("Not enough money!")
        except ValueError:
            print("Please enter a valid number!")
