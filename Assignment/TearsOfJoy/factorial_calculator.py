"""Calculate the factorial of a number n entered by the user using a while loop."""

number = int(input('Enter a number: '))

count = 0
factorial = 1

while (count < number):
    count += 1
    factorial = factorial * count
    
print('factorial:', factorial)
    