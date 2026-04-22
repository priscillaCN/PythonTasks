"""Keep reading integers from the user.
When they enter 0, stop and print the total of all entered numbers."""

number = 1
sum = 0

while(number != 0):
    number = int(input('Enter a number: '))
    
    if (number == 0):
        break
        
    sum = sum + number
    
print('Total:', sum)