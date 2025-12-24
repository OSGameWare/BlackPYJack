import time
import cardhints
import instructions
import intro
import introbank
import game
import usrinfo

def main():
    while True:
        time.sleep(1)
        print("\033c")
        print(intro.intxt)

        intinput = input("Please select an option: ").lower()

        if intinput in ["1", "start game"]:
            print("\033c")
            while game.play_game():
                pass
            continue

        elif intinput in ["2", "instructions"]:
            print("\033c")
            print(instructions.text)
            print("\n")
            input("Press Enter to continue...")

        elif intinput in ["3", "card hints"]:
            print("\033c")
            print(cardhints.cardnames)
            print("\n")
            input("Press Enter to continue...")

        elif intinput in ["4", "User Stats"]:
            print("\033c")
            print(usrinfo.uname)
            print(f"Money: ${usrinfo.money}")
            print(f"Chips: {usrinfo.chips}")
            print(f"\nWin probability display: {'Enabled' if usrinfo.show_probability else 'Disabled'}")
            print(f"Strategy advice display: {'Enabled' if usrinfo.show_strategy else 'Disabled'}")
            toggle_prob = input("\nToggle win probability? (y/n): ").lower()
            if toggle_prob == 'y':
                usrinfo.toggle_probability()
                print(f"Win probability display: {'Enabled' if usrinfo.show_probability else 'Disabled'}")
            toggle_strat = input("Toggle strategy advice? (y/n): ").lower()
            if toggle_strat == 'y':
                usrinfo.toggle_strategy()
                print(f"Strategy advice display: {'Enabled' if usrinfo.show_strategy else 'Disabled'}")
            input("Press Enter to continue...")

        elif intinput in ["5", "Buy Chips"]:
            import buy
            buy.buy_chips_menu()

        elif intinput in ["6", "Convert Money"]:
            import convert
            convert.convert_menu()

        elif intinput in ["7", "bank"]:
            while True:
                print("\033c")
                print(introbank.intxt)
                bank_input = input("Please select an option: ").lower()
                
                if bank_input in ["1", "apply for loan"]:
                    import loan
                    loan.process_loan()
                elif bank_input in ["2", "payback loan"]:
                    import loan
                    loan.process_payment()
                elif bank_input in ["3", "bank policy"]:
                    print("\033c")
                    import policy
                    print(policy.bankpolicy)
                    input("\nPress Enter to continue...")
                elif bank_input in ["4", "bank statement"]:
                    print("\033c")
                    import statement
                    print(statement.get_statement())
                    input("\nPress Enter to continue...")
                elif bank_input in ["5", "exit"]:
                    break
                else:
                    print("Invalid input")
                    time.sleep(1)

        elif intinput in ["8", "exit"]:
            print("Thanks for playing!")
            time.sleep(1)
            print("\033c")
            break

        else:
            print("Invalid input")
            time.sleep(1)

if __name__ == "__main__":
    main()