import os
from typing import List

def calculate(x: int | float,
              y: int | float,
              z: int | float = 1) -> int | float:

    if any([not isinstance(x, (int, float)),
            not isinstance(y, (int, float)),
            not isinstance(z, (int, float))]):
        raise TypeError('Invalid argument type')

    try:
        result = (x + y) * z
    except Exception as ex:
        print('Error in calculation!', ex)

    return result


def minmax1(numbers):
    return min(numbers), max(numbers)

def minmax2(*args, **kwargs):
    return min(args), max(args)

def print_arguments(x, *args, prefix, **kwargs):
    print(x)
    print(args)
    print(prefix)
    print(kwargs)


# ---------------------------------------------------------------------

if __name__ == '__main__':

    print(calculate(23, 42, 5))
    print(calculate(23, 42, 2.5))
    print(calculate(23, 42))

    # print(float(calculate(4, 5, '1')))

    print(minmax1([23, 67, 34, 76 ,8, 23, 12]))
    print(minmax2(23, 67, 34, 76 ,8, 23, 12))

    print_arguments(23, 42, 'abc', factor=7, prefix='qq_')


    # filename = 'xxx.txt'
    #
    # if os.path.exists(filename):
    #     f = open(filename)
    #     f.close()
    # else:
    #     print(f'"{filename}" does not exist')
    #
    # try:
    #     f = open(filename)
    #     f.close()
    # except FileNotFoundError:
    #     print(f'"{filename}" does not exist')