def maximum_number(number_one, number_two, number_three):
    
    largest_number = number_one
    
    if(number_two > largest_number):
        largest_number = number_two
        
    if(number_three > largest_number):
        largest_number = number_three
    
        return largest_number
        
       
number_one = int(input('Enter first number: '))

number_two = int(input('Enter second number: '))

number_three = int(input('Enter third number: '))

max = maximum_number(number_one, number_two, number_three)

print('the maximum number is', max)
