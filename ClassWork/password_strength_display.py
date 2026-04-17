"""A program that evaluates the strength of a user's password"""

"""
1. prompt user to enter a password
2. use the len keyword to declare input
3. if password length is less than 8, print very weak
4. if password length is 8, print weak
5. if password is between 8 and 16, print strong
6. if password length is above 16, print very strong  
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