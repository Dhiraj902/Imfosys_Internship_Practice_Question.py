#CSV PRACTICE QUESTIONS
# Q1 — Create students.csv (3 records)
import csv

rows = [
    ['name','age','grade'],
    ['Ankitha','21','A'],
    ['Dheeraj','23','B'],
    ['Maya','20','A+']
]

with open('students.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Output (students.csv)
'''name,age,grade
Ankitha,21,A
Dheeraj,23,B
Maya,20,A+
'''






# Q2 — Read employees.csv
import csv

with open('employees.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# Output: 
'''
['id', 'name', 'dept']
['1', 'Ramesh', 'Sales']
['2', 'Sita', 'HR']
['3', 'John', 'IT']

'''







# Q3 — Print first column from products.csv
import csv

with open('products.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])

# Output: 

'''
product
Pen
Book
Bag

'''





#Q4 — DictReader print key–value pairs
import csv

with open('dict_sample.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for k,v in row.items():
            print(k,":",v)
        print("---")

#Output:
'''
name : Asha
city : Mumbai
---
name : Vikram
city : Delhi
---
'''








# Q5 — Add new row to marks.csv
import csv

new_row = ['Kiran','English',90]

with open('marks.csv','a',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(new_row)

# Output (marks.csv)
'''
name,subject,marks
Rani,Math,85
Kiran,English,90

'''







#Q6 — Count rows in data.csv (excluding header)
import csv

count = 0
with open('data.csv','r') as f:
    reader = csv.reader(f)
    next(reader)
    for _ in reader:
        count += 1

print(count)

# Output : 2






# Q7 — Total sales = price × quantity

import csv

total = 0

with open('sales.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        t = float(row['price']) * int(row['quantity'])
        print(row['item'], "->", t)
        total += t

print("Total:", total)

# Output: 
'''
Pen -> 30
Book -> 300
Bag -> 700
Total: 1030
'''







# Q8 — Convert list of lists to CSV
import csv

data = [[1,'Raja'],[2,'Sara'],[3,'Mohan']]

with open('id_name.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id','name'])
    writer.writerows(data)

# Output (id_name.csv):
'''
id,name
1,Raja
2,Sara
3,Mohan

'''










# Q9 — Filter rows where age > 30
import csv

with open('people.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['age']) > 30:
            print(row)

# Output:
'''
{'name': 'B', 'age': '35'}
{'name': 'C', 'age': '40'}

'''






# Q10 — Copy source.csv → copy.csv
import shutil

shutil.copy('source.csv','copy.csv')

#Output (copy.csv):
'''
a,b
1,2

'''








# NOW JSON QUESTIONS
#Q1 Convert JSON string → Python Dictionary
import json

s = '{"name": "Alex", "age": 22, "city": "Chennai"}'
d = json.loads(s)
print(d)

# Output :{'name': 'Alex', 'age': 22, 'city': 'Chennai'}




#Q2 — Convert Dictionary → JSON string

import json

d = {'id': 101, 'product': 'Laptop', 'price': 55000}
s = json.dumps(d)
print(s)

#Output :{"id": 101, "product": "Laptop", "price": 55000}





#Q3 — Read JSON file and print key-value pairs
#(Assume data.json contains)
#{"a": 1, "b": 2, "name": "Test"}

import json

with open('data.json','r') as f:
    data = json.load(f)
    for k,v in data.items():
        print(k, ":", v)
#Output :
'''a : 1
b : 2
name : Test
'''






# Q4 — Write dictionary into student.json

import json

student = {'name': 'Mia', 'age': 24, 'grade': 'A'}

with open('student.json','w') as f:
    json.dump(student, f)

print("JSON file created")

# Output :(student.json) {"name": "Mia", "age": 24, "grade": "A"}







#Q5 — Print only department from nested JSON
#{"employee": {"name": "John", "age": 30, "department": "HR"}}

obj = {'employee': {'name': 'John', 'age': 30, 'department': 'HR'}}
print(obj['employee']['department'])

# Output: HR







# Q6 — Update dictionary & convert to JSON Original:
#{'name': 'Raj', 'age': 45}

import json

raj = {'name': 'Raj', 'age': 45}
raj['age'] = 50
print(json.dumps(raj))

# Output: {"name": "Raj", "age": 50}






# Q7 — Read JSON list and print 2nd item JSON:
#["red", "green", "blue"]


import json

s = '["red","green","blue"]'
lst = json.loads(s)
print(lst[1])

# Output :green





# Q8 — Print all user names from list of users JSON:
#{"users":[{"id":1,"name":"Alex"},{"id":2,"name":"Mia"}]}

obj = {'users': [{'id':1,'name':'Alex'}, {'id':2,'name':'Mia'}]}

for user in obj['users']:
    print(user['name'])

# Output: 
'''
    Alex   
    Mia'''






# Q9 — Add new key "country":"India" and convert to JSON JSON:
#{"name":"Sam","age":28}


import json

sam = {'name': 'Sam', 'age': 28}
sam['country'] = 'India'

print(json.dumps(sam))

# Output : {"name": "Sam", "age": 28, "country": "India"}




#  Q10 — Create items.json and print total cost JSON list:
'''[
  {"item": "Pen",  "price": 10},
  {"item": "Book", "price": 50},
  {"item": "Bag",  "price": 700}
]
'''

import json

items = [
    {'item':'Pen','price':10},
    {'item':'Book','price':50},
    {'item':'Bag','price':700}
]

with open('items.json','w') as f:
    json.dump(items, f)

items_loaded = json.load(open('items.json'))
total = sum(i['price'] for i in items_loaded)

print("Total cost:", total)

# Output : Total cost: 760
