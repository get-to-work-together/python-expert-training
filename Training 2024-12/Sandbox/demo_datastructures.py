number_of_cars = 20
numberOfCars = 20

MAX_NUMBER_OF_CARS = 100


class CarTank:
    """This is my demo class"""
    pass


gender = 'V'

gender = gender.replace('v', 'f')

# gender - possible values: v, m
if gender == 'm':
    print('Dear sir ...')

elif gender in ('f', 'v'):
    print('Dear madame ...')

else:
    print('Dear person ...')

match gender.lower():
    case 'm':
        print('Dear sir ...')

    case 'f' | 'v':
        print('Dear madame ...')

    case _:
        print('Dear person ...')


print(help(CarTank))