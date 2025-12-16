
#1.Print text

print("Hello SkillGapAI")
#Output : Hello SkillGapAI





# 2. Assign a variable
name = "Your Name"
print(name)
#Output : Your Name






#3. Multiple variables
age = 25
city = "Chennai"
skill = "Python"

print(age, city, skill)


#Output: 25 Chennai Python







#4. Type conversion
value = str(100)
print(type(value))


#Output : <class 'str'>





#5. Uppercase string

text = "python basics"
print(text.upper())


#Output: PYTHON BASICS







#6. Length of string

print(len("SkillGapAI"))


#Output : 10





#7. List indexing

colors = ["red", "blue", "green"]
print(colors[1])


#Output : blue





#8. Append to list

fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)


#Output: ['apple', 'banana', 'orange']






#9. Remove from list

items = ["apple", "banana", "orange"]
items.remove("banana")
print(items)


#Output: ['apple', 'orange']







#10. List to tuple
nums = [1, 2, 3]
t = tuple(nums)
print(t)


# Output : (1, 2, 3)








#11. Dictionary

resume = {
    "name": "John",
    "age": 25,
    "skills": ["Python", "SQL"]
}
print(resume)


#Output : {'name': 'John', 'age': 25, 'skills': ['Python', 'SQL']}






#12. Access dictionary value

print(resume["skills"])


#Output : ['Python', 'SQL']






#13. Conditional expression

marks = 50
print("Pass" if marks > 40 else "Fail")


#Output : Pass







#14. Even or Odd

num = 7
print("Even" if num % 2 == 0 else "Odd")


#Output : Odd







#15. For loop

for i in range(1, 11):
    print(i)


#Output
'''
1
2
3
4
5
6
7
8
9
10
'''








#16. While loop


i = 5
while i >= 1:
    print(i)
    i -= 1


#Output
'''
5
4
3
2
1
'''






#17. Function (no return)

def say_hello():
    print("Hello")

say_hello()


#Output : Hello







#18. Function with return

def add(a, b):
    return a + b

print(add(5, 3))


#Output : 8







#19. Import module

import math
print(math.pi)


#Output : 3.141592653589793






#20. Create virtual environment

#Command

#python -m venv myenv


#Output : (no output if successful)
