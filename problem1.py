#!python3

# Canada Income Tax Calculator part I

'''
It's tax season!  Nobody loves doing taxes, so EVERYONE uses computers to help them.  We will use
Python to determine Federal and Provincial Income Tax.

The Canadian income tax system is a tiered system, which means you pay different percentages of
your income for different parts of your income.
You pay 15% tax on the first 49020 you earn.  If you earn more than this amount, you pay
20.5% on amounts over 49020 that are less than 98040
26% on amounts over 98040 but less than 151978
29% on amounts over 151978 but less than 216511
33% on amounts over 216511

Write a program to calculate the amount of Federal Income Tax for people who earn over 100,000 but less than 150,000

Example:
Enter your income: 125000
Your federal income tax is: 24411.7

'''

income = float(input("Enter your income :"))  


tax_brackets = [
    (49020, 0.15),
    (98040, 0.205),
    (151978, 0.26),
    (216511, 0.29)
]


tax = 0
remaining_income = income

for bracket in tax_brackets:
    bracket_limit, bracket_rate = bracket
    if remaining_income <= 0:
        break
    if remaining_income > bracket_limit:
        taxable_amount = bracket_limit
    else:
        taxable_amount = remaining_income
    tax += taxable_amount * bracket_rate
    remaining_income -= taxable_amount

print(f"Federal Income Tax for an income of ${income:,.2f} is ${tax:,.2f}")
