"""A program that gives user a simple diagnosis"""

user_problem = input('What is your problem?\n')

question = input('Have you had this problem before? (yes or no)\n')

if question == 'yes':
    print('well, you have it again.')

if question == 'no':
    print('well, you have it now.')


"""
this conversation will not convince the user that the entity at the other end exhibited intelligent behaviour because the inquiry lack empathy and rational conclusion.
"""