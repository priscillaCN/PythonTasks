"""Keep asking the user to enter a positive number.
 Stop and print it when they enter a number greater than 0."""
 
number = int(input('Enter a number: '))
 
while (number <= 0):
    number = int(input('Enter a number: '))
     
print('You entered', number)