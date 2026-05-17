def dollar_to_naira(amount_in_dollar):
    naira_equivalent = float(amount_in_dollar * 1550)
        return naira_equivalent
        
        
amount_in_dollar = int(input('Enter an amount in dollar: '))
convert_to_naira = dollar_to_naira(amount_in_dollar)
print(convert_to_naira, 'Naira')
