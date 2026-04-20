"""Multiplication table of number entered by user"""

"""
prompt user to enter a number
initialise a variable called count
initilalise a multiple variable to take in value of count times number entered by user
use for loop and set range to (1,11)
give count the value of range
give multiple vaiable the value of range times number
print output
"""

number = int(input('Enter any number: '))

count = 0
	
multiple_of_number = 0
		
for range in range (1,11):
			
	count = range
			
	multiple_of_number = range * number
			
	print(number, 'x ', range, ' = ', multiple_of_number)