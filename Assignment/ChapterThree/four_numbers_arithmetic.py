counter = 0
sum = 0
multiply = 1

for counter in range (1,5):
    number = int(input('Enter number: '))
    sum += number
    multiply *= number
    average = sum / counter
    
print('The sum is ', sum, '\nThe product is ',multiply, '\nThe average is ', average)
    
