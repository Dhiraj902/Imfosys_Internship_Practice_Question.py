# 1. Write a function welcome() that prints “Welcome to Python!”. 
def welcome():
    print("Welcome to Python!")

welcome()
#Output : Welcome to Python!



# 2. Write a function greet(name) that prints “Hello <name>”. 
def greet(name):
    print(f"Hello {name}")

greet("Dheeraj")
#Output :Hello Dheeraj



# 3. Write a function square(n) that returns the square of n. 
def square(n):
    return n * n

print(square(5))
#Output: 25




# 4. Write a function calculator(a, b) that returns the sum, difference & product. 
def calculator(a, b):
    return a + b, a - b, a * b

print(calculator(10, 4))
# Output:  (14, 6, 40)




# 5. Write a function country(name='India') that prints “I am from <name>”. 
def country(name="India"):
    print(f"I am from {name}")

country()
country("USA")
#Output : I am from India ,I am from USA




# 6. Write a function total(*nums) that returns the sum of all numbers. 
def total(*nums):
    return sum(nums)

print(total(10, 20, 30))
#Output : 60


# 7. Write a function student_info(**data) that prints key : value. 
def student_info(**data):
    for key, value in data.items():
        print(f"{key} : {value}")

student_info(name="Rahul", age=20, marks=88)
#Output :
"""
name : Rahul
age : 20
marks : 88
"""




# 8. Write a function count_vowels(text) that returns number of vowels.

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count

print(count_vowels("Programming"))
# Output: 3





# 9. Write a lambda function to return the cube of a number.
cube = lambda n: n ** 3
print(cube(4))
#Output : 64





# 10. Write a function unique_letters(text) that returns unique letters in order.
def unique_letters(text):
    seen = []
    for ch in text:
        if ch not in seen:
            seen.append(ch)
    return "".join(seen)

print(unique_letters("programming"))
# Output : progamin
