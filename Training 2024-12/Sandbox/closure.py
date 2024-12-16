def make_counter():
    count = 0 # Enclosing variable
    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter = make_counter()

print( counter() )
print( counter() )
print( counter() )