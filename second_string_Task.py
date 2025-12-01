1 #Extract the first 3 characters of: text = 'Python' code:
text = 'Python'
print(text[:3])
# Output: Pyt

2  #Convert to lowercase: name = 'hello WORLD' code:
name = 'hello WORLD'
print(name.lower())
#Output: hello world

3 #Remove extra spaces: msg = ' Welcome to Python ' code:
msg = ' Welcome to Python '
print(msg.strip())
#Output: Welcome to Python

4 #Find the length of: word = 'Programming' code:
word = 'Programming'
print(len(word))
#Output: 11

5 #Split based on comma: text = 'apple,banana,grape' code:
text = 'apple,banana,grape'
print(text.split(','))
# Output: ['apple', 'banana', 'grape']

6  #Replace 'Java' with 'Python' in: text = 'I love Java' code:
text = 'I love Java'
print(text.replace('Java', 'Python'))
#Output: I love Python

7 #Extract 'Science' from: line = 'Data Science' code:
line = 'Data Science'
print(line.split()[1])
# Output: Science

8 #Get the last character of: text = 'Python' code:
text = 'Python'
print(text[-1])
# Output: n

9#Check if 'Python' is present in: sentence = 'Learning Python is fun' code:
sentence = 'Learning Python is fun'
print('Python' in sentence)
#Output: True

10#Join list into a sentence: words = ['Python', 'is', 'easy'] code:
words = ['Python', 'is', 'easy']
print(' '.join(words))
#Output: Python is easy




11 #Extract 'Programming' from: text = 'PythonProgramming' using slicing only code:
text = 'PythonProgramming'
start = len('Python')
end = start + len('Programming')
print(text[start:end])
#Output: Programming

12 #Count how many times 'Hello' appears in: s = 'Hello, Python, Hello, World'code:
s = 'Hello, Python, Hello, World'
print(s.count('Hello'))
#Output: 2

13 #Reverse the string without using reverse(): word = 'Development' code:
word = 'Development'
print(word[::-1])
#Output: tnempoleveD

14 #Replace 'awesome' with 'powerful' only if 'Python' exists in: sentence = 'Python is awesome'code:
sentence = 'Python is awesome'
if 'Python' in sentence:
    sentence = sentence.replace('awesome', 'powerful')
print(sentence)
#Output: Python is powerful

15 #Count occurrences of 'aaa' (including overlapping) in: text = 'aaabbbcccaaa' code:
text = 'aaabbbcccaaa'
pattern = 'aaa'
count = sum(1 for i in range(len(text)-len(pattern)+1) if text[i:i+len(pattern)]==pattern)
print(count)
#Output: 2

16 #Extract username and domain from: email = 'username@example.com'code:
email = 'username@example.com'
username, domain = email.split('@')
print(username, domain)
#Output: username example.com

17 #Extract the numeric value from: line = 'The price is 1500 rupees' code:
# Method 1
line = "The price is 1500 rupees"
num = ""
found = False

for ch in line:
    if ch.isdigit():
        num += ch
        found = True
    else:
        if found:   # stop when number ends
            break

print(num)


# Method 2
import re
line = 'The price is 1500 rupees'
nums = re.findall(r'\d+', line)
num = nums[0] if nums else ''
print(num)
# Output: 1500

18 #Split by '-' and rejoin with spaces: words = 'python-is-simple-and-powerful'code:
words = 'python-is-simple-and-powerful'
parts = words.split('-')
print(' '.join(parts))
# Output: python is simple and powerful

19 # Remove numbers and keep only letters from: text = 'Hello123World45Python' code:
# Method 1
text = "Hello123World45Python"
letters_only = ""

for ch in text:
    if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
        letters_only += ch

print(letters_only)

# Method 2
import re
text = 'Hello123World45Python'
letters_only = re.sub(r'[^A-Za-z]', '', text)
print(letters_only)
# Output: HelloWorldPython

20 # Find the first character that appears more than once in: text = 'Mississippi'(code finds the earliest character whose total count > 1)code:
text = 'Mississippi'
for ch in text:
    if text.count(ch) > 1:
        print(ch)
        break
#Output: i
