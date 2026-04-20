"""print ('     1  2  3  4  5  6  7  8  9', end = ' ')
print( )
print( '-------------------------------', end = ' ')
print( )"""
for number in range (1, 10):
    print(number, end = ' ')
    print('--', end = '')
print( )
    
for number in range (1, 10):
    print(number, ' |', end = '   ')
    for count in range (1, 10):
        print(number * count, end = '   ')
    print( )
    