x, y = y, x  # swapping

print(1 > 2 > 3)  # prints False

# filtering (there is also reduce(), map())
numbers = range(50)
evenNumbers = filter(lambda x: x % 2 == 0, numbers)
print("All even numbers in [0; 50): %s"%evenNumbers)

# list comprehensions:
squares = [x**2 for x in numbers]

a += 2  # a = a + 2

print("string" in "Long string")  # prints True
