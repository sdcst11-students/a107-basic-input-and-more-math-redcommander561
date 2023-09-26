'''
##### Task 2 Compound Interest
Ask the user to enter the following:
* The principal (amount invested or borrowed)
* The annual interest rate (expressed as a percent)
* The number of compounding periods per year
* The length of time for the investment
Calculate the final amoutn as well as the amount of interest earned. Round your answer to 2 decimal places

```
https://www.thecalculatorsite.com/articles/finance/compound-interest-formula.php
Enter the Princial: 2000
Enter the annual interest rate as a percent: 4
Enter the number of compounding periods: 4
How long is the investment period in years: 3
Your final amount is $2253.65
You earned $253.65 interest

Enter the Princial: 25000
Enter the annual interest rate as a percent: 7.5
Enter the number of compounding periods: 12
How long is the investment period in years: 6
Your final amount is $39152.94
You earned $14152.94 interest
```
'''
principal = float(input("Enter the Principal: "))
annual_interest_rate = float(input("Enter the annual interest rate as a percent: "))
compounding_periods = int(input("Enter the number of compounding periods: "))
investment_period_years = int(input("How long is the investment period in years: "))


annual_interest_rate_decimal = annual_interest_rate / 100

final_amount = principal * (1 + (annual_interest_rate_decimal / compounding_periods)) ** (compounding_periods * investment_period_years)

interest_earned = final_amount - principal

rounded_final_amount = round(final_amount, 2)
rounded_interest_earned = round(interest_earned, 2)

print(f"Your final amount is ${rounded_final_amount}")
print(f"You earned ${rounded_interest_earned} interest")