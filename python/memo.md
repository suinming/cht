# import the module

```python
# method 1
import module_name
# method 2
from module_name import thing_in_module1, thing_in_module2
# method 3 import all things in the module
from module_name import *
# method module name alias
import module_name as alias
```

=======================================================================

# class inheritence

```python
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        # inherit the attribute from Animal class
        super().__init__()
        # new attribute in Fish class
        self.tail_length = 10

    def breathe(self):
        # inherit the behavior in Animal class
        super().breathe()
        # some adjustment in Fish class
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()
print(nemo.tail_length)
```

=======================================================================

# list comprehension

```python
# pure list comprehension
# square the numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
# it will print out:
# 1, 1, 4, 9, 25, 64, 169, 441, . .

# list comprehension and if statement combine
# fileter the even number and square the numbers
squared_numbers = [num * num for num in numbers if num % 2 == 0]
```

=======================================================================

# dictionary comprehension

```python
student_score = {
  "frank": 100,
  "tom": 50,
  "jack": 33,
  "angela": 98
}

pass_students = {student: score for (student, score) in student_score.items() if score > 60}

print(pass_students)
```

=======================================================================

# iterate over rows in pandas dataframe

```python
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    print(row.student, row.score)
    pass
```

=======================================================================

# many positional arguments

```python
# the args is the tuple
def add(*args):
  sum = 0
  for num in args:
    sum += num
  return sum

print(add(1, 2, 3))
```

=======================================================================

# many keyword arguments

```python
# the kwargs is the dictionary
def calculate(n, **kwargs):
  n += kwargs["add"]
  n *= kwargs["multiply"]
  return n

print(calculate(5, add=2, multiply=10))
```

=======================================================================

# get the value from the dictionary by using get function

```python
dict = {"a": 1, "b":2}
# get the existing key "a" in the dictionary
print(dict.get("a")) # 1
# get the non-existing key "c" in the dictinary
print(dict.get("c")) # None
```

=======================================================================

# error handling

```python
try:
    # do something that might trigger error
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    # if there is FileNotFoundError execute this block
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    # if there is KeyError execute this block
    print(f"The key {error_message} does not exist.")
else:
    # if there is no error execute this block
    content = file.read()
    print(content)
finally:
    # do this block no matter there is error or not
    raise TypeError("This is an error that I made up.")
```

=======================================================================

# api request

1. get request

```python
import requests as req
url_params = {
    "params_1": "1",
    "params_2": "2",
}
res = req.get("your url", params=url_params)
res.raise_for_status()
data = res.json()
print(data)
```

2. post request

```python
body ={
    "id": GRAPH_ID,
    "name":"Coding Graph",
    "unit":"commit",
    "type":"int",
    "color":"sora"
}

headers = {
    "X-USER-TOKEN": API_TOKEN
}
res = requests.post(f"{BASE_URL}/users/{USER_NAME}/graphs", json=body, headers=headers)
print(res.text) # check if the post request is success
```

=======================================================================

# SMTP email service

```python
import smtplib
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    my_email = "0223314338aa@gmail.com"
    pw = "qgog rxmx ojdp ojlp "
    to_addrs = "n86094275@gs.ncku.edu.tw"
    connection.login(user=my_email, password=pw)
    connection.sendmail(from_addr=my_email, to_addrs=to_addrs, msg=f"Subject:This is the subject\n\n{final_letter}")
```

=======================================================================

# type hint and arrow

there are four kind of types:

1. int
2. str
3. float
4. bool

```python
age: int
age = 14
is_human: bool
is_human = True
```

using the type hint and arrow in function:

```python
def police_check(age: int) ->bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive
```

=======================================================================

#

=======================================================================

#

=======================================================================

#

=======================================================================

#

=======================================================================

#

=======================================================================

#

=======================================================================

#

=======================================================================
