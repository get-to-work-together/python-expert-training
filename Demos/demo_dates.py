from datetime import datetime
from dateutil.relativedelta import relativedelta

user_input = input('What is your date of birth? [dd-mm-yyyy] : ')

try:
    date_of_birth = datetime.strptime(user_input, '%d-%m-%Y')

except ValueError:
    print('Invalid date')

else:
    delta = relativedelta(datetime.today(), date_of_birth)

    age = delta.years

    print(f'You are {age} years old.')
