
import usrinfo
import time

def get_statement():
    days_with_loan = 0
    if usrinfo.loan > 0:
        days_with_loan = int((time.time() - usrinfo.loan_date) / (24 * 60 * 60))
    
    return f"""
=== BANK STATEMENT ===
Account Holder: {usrinfo.uname}
Current Balance: ${usrinfo.money:.2f}
Chips: {usrinfo.chips}
Outstanding Loan: ${usrinfo.loan:.2f}
Days with Loan: {days_with_loan}
Interest Rate: 1.5% monthly
==================
"""
