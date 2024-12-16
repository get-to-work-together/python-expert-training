from functools import partial

# Define a function that takes three arguments
def multiply(x, y, z):
    return x * y * z

# Create a partial function with y = 2 and z = 3
partial_multiply = partial(multiply, y=2, z=3)

# Now we only need to pass one argument (x)
result = partial_multiply(4)  # equivalent to multiply(4, 2, 3)

print(result)