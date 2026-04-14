"""A program that calculates simple interest"""

principal = input(int('Enter principal value: '))
rate = input(int('Enter rate value: '))
time = input(int('Enter number of years: '))

simpleinterest = (principal * rate * time) / 100
print(simpleinterest)

amount = principal + simpleinterest
print(amount)
