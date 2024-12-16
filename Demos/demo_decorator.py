def my_decorator(f):
    def wrapper(*args, **kwargs):
        # do something
        return_value = f(*args, **kwargs)
        # do something
        return return_value
    return wrapper

@my_decorator
def another_function():
    print('Hello')

another_function()