# Additional Notes for CS50P Final Chapter

### Sets  

`Set`s are a collection of values where duplicates aren't allowed. Similar to a `list`  

For the example we will use a `list` of `dict`s

```python
students = [{"name": "Hermione", "house": "Gryffindor"},
            {"name": "Harry", "house": "Gryffindor"},
            {"name": "Ron", "house": "Gryffindor"},
            {"name": "Draco", "house": "Slytherin"},
            {"name": "Padma", "house": "Ravenclaw"}
            ]
```

We can create an empty list and fill it with houses if the aren't already inside the list.  
Alternatively we can use the `set` datatype.  

```python
# Using list()
houses = []
for student in students:
    if student['house'] not in houses:
        houses.append(student['house'])
print(sorted(houses))
# Using set()
houses = set()
for student in students:
    houses.add(student['house'])
print(houses)
```

### Global variables

We can read global variables (defined outside of any functions), but can't write to them from within a function.

```python
balance = 0
def main():
    deposit(100)

def deposit(n):
    balance += n

# >>> UnboundLocalError: local variable 'balance' referenced before assignment
```

In order to access this global variable we need to point to it inside the function

```python
def deposit(n):
    global balance
    balance += n
```

**However** inside classes variables can be accessed from within instance/class methods. Which is much safer than allowing functions to access global variables. (We control the rules)

```python
class Account:
    def __init__(self) -> None:
        self._balance = 0
    @property
    def balance(self):
        return self._balance
    def deposit(self, n):
        self._balance += n
    def withdraw(self, n):
        self._balance -= n
x = Account()
x.balance
```

### Constants

It's best practice to use `constants` at the top of your file, so you don't hard-code values in your code.  
Usually named with **uppercase letters**. In python we don't have a constant `keyword` like some other languages  
The same should be done inside a `class`  
These constants can be accessed with `Classname.VARIABLENAME`

### Type Hints 😁

More info in Py [Docs](docs.python.org/3/library/typing.html)  
Very useful feature, which is getting more focus in newer versions of python.  

```python
# Type hints for functions
def fun(n: int, x: bool = True) -> str:
    return '😎' * n

# Type hints for variables
n: int = int(input("Number: "))
string: str = fun(n)
print(string)
```

I use `pylint` extension in VSCode to show me typehints and type hint warnings.

Could use mypy to test your script/program based on typehints. Useful for when your codebase gets large.  
See [mypy Docs](mypy.readthedocs.io)  
Allows us to run `mypy ./myscript.py` in terminal to test for typing errors  

### Docstrings

Very useful for keeping your code functionality clear. Having docstrings also allows added functionality and automatic documentation generation.

```python
'''Info
Args:
    n (int): number of times to multiply emoticon
    x (bool, optional): No use: Defaults to True
Returns:
    str: Multiple emoticons
Raises:
    TypeError: n needs to be a int
'''
```

### argparse library

Parsing arguments from cmdline can get complected if there are multiple arguments 

> Convention to have one dash for single letters:
> `-n`
> Or two dashes for words:
> `--number`

```python
import argparse

# create parser object
parser = argparse.ArgumentParser()
# declare an argument '-n ?'
parser.add_argument('-n')
# Create variable with the arguments specified 
args = parser.parse_args()

for _ in range(int(args.n)):
    print('meow')
```

We can add to this by including help information accessed by running `filename.py -h`  
And also add a **default values** and also **specify type**

```python
import argparse
parser = argparse.ArgumentParser(description="Program description")
parser.add_argument('-n', default=1, help="Number of times to meow", type=int)
...
```

```
python testing.py
>>> meow

python testing.py -n four
>>> testing.py: error: argument -n: invalid int value: 'four'

python testing.py -h
>>> usage: testing.py [-h] [-n N]
>>> Program description
>>> options:
>>>   -n N        Number of times to meow
```

### Unpacking

#### **Unpacking lists**
---

Notice how a `*` unpacks the sequence of the list of coins and passes in each of its individual elements to `total`.

```python
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]
print(total(*coins), "Knuts")
```

#### **Unpacking Dicts**
---

Notice how `**` allows you to unpack a dictionary. When unpacking a dictionary, it provides both the keys and values.

```python
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins), "Knuts")
```
#### **\*args and \*\*kwargs**
---

```python
def myfunc(*args, **kwargs):
    print('Positional:', args)
    print('Named:', kwargs)

myfunc(100, 50, 25)
# >>> Positional: (100, 50, 25)
myfunc(galleons=100, sickles=50, knuts=50)
# >>> Named: {'galleons': 100, 'sickles': 50, 'knuts': 50}
myfunc(1, 0, galleons=100, sickles=50, knuts=50)
# >>> Positional: (1, 0)
# >>> Named: {'galleons': 100, 'sickles': 50, 'knuts': 50}
```
Notice how the named values are provided in the form of a dictionary.


### map



### list comprehension

Create lists very quickly

```python
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]
gryffindors = [ student["name"] for student in students if student["house"] == "Gryffindor" ]
```

### filter

<!-- TODO  -->
<!-- https://cs50.harvard.edu/python/2022/notes/9/#filter -->

### Dictionary comprehension

Create dictionaries very quickly

```python
students = ["Hermione", "Harry", "Ron"]
gryffindors = []
for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})
print(gryffindors)
# Dict comprehension
students = ["Hermione", "Harry", "Ron"]
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
print(gryffindors)
# Or even simpler
students = ["Hermione", "Harry", "Ron"]
gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)
```

### Enumerate



### Generators, iterators, yield


IM HERE:
https://youtu.be/6pgodt1mezg?t=6478
https://cs50.harvard.edu/python/2022/notes/9/#filter