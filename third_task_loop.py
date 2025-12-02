#Question 1: Print numbers from 1 to 10 using a for loop Code:
for i in range(1, 11):
    print(i)
# Output:1 2 3 4 5 6 7 8 9 10


#Question 2: Print all even numbers from 1 to 20 Code:
for i in range(2, 21, 2):
    print(i)
#Output: 2 4 6 8 10 12 14 16 18 20



# Question 3: Print each character of the string 'Python' Code:
for ch in "Python":
    print(ch)

#Output:
    """
    P
    y
    t
    h
    o
    n
    """


# Question 4: Using a while loop, print numbers from 5 down to 1 Code:
i = 5
while i >= 1:
    print(i)
    i -= 1

#Output: 5 4 3 2 1



#Question 5: Find the sum of numbers from 1 to 50 Code:
s = 0
for i in range(1, 51):
    s += i
print(s)

# Output: 1275



#Question 6: Print the multiplication table of 5 (5×1 to 5×10) Code:
for i in range(1, 11):
    print(5, "x", i, "=", 5*i)

# Output:
"""
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
"""


# Question 7: Count how many vowels are present in 'Programming' Code:
# Method 1
vowels = "aeiou"
count = 0
for ch in "Programming":
    if ch.lower() in vowels:
        count += 1
print(count)


# Method 2
count = 0
for ch in "Programming":
    ch = ch.lower()
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count += 1

print(count)

# Output: 3



# Question 8: Reverse the string 'PythonLoops' Code:
s = "PythonLoops"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

# Output: spooLnohtyP



# Question 9: Print numbers 1–10 but skip 5 using continue Code:
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Output: 1 2 3 4 6 7 8 9 10



# Question 10: Stop loop when number reaches 13 Code:
for i in range(1, 21):
    if i == 13:
        break
    print(i)

# Output: 1 2 3 4 5 6 7 8 9 10 11 12



# uestion 11: Check if a number is prime Code:
n = 17
flag = True

for i in range(2, n):
    if n % i == 0:
        flag = False
        break

print("Prime" if flag else "Not Prime")

# Output: Prime



# Question 12: Count how many times each character occurs in 'mississippi' Code:
s = "mississippi"
count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

print(count)

#Output: {'m': 1, 'i': 4, 's': 4, 'p': 2}



# Question 13: Print pattern *, **, ***, ****, ***** Code:
for i in range(1, 6):
    print('*' * i)

# Output:
"""
*
**
***
****
*****
"""


# Question 14: Find the largest digit in 5847361 Code:
n = "5847361"
print(max(n))

# Output: 8


# Question 15: Print pattern *****, ****, ***, **, * Code:
for i in range(5, 0, -1):
    print('*' * i)

# Output:
"""
*****
****
***
**
*
"""
