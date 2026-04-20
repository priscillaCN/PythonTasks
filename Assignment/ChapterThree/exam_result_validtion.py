"""A program that validates exam results"""

grade_counter = 0


result_value = int(input('Enter result (1 = pass, 2 = fail): ')) 

while (result_value != 1) and (result_value != 2):
    result_value = int(input('Enter result (1 = pass, 2 = fail): ')) 

    for result_value in range (10):
        if result_value == 1:
            grade_counter += 1
 
print('failed: ', 10 - grade_counter)


