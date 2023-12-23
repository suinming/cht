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
  **常常和functools中的wrap一起使用**

```python
from functools import wraps
from flask import abort

# ex1
def logging_decorator(fn):
  def wrapper(*args, **kwargs):
    print(f"You called {fn.__name__}({args[0]}, {args[1]}, {args[2]})")
    print(f"It returned: {fn(args[0],args[1], args[2])}")
  return wrapper

@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(1, 2, 3)
# You called a_function(1, 2, 3)
# It returned: 6

# ex2
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id == 1:
            return f(*args, **kwargs)
        return abort(403)
    return decorated_function
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
def query(random_number):
    num = random_number + 2
    return num

# you can get the params in the url
# i.e. /search?num=5
@app.route("/search")
def parmas():
    num = request.args.get('num')
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

# determine empty list in jinja html template

```python
{% if books == []: %}
<p>Library is empty.</p>
```

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

# sqlite3 in python

```python

import sqlite3

# init sqlite db file and cursor
db = sqlite3.connect("books-collections.db")
cursor = db.cursor()

# create a table called books in db
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# insert value to books table
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
```

=======================================================================

# sqlite3 with SQLAlchemy

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy()
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
```

=======================================================================

# CRUD in SQLAlchemy

```python
## 1. Create a new record
# create a new record
    with app.app_context():
        new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
        db.session.add(new_book)
        db.session.commit()

# create a new record from form data
    with app.app_context():
        new_book = Book(title=request.form.get("title"), author=request.form.get("author"), rating=request.form.get("rating"))
        db.session.add(new_book)
        db.session.commit()

###################################

## 2. Read record/records
# read all records
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars()
# read a single record
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title).where(Books.title == "Harry Potter"))
        book = result.scalar()

###################################

## 3. Update a record
# update by query
    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
        book_to_update.title = "Harry Potter and the Chamber of Secrets"
        db.session.commit()
# update by id
    book_id = 1
    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_update = db.get_or_404(Book, book_id)
        book_to_update.title = "Harry Potter and the Goblet of Fire"
        db.session.commit()

###################################

## 4. Delete a record
    book_id = 1
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
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
