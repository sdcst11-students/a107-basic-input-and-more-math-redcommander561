#!python3

"""
Write a program to ask the user to input a length in centimeters. Convert this into feet and inches.  Round your inches to the nearest whole inch.
You will likely need to make use of at least one of the following:
* % modulus
* math.floor()

Sample output:
```
Enter a length in centimeters: 172
172 centimeters is 5 feet and 8 inches

Enter a length in centimeters: 32
32 centimeters is 1 feet and 1 inches
```
"""

import math

length_cm = float(input("enter how many centimeters :"))

length_inches = length_cm * 0.393701


feet = int(length_inches // 12)
remaining_inches = round(length_inches % 12)

print(f"{length_cm} centimeters is approximately {feet} feet and {remaining_inches} inches.")


