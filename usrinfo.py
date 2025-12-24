
import json
import time

DEFAULT_DATA = {
    "uname": "player1",
    "money": 1000,
    "chips": 0,
    "loan": 0,
    "loan_date": 0,
    "show_probability": False,
    "show_strategy": False
}

def load_data():
    try:
        with open('userdata.json', 'r') as f:
            return json.load(f)
    except:
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA

def save_data(data):
    with open('userdata.json', 'w') as f:
        json.dump(data, f)

data = load_data()
uname = data["uname"]
money = data["money"]
chips = data["chips"]
loan = data["loan"]
loan_date = data["loan_date"]
show_probability = data.get("show_probability", False)
show_strategy = data.get("show_strategy", False)

def toggle_strategy():
    global show_strategy
    show_strategy = not show_strategy
    save_data({"uname": uname, "money": money, "chips": chips, "loan": loan, "loan_date": loan_date, "show_probability": show_probability, "show_strategy": show_strategy})
    return show_strategy

def toggle_probability():
    global show_probability
    show_probability = not show_probability
    save_data({"uname": uname, "money": money, "chips": chips, "loan": loan, "loan_date": loan_date, "show_probability": show_probability})
    return show_probability

def buy_chips(amount):
    global money, chips
    if amount <= money:
        money -= amount
        chips += amount
        save_data({"uname": uname, "money": money, "chips": chips, "loan": loan, "loan_date": loan_date})
        return True
    return False

def sell_chips(amount):
    global money, chips
    if amount <= chips:
        chips -= amount
        money += amount
        save_data({"uname": uname, "money": money, "chips": chips, "loan": loan, "loan_date": loan_date})
        return True
    return False

def take_loan(amount):
    global money, loan, loan_date
    if money >= 1000 and loan == 0:
        money += amount
        loan = amount
        loan_date = time.time()
        save_data({"uname": uname, "money": money, "chips": chips, "loan": loan, "loan_date": loan_date})
        return True
    return False

def pay_loan(amount):
    global money, loan
    if amount <= money and amount <= loan:
        money -= amount
        loan -= amount
        save_data({"uname": uname, "money": money, "chips": chips, "loan": loan, "loan_date": loan_date})
        return True
    return False

def apply_interest():
    global loan, loan_date
    if loan > 0:
        days_passed = (time.time() - loan_date) / (30 * 24 * 60 * 60)  # Convert to months
        if days_passed >= 1:
            loan = loan * (1 + 0.015)  # 1.5% interest
            loan_date = time.time()  # Reset loan date after applying interest
            save_data({"uname": uname, "money": money, "chips": chips, "loan": loan, "loan_date": loan_date})
