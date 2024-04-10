from validator_collection import validators, checkers, errors

email_address = input("What's your email address? ")

if checkers.is_email(email_address) == True:
    print('Valid')
else:
    print('Invalid')