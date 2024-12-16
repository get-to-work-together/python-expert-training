def make_counter():
    count = 0  # Enclosing variable

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

# Using the closure
counter = make_counter()

print(counter())  # Output: 1
print(counter())  # Output: 2
print(counter())  # Output: 3