"""A program that appiles tiered discounts to customers' total spending"""


"""
1. ask user to enter their total spending
2. if purchases are between 1000 and 10000,
   discount = (price / 100) * 5
"""

total_spending = int (input('Enter your total spending: '))

if total_spending < 1000:
    print ('no discount')

elif total_spending <= 10000:
    discount = (total_spending / 100) * 5
    new_price = total_spending - discount
    print ('you receive a 5% discount! Your new price is', new_price)

elif total_spending <= 50000:
    discount = (total_spending / 100) * 10
    new_price = total_spending - discount
    print ('you receive a 10% discount! Your new price is', new_price)

else:
    discount = (total_spending / 100) * 20
    new_price = total_spending - discount
    print ('you receive a 20% discount! Your new price is', new_price)
