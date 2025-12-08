# MINI PROJECT : PYTHON PRACTICAL EXAMPLES
# Internship : Infosys


# --------------------------------------------------
# EXAMPLE 1 : FOR LOOP
# --------------------------------------------------
for i in range(1, 4):
    print(i)
# Output: 1 2 3


# --------------------------------------------------
# EXAMPLE 2 : WHILE LOOP
# --------------------------------------------------
x = 1
while x <= 3:
    print(x)
    x += 1
# Output: 1 2 3


# --------------------------------------------------
# EXAMPLE 3 : BREAK
# --------------------------------------------------
for i in range(1, 6):
    if i == 4:
        break
    print(i)
# Output: 1 2 3


# --------------------------------------------------
# EXAMPLE 4 : CONTINUE
# --------------------------------------------------
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Output: 1 2 4 5


# --------------------------------------------------
# EXAMPLE 5 : PASS
# --------------------------------------------------
for i in range(1, 4):
    if i == 2:
        pass
    print(i)
# Output: 1 2 3


# --------------------------------------------------
# EXAMPLE 6 : FUNCTION (No parameter)
# --------------------------------------------------
def greet():
    return "Hello Infosys"

print(greet())
# Output: Hello Infosys


# --------------------------------------------------
# EXAMPLE 7 : FUNCTION (With parameter & return)
# --------------------------------------------------
def multiply(a, b):
    return a * b

print(multiply(4, 5))
# Output: 20


# --------------------------------------------------
# EXAMPLE 8 : FUNCTION with *args
# --------------------------------------------------
def add_numbers(*nums):
    return sum(nums)

print(add_numbers(1, 2, 3))
# Output: 6


# --------------------------------------------------
# EXAMPLE 9 : FUNCTION with **kwargs
# --------------------------------------------------
def show_details(**data):
    return data

print(show_details(name="Amit", age=22))
# Output: {'name': 'Amit', 'age': 22}


# --------------------------------------------------
# EXAMPLE 10 : LAMBDA FUNCTION
# --------------------------------------------------
cube = lambda x: x ** 3
print(cube(3))
# Output: 27


# --------------------------------------------------
# EXAMPLE 11 : RECURSIVE FUNCTION
# --------------------------------------------------
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(4))
# Output: 24


# --------------------------------------------------
# EXAMPLE 12 : BUILT-IN FUNCTIONS (WITH EXAMPLES)
# --------------------------------------------------
print(len([1,2,3]))          # Output: 3
print(type(10))              # Output: <class 'int'>
print(max(5, 9, 2))          # Output: 9
print(min(5, 9, 2))          # Output: 2
print(sum([1,2,3]))          # Output: 6
print(sorted([3,1,2]))       # Output: [1,2,3]
print(abs(-10))              # Output: 10
print(round(4.6))            # Output: 5
