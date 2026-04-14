"""Mortgage Calculator"""

principal = input(int('Enter the princial amount: '))
annualrate = input(int('Enter the annual interest rate: '))
duration = input(int('Enter the duration of loan in years: '))

monthlyrate = annualrate // 100 // 12
numberofmonths = duration * 12

monthlypayment = principal * (monthlyrate * (1 + monthlyrate) ** numberofmonths) // ((1 + monthlyrate)**numberofmonths - 1)

print('Your monthly payment is', monthlypayment)