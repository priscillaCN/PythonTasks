"""A program that evaluates the strength of a user's password"""

"""
1. create a password variable
2. use the len keyword to declare input
3. prompt user to enter password
4. if password length is less than 8, print very weak
5. else if password length is 8, print weak
6. else if password is between 8 and 16, print strong
7. else, print very strong  
"""

password = len(input('Enter your password: '))

if (password < 8):
    print('very weak')

elif (password == 8):
    print('weak')

elif (password <= 16):
    print('strong')

else:
    print('very strong')