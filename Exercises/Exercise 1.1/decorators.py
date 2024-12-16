import time
from datetime import datetime


def debug(func):
    func_name = func.__qualname__

    def wrapper(*args, **kwargs):
        nonlocal func_name

        print(80 * '-')
        print(f'T:', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print(f'Calling: {func_name}')
        print(f'  positional arguments:', args)
        print(f'  keyword arguments:', kwargs)

        t0 = time.time_ns()

        try:
            return_value = func(*args, **kwargs)
            print(f'  return value:', return_value)
        except Exception as ex:
            print(f'  exception raised:', ex)
            raise ex
        finally:
            print(f'T:', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            t1 = time.time_ns()
            duration = t1 - t0
            print(f'duration: {duration}ns')
            print(80 * '-')

        return return_value
    return wrapper


@debug
def f(x, y):
    return x + y


if __name__ == '__main__':
    print( f(3, 4) )
    print( f(3, 'x') )

