#Question:1️ :Square root of a number using math.sqrt()
#Use math.sqrt() to find the square root of a number.
import math
num = 25
result = math.sqrt(num)
print(result)
# Output: 5.0




# Question: 2️ :Round 5.67 using math.floor() and math.ceil()
import math
num = 5.67
print(math.floor(num))
print(math.ceil(num))
# Output :
"""  5
     6
"""




#Question:3️: Generate a random number between 1 and 100
import random
print(random.randint(1, 100))
# Output: (example): 42





# Question:4️:Print 5 random integers between 10 and 20
import random
for i in range(5):
    print(random.randint(10, 20))




# Output (example):
'''
12
19
10
15
18
'''




#Question:5️: Print today’s date
import datetime
today = datetime.date.today()
print(today)
# Output (example): 2025-12-08





#Question:6️ : Print current year, month, and day separately
import datetime
today = datetime.date.today()
print(today.year)
print(today.month)
print(today.day)
# Output (example):
'''
2025
12
8
'''




#Question:7️:Print current working directory
import os
print(os.getcwd())
# Output (example): C:\Users\Dheeraj





#Question:8️: List all files in the current directory
import os
print(os.listdir())
#Output (example): ['file1.py', 'data.csv', 'backup']






#Question:9️: Print current Python version
import sys
print(sys.version)
#Output (example): 3.11.5 (main, ...)





#Question:10: Convert JSON string to dictionary
import json
json_data = '{"name": "Dheeraj", "age": 22}'
data = json.loads(json_data)
print(data)
# Output: {'name': 'Dheeraj', 'age': 22}





#Question:1️1️: Compute cos(0), sin(90°), and log(10)
#⚠ Note: Python uses radians
import math
print(math.cos(0))
print(math.sin(math.radians(90)))
print(math.log(10))
# Output:
'''
        1.0
        1.0
        2.302585092994046
        '''




#Question:1️2️: Roll a dice 10 times and store results
import random
results = []
for i in range(10):
    results.append(random.randint(1, 6))
print(results)
# Output (example): [2, 5, 1, 6, 3, 4, 2, 6, 1, 5]




#Question:1️3️ :Days left for next birthday
#(Example: birthday = 20th March)
import datetime
today = datetime.date.today()
birthday = datetime.date(today.year, 3, 20)
if birthday < today:
    birthday = datetime.date(today.year + 1, 3, 20)

days_left = (birthday - today).days
print(days_left)

# Output (example): 102



#Question:1️4️: Add 30 days to a date
import datetime
date = datetime.datetime.strptime("2022-05-15", "%Y-%m-%d")
new_date = date + datetime.timedelta(days=30)
print(new_date.date())

#Output: 2022-06-14

#Question:1️5️: Create a new folder named backup
import os

os.mkdir("backup")
print("Folder created")

#Output: Folder created



#Question:1️6️ :Convert dictionary to JSON
import json
data = {"name": "Dheeraj", "skill": "Python"}
json_data = json.dumps(data)
print(json_data)
#Output: {"name": "Dheeraj", "skill": "Python"}





#Question:1️7️ :Extract all digits from a string using regex
import re

text = "Age is 22 and year is 2025"
digits = re.findall(r"\d+", text)
print(digits)
# Output: ['22', '2025']






#Question:1️8️: Check if string starts with "Hello" using regex
import re
text = "Hello World"
result = re.match(r"Hello", text)
print(bool(result))
#Output: True





#Question:1️9️: Mean, Median, Mode
import statistics
data = [1, 2, 2, 3, 4]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.mode(data))
#Output:
'''
2.4
2
2
'''




#Question:2️0️ : Measure execution time of a loop

import time

start = time.time()

for i in range(1, 1_000_001):
    pass

end = time.time()
print("Time taken:", end - start)


#Output (example): Time taken: 0.04
