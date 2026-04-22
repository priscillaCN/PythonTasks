"""Print numbers 1-50. For multiples of 3 print 'Fizz', 
multiples of 5 print 'Buzz', multiples of both print 'FizzBuzz'."""

for number in range (1, 51):
    
    if(number % 3 == 0):
        print(number,'Fizz')
        
    elif(number % 5 == 0):
        print(number, 'Buzz')
        
    elif(number % 3 == 0 and number % 5 == 0):
        print(number, 'FizzBuzz') 
    
    else:
         print(number)
        