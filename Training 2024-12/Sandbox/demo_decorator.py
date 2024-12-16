import time
from datetime import datetime

def my_decororator(f):
    def wrapper(*args, **kwargs):
        print('Before the decorated function')
        return_value = f(*args, **kwargs)
        print('After the decorated function')
        return return_value

    return wrapper


def cache(f):
    result_cache = dict()
    def wrapper(*args):
        if args in result_cache:
            return_value, t_expire = result_cache[args]
            if time.time() < t_expire:
                return return_value

        return_value = f(*args)
        result_cache[args] = return_value, (time.time() + 5)
        return return_value

    return wrapper


# -	a timestamp when the function was called
# -	the name of the function that was called
# -	the arguments and the values of the arguments of the call
# -	the time it took to execute the function
# -	the return value
def debug(f):
    def wrapper(*args, **kwargs):
        timestamp = datetime.now()
        t0 = time.time_ns()
        return_value = f(*args, **kwargs)
        t1 = time.time_ns()

        print(f"""\
{80 * '-'}
Function: {f.__name__}
Called at: {timestamp.strftime('%c')}
Positional arguments: {args}
Keyword arguments: {kwargs}
Return value: {return_value}
Time elapsed: {t1 - t0}ns
{80 * '-'}""")

        return return_value

    return wrapper


@debug
def some_function(a, b, c=1, d=1):
    print(a, b, c, d)
    return a * b * c * d





def repeater(f):
    def wrapper(*args, **kwargs):
        n = 5
        for _ in range(n):
            f(*args, **kwargs)

    return wrapper



@cache
def do_calculation(a, b, c):
    time.sleep(2)
    return (a + b) * c




@repeater
def say_hi(name):
    print("Hello " + name)


# t0 = time.time()
# print(f'Starting')
#
# print( do_calculation(23, 45, 67) )
# print( do_calculation(23, 45, 67) )
# print( do_calculation(23, 45, 67) )
# print( do_calculation(23, 45, 67) )
# print( do_calculation(23, 45, 67) )
# print( do_calculation(23, 45, 67) )
#
# print('Sleeping')
# time.sleep(5)
# print('Done sleeping')

# print( do_calculation(23, 45, 67) )
# print( do_calculation(23, 45, 67) )
# print( do_calculation(23, 45, 67) )
#
# t1 = time.time()
# duration = t1 - t0
# print(f'Done in {duration}s')


print( some_function(2, 3, c=1, d=1) )
print( some_function(8, 2, 3, d=10) )