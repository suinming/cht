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
# the args is the tuple => (arg1, arg2, arg3, ...)
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

# web scraping BeautifulSoup template

```python
import requests as req
from bs4 import BeautifulSoup
import lxml

# get the html
website_url = "url ..."
res = req.get(website_url, headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
                                    "Accept-Language":"en-US,en;q=0.5"}).text
print(res.prettify())

# get the target content you want by using BeautifulSoup
# the first arg in BeautifulSoup is the response html text
# the second arg in BeautifulSoup is the parser
# the parser can be html.parser or lxml(need to install)
soup = BeautifulSoup(res, 'lxml')
# METHOD-1: use find method to select the target content
price = soup.find(class_="a-offscreen").get_text()

# METHOD-2: use css selector to select the target content
price = soup.css.select(".a-offscreen")[0].get_text()

```

=======================================================================

# web scraping selenium template

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class Bot:

    def __init__(self):
        # keep the chrome driver open after the program finish
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        # incognito mode
        chrome_options.add_argument("--incognito")
        # set up the driver for chrome browser
        self.driver = webdriver.Chrome(options=chrome_options)

    def your_fn(self):
        self.driver.find_element(By.ID, "css id")
        self.driver.find_element(By.CLASS_NAME, "css class")
        self.driver.find_element(By.XPATH, "xpath")

```

=======================================================================

# decorator function

- concept:
  decorator function是function，用function作為input argument裝飾input
  function，並回傳調整後的function作為return，使得重複的邏輯得以重複使用。

```python
def logging_decorator(fn):
  def wrapper(*args):
    print(f"You called {fn.__name__}({args[0]}, {args[1]}, {args[2]})")
    print(f"It returned: {fn(args[0],args[1], args[2])}")
  return wrapper

@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(1, 2, 3)
# You called a_function(1, 2, 3)
# It returned: 6
```

=======================================================================

# setup flask app

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>This is the root route</h1>"


# you can get the query variable in the url
@app.route("/<int:random_number>")
def root(random_number):
    num = random_number + 2
    return num

# start the flask app and open the debug mode
if __name__ == "__main__":
    app.run(debug=True)
```

=======================================================================

# render html and css file in flask server

## the structure of the file

You have to create two folders due to flask Doc,
first one is **templates folder** which holds the html file
second one is **static folder** which holds images or css files

- static
  - images
    - image-1.png
  - css
    - style.css
- templates
  - index.html

```python
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def root():
    # render the index.html file in the templates folder
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
```

=======================================================================

# jinja template

```python
# the input of the html file is posts
post = [
    {
        "id": 1
        "title": "title-1",
        "subtitle": "subtitle-1",
        "body": "body-1",
    },
    {
        "id": 2
        "title": "title-2",
        "subtitle": "subtitle-2",
        "body": "body-2",
    },
]

# index.html
    {% for post in posts %}
        <div class="content">
            <div class="card">
                <h2>{{ post["title"] }}</h2>
                <p class="text">{{ post["subtitle"] }}</p>
                # you can use the url_for function to different route
                # you can also send the keyword arguments in url_for
                <a href="{{ url_for('blog', id = post['id'] - 1) }}">Read</a>
            </div>
        </div>
    {% endfor %}
```

=======================================================================

# python requirement file to manage package

[requirement file explain](https://docs.google.com/document/d/e/2PACX-1vRIW_TuZ6z0ASjAoxgJgmzjGYLCDx019tKvphaTwK_Za7fnMKywUuXI0-s5wr0nQI_gprm6J6y7L9rL/pub)

=======================================================================

# flask wtForm with bootstrap

day61
有完整的範例(projectName wtForm in Pycharm dir)如何用wtForm完成表單與表單驗證，並配合bootstrap讓程式簡潔界面漂亮

=======================================================================

# access index in for loop in jinja template

- use loop.index0 to access the current index value in for loop

```python
	  <table class="table table-dark table-striped table-hover">
          {% for cafe in cafes %}
              {% if loop.index0 == 0 %}
                  <thead>
                    <tr>
                        {% for col in cafe %}
                            <th colspan="2">{{ col }}</th>
                        {% endfor %}
                    </tr>
                  </thead>
              {% else %}
                  <tbody>
                    <tr>
                        {% for col in cafe %}
                            <th colspan="2">{{ col }}</th>
                        {% endfor %}
                    </tr>
                  </tbody>
              {% endif %}
          {% endfor %}
  	  </table>
```

=======================================================================
