'''
##### Task 1 Percent Error
Ask the user to input the following:
* the expected number
* the actual result
Calculate the percent difference between the two results. Round your answer to 2 decimal places

```
https://www.skillsyouneed.com/num/percent-change.html

Sample Output:
Enter expected: 10
Enter actual : 9
The percent difference is -10.0%

Enter expected: 12
Enter actual : 14
The percent difference is 16.67%
```
'''
expected = float(input("Enter expected: "))
actual = float(input("Enter actual: "))


percent_difference = ((actual - expected) / expected) * 100

rounded_percent_difference = round(percent_difference, 2)

print(f"The percent difference is {rounded_percent_difference}%")
#You can run this code, and it will ask the user to input the expected and actual values, calculate the percent difference, and display the result rounded to 2 decimal places.





