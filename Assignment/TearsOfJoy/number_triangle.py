"""rint a right-angled triangle of numbers with 5 rows."""
number = 0
for row in range(1, 6):
    
    for line in range(1, 6,):
        number = number + line
        print(number, end = ' ')
        
    print()