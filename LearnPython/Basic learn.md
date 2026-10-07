हो Sachin. खाली मी तुला **Python चा complete roadmap / syllabus — Basic ते Advanced — सर्व major topics आणि प्रत्येक topic ची Definition** देत आहे. हा **Python Developer / Backend Developer / FastAPI / Django / Interview** preparation साठी reference म्हणून वापरू शकतोस.

# 🐍 Python Complete Syllabus
## Basic → Intermediate → Advanced → Backend → Django → FastAPI

---

# PART 1 — Python Fundamentals

## 1. Python

**Definition:**  
Python is a high-level, interpreted, general-purpose programming language.

**मराठी:**  
Python ही high-level, interpreted आणि general-purpose programming language आहे.

**Uses:**
- Web Development
- Backend Development
- REST API
- Automation
- Data Science
- AI/ML
- Testing
- Scripting
- Desktop applications

---

## 2. Programming Language

**Definition:**  
A programming language is a language used to give instructions to a computer.

**मराठी:**  
Computer ला instructions देण्यासाठी वापरली जाणारी language म्हणजे programming language.

---

## 3. High-Level Language

**Definition:**  
A high-level language is designed to be easier for humans to read and write.

Examples:
- Python
- Java
- C#
- JavaScript

---

## 4. Interpreter

**Definition:**  
An interpreter executes program code at runtime.

Python interpreter Python program execute करतो.

---

## 5. Compiler

**Definition:**  
A compiler translates source code into another form, typically machine code or intermediate code, before execution.

---

## 6. Python Interpreter vs Compiler

| Interpreter | Compiler |
|---|---|
| Runtime execution | Usually translates before execution |
| Easier interactive execution | Produces compiled/intermediate output |
| Python uses interpreter-based execution | C/C++ commonly compiled |

---

# PART 2 — Python Installation & Environment

## 7. Python Installation

Python install केल्यानंतर check:

```bash
python --version
```

किंवा:

```bash
py --version
```

---

## 8. Python Interactive Shell

Python command:

```bash
python
```

नंतर:

```python
print("Hello")
```

---

## 9. Python File

Python file extension:

```text
.py
```

Example:

```text
main.py
```

Run:

```bash
python main.py
```

---

## 10. IDE

**Definition:**  
IDE is software that provides tools for writing, running and debugging code.

Examples:
- VS Code
- PyCharm
- Visual Studio

---

## 11. pip

**Definition:**  
`pip` is Python's package installer.

```bash
pip install requests
```

---

## 12. Virtual Environment

**Definition:**  
A virtual environment is an isolated Python environment for project dependencies.

Create:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

---

## 13. requirements.txt

**Definition:**  
A file used to store project dependencies.

Example:

```text
fastapi
uvicorn
requests
mysql-connector-python
```

Install:

```bash
pip install -r requirements.txt
```

---

# PART 3 — Python Syntax

## 14. Syntax

**Definition:**  
Syntax means the rules used to write valid Python code.

Example:

```python
if age >= 18:
    print("Adult")
```

---

## 15. Indentation

**Definition:**  
Indentation means spaces/tabs used to define code blocks.

Python मध्ये indentation अत्यंत important आहे.

```python
if True:
    print("Hello")
```

---

## 16. Comments

**Definition:**  
Comments are non-executable notes written to explain code.

```python
# This is a comment
```

---

## 17. Docstring

**Definition:**  
A docstring is documentation written inside a function, class or module.

```python
def add(a, b):
    """Return sum of two numbers."""
    return a + b
```

---

# PART 4 — Variables

## 18. Variable

**Definition:**  
A variable is a name that refers to a value/object.

```python
name = "Sachin"
age = 24
```

---

## 19. Variable Naming Rules

- Letter किंवा `_` ने start
- Number ने start नाही
- Spaces नाही
- Keywords नाही
- Case-sensitive

Valid:

```python
student_name = "Sachin"
age1 = 24
```

Invalid:

```python
1age = 24
student-name = "Sachin"
```

---

## 20. Constants

Python मध्ये strict constant keyword नाही.

Convention:

```python
PI = 3.14
MAX_USERS = 100
```

---

# PART 5 — Data Types

## 21. Data Type

**Definition:**  
Data type defines the kind of value an object represents.

Python basic types:

```text
int
float
complex
bool
str
list
tuple
set
dict
NoneType
```

---

## 22. Integer

**Definition:**  
Whole numbers are integers.

```python
age = 24
```

---

## 23. Float

**Definition:**  
Numbers containing decimal values.

```python
price = 99.50
```

---

## 24. Complex

```python
x = 10 + 5j
```

---

## 25. Boolean

**Definition:**  
Boolean represents truth values.

```python
True
False
```

---

## 26. String

**Definition:**  
String is a sequence of characters.

```python
name = "Sachin"
```

---

## 27. None

**Definition:**  
`None` represents absence of a value.

```python
result = None
```

---

## 28. `type()`

**Definition:**  
Returns the type of an object.

```python
type(10)
```

---

## 29. `id()`

**Definition:**  
Returns an object's identity value.

```python
x = 10
print(id(x))
```

---

# PART 6 — Type Conversion

## 30. Type Casting

**Definition:**  
Converting one data type into another is called type casting.

```python
int("10")
float("10.5")
str(100)
bool(1)
```

---

## 31. Implicit Conversion

Python automatically converts compatible types in some expressions.

```python
x = 10
y = 2.5

result = x + y
```

Result becomes float.

---

## 32. Explicit Conversion

Developer explicitly converts type.

```python
age = int("24")
```

---

# PART 7 — Input / Output

## 33. `print()`

**Definition:**  
Used to display output.

```python
print("Hello")
```

---

## 34. `input()`

**Definition:**  
Used to receive input from the user.

```python
name = input("Enter name: ")
```

Important:

`input()` normally returns `str`.

---

## 35. f-string

**Definition:**  
A formatted string syntax used to embed expressions inside strings.

```python
name = "Sachin"
age = 24

print(f"{name} is {age} years old")
```

---

# PART 8 — Operators

## 36. Operators

**Definition:**  
Operators are symbols/keywords used to perform operations.

Types:

1. Arithmetic
2. Comparison
3. Assignment
4. Logical
5. Identity
6. Membership
7. Bitwise

---

## 37. Arithmetic Operators

```text
+
-
*
/
//
%
**
```

---

## 38. Comparison Operators

```text
==
!=
>
<
>=
<=
```

Result:

```text
True / False
```

---

## 39. Assignment Operators

```text
=
+=
-=
*=
/=
%=
//=
**=
```

---

## 40. Logical Operators

```text
and
or
not
```

---

## 41. Identity Operators

```text
is
is not
```

`is` object identity compare करते.

---

## 42. Membership Operators

```text
in
not in
```

---

## 43. Bitwise Operators

```text
&
|
^
~
<<
>>
```

Binary-level operations साठी वापरले जातात.

---

# PART 9 — Conditional Statements

## 44. Conditional Statement

**Definition:**  
A conditional statement executes code based on a condition.

Types:

```text
if
if-else
if-elif-else
nested if
```

---

## 45. `if`

```python
if age >= 18:
    print("Adult")
```

---

## 46. `if-else`

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## 47. `if-elif-else`

Multiple conditions check करण्यासाठी.

```python
if marks >= 90:
    print("A+")
elif marks >= 75:
    print("A")
else:
    print("B")
```

---

## 48. Nested Condition

एका condition मध्ये दुसरी condition.

```python
if age >= 18:
    if citizen:
        print("Eligible")
```

---

# PART 10 — Loops

## 49. Loop

**Definition:**  
A loop repeatedly executes a block of code.

Types:

```text
for
while
```

---

## 50. `for` Loop

```python
for i in range(5):
    print(i)
```

---

## 51. `while` Loop

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

## 52. `range()`

**Definition:**  
Creates a range object representing a sequence of numbers.

```python
range(start, stop, step)
```

---

## 53. `break`

Loop पूर्णपणे stop करतो.

---

## 54. `continue`

Current iteration skip करतो.

---

## 55. `pass`

Placeholder म्हणून वापरतो.

---

# PART 11 — Strings

## 56. String

**Definition:**  
A string is an immutable sequence of characters.

```python
name = "Python"
```

---

## 57. String Indexing

```python
name[0]
```

---

## 58. Negative Indexing

```python
name[-1]
```

---

## 59. String Slicing

```python
name[start:stop:step]
```

---

## 60. Important String Methods

```text
upper()
lower()
capitalize()
title()
strip()
lstrip()
rstrip()
replace()
split()
join()
find()
index()
count()
startswith()
endswith()
isdigit()
isalpha()
isalnum()
```

---

## 61. String Formatting

Methods:

```text
f-string
format()
%
```

Modern Python मध्ये f-string preferred आहे.

---

# PART 12 — Python Collections

Python मधील **सर्वात important section**.

Main collections:

```text
List
Tuple
Set
Dictionary
```

---

# PART 13 — List

## 62. List

**Definition:**  
List is an ordered, mutable collection that can contain duplicate elements.

```python
students = ["Sachin", "Rahul", "Amit"]
```

Properties:

- Ordered
- Mutable
- Duplicate allowed
- Indexing
- Slicing
- Multiple data types

---

## 63. List Methods

```text
append()
extend()
insert()
remove()
pop()
clear()
index()
count()
sort()
reverse()
copy()
```

---

# PART 14 — Tuple

## 64. Tuple

**Definition:**  
Tuple is an ordered, immutable collection.

```python
data = (10, 20, 30)
```

Methods:

```text
count()
index()
```

---

# PART 15 — Set

## 65. Set

**Definition:**  
Set is a collection of unique elements.

```python
numbers = {1, 2, 3}
```

Important operations:

```text
union
intersection
difference
symmetric_difference
subset
superset
disjoint
```

Methods:

```text
add()
update()
remove()
discard()
pop()
clear()
```

---

# PART 16 — Dictionary

## 66. Dictionary

**Definition:**  
Dictionary is a mutable collection of key-value pairs.

```python
student = {
    "name": "Sachin",
    "age": 24
}
```

---

## 67. Dictionary Methods

```text
keys()
values()
items()
get()
update()
pop()
popitem()
setdefault()
clear()
copy()
fromkeys()
```

---

# PART 17 — Advanced Collections

## 68. Nested List

List inside list.

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

---

## 69. Nested Dictionary

Dictionary inside dictionary.

```python
students = {
    1: {"name": "Sachin"},
    2: {"name": "Rahul"}
}
```

---

## 70. List of Dictionaries

Backend development मध्ये अत्यंत common.

```python
students = [
    {"id": 1, "name": "Sachin"},
    {"id": 2, "name": "Rahul"}
]
```

---

# PART 18 — Comprehensions

## 71. List Comprehension

**Definition:**  
Concise syntax for creating lists.

```python
squares = [x*x for x in range(5)]
```

---

## 72. Set Comprehension

```python
values = {x*x for x in range(5)}
```

---

## 73. Dictionary Comprehension

```python
values = {x: x*x for x in range(5)}
```

---

## 74. Generator Expression

```python
values = (x*x for x in range(5))
```

---

# PART 19 — Functions

## 75. Function

**Definition:**  
A function is a reusable block of code designed to perform a specific task.

---

## 76. Function Syntax

```python
def function_name():
    pass
```

---

## 77. Parameter

Function definition मध्ये असलेला variable.

```python
def add(a, b):
    pass
```

`a`, `b` parameters आहेत.

---

## 78. Argument

Function call करताना pass केलेली actual value.

```python
add(10, 20)
```

---

## 79. Return

Function मधून result परत करण्यासाठी.

```python
def add(a, b):
    return a + b
```

---

## 80. Default Arguments

```python
def greet(name="Guest"):
    print(name)
```

---

## 81. Keyword Arguments

```python
greet(name="Sachin")
```

---

## 82. Positional Arguments

```python
add(10, 20)
```

---

## 83. `*args`

Multiple positional arguments.

```python
def test(*args):
    print(args)
```

---

## 84. `**kwargs`

Multiple keyword arguments.

```python
def test(**kwargs):
    print(kwargs)
```

---

## 85. Lambda Function

**Definition:**  
A lambda is a small anonymous function.

```python
square = lambda x: x * x
```

---

## 86. Recursive Function

**Definition:**  
A function that calls itself is called a recursive function.

```python
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)
```

---

# PART 20 — Scope

## 87. Scope

**Definition:**  
Scope defines where a variable can be accessed.

Main:

```text
Local
Enclosing
Global
Built-in
```

LEGB rule.

---

## 88. Local Variable

Function मध्ये तयार होतो.

---

## 89. Global Variable

Module/function बाहेर define होतो.

---

## 90. `global`

Global variable modify करण्यासाठी.

---

## 91. `nonlocal`

Nested function मधील enclosing scope variable modify करण्यासाठी.

---

# PART 21 — Exception Handling

## 92. Exception

**Definition:**  
An exception is an event that interrupts normal program execution because of an error condition.

---

## 93. Exception Handling

Keywords:

```text
try
except
else
finally
raise
```

---

## 94. try

Risky code ठेवतो.

---

## 95. except

Exception handle करतो.

---

## 96. else

Exception नसेल तर execute होतो.

---

## 97. finally

Normally cleanup साठी execute होतो.

---

## 98. raise

Manually exception raise करण्यासाठी.

---

## 99. Custom Exception

आपली स्वतःची exception class तयार करू शकतो.

```python
class InvalidAgeError(Exception):
    pass
```

---

# PART 22 — File Handling

## 100. File Handling

**Definition:**  
File handling means reading, writing, updating and managing files using Python.

---

## 101. `open()`

```python
open("data.txt", "r")
```

---

## 102. File Modes

```text
r
w
a
x
b
t
+
```

---

## 103. `read()`

पूर्ण file read.

---

## 104. `readline()`

एक line read.

---

## 105. `readlines()`

सर्व lines list स्वरूपात.

---

## 106. `write()`

File मध्ये data लिहितो.

---

## 107. `writelines()`

Multiple lines write करण्यासाठी.

---

## 108. `with open()`

Context manager वापरून file safely handle करण्यासाठी.

---

# PART 23 — JSON

## 109. JSON

**Definition:**  
JSON stands for JavaScript Object Notation and is a text format commonly used for data exchange.

---

## 110. Python JSON Module

```python
import json
```

---

## 111. `json.load()`

JSON file → Python object.

---

## 112. `json.loads()`

JSON string → Python object.

---

## 113. `json.dump()`

Python object → JSON file.

---

## 114. `json.dumps()`

Python object → JSON string.

---

# PART 24 — Modules & Packages

## 115. Module

**Definition:**  
A module is a Python file containing reusable code.

---

## 116. Package

**Definition:**  
A package is a collection of related Python modules.

---

## 117. `import`

```python
import math
```

---

## 118. `from ... import`

```python
from math import sqrt
```

---

## 119. Alias

```python
import pandas as pd
```

---

## 120. `__name__`

Special variable used to determine whether a file is being run directly or imported.

```python
if __name__ == "__main__":
    main()
```

---

# PART 25 — OOP

## 121. OOP

**Definition:**  
Object-Oriented Programming is a programming paradigm based on objects and classes.

---

## 122. Class

**Definition:**  
A class is a blueprint for creating objects.

---

## 123. Object

**Definition:**  
An object is an instance of a class.

---

## 124. Constructor

Python मध्ये commonly:

```python
__init__()
```

---

## 125. `self`

Current object ला refer करते.

---

## 126. Instance Variable

प्रत्येक object ची स्वतःची variable.

---

## 127. Instance Method

Object-specific behavior define करणारी method.

---

## 128. Class Variable

Class च्या सर्व instances मध्ये shared variable.

---

## 129. Class Method

`@classmethod` वापरून define केलेली method.

---

## 130. Static Method

`@staticmethod` वापरून define केलेली utility method.

---

## 131. Encapsulation

**Definition:**  
Bundling data and methods together and controlling access to internal state.

---

## 132. Inheritance

**Definition:**  
One class acquiring features/behavior from another class.

Types:

```text
Single
Multiple
Multilevel
Hierarchical
Hybrid
```

---

## 133. Polymorphism

**Definition:**  
Same interface/name can have different behavior.

---

## 134. Method Overriding

Child class parent method ची स्वतःची implementation देते.

---

## 135. Method Overloading

Python मध्ये traditional method overloading नाही; default arguments, `*args`, etc. वापरून similar behavior implement करता येतो.

---

## 136. Abstraction

**Definition:**  
Hiding implementation details and exposing essential behavior.

---

## 137. Abstract Class

`ABC` आणि `abstractmethod` वापरता येतात.

---

## 138. Interface

Python मध्ये Java सारखा dedicated `interface` keyword नाही.

Interface-like design साठी:

```text
ABC
Protocol
Duck Typing
```

---

# PART 26 — Special / Magic Methods

## 139. Magic Methods

Double underscore methods.

Examples:

```text
__init__
__str__
__repr__
__len__
__eq__
__add__
__iter__
__next__
```

---

## 140. `__str__`

Object ची user-friendly string representation.

---

## 141. `__repr__`

Developer-oriented representation.

---

## 142. Operator Overloading

Operators ला custom objects साठी behavior देणे.

Example:

```python
__add__
```

---

# PART 27 — Iterator & Generator

## 143. Iterable

**Definition:**  
An object that can be iterated over.

Examples:

```text
list
tuple
string
dict
set
```

---

## 144. Iterator

**Definition:**  
An object that produces values one at a time using iteration protocol.

Important:

```text
__iter__()
__next__()
```

---

## 145. Generator

**Definition:**  
A generator produces values lazily using `yield`.

---

## 146. `yield`

Function ला generator मध्ये बदलण्यासाठी वापरतो.

---

## 147. Generator vs List

Generator memory efficient असतो कारण values एकावेळी generate करतो.

---

# PART 28 — Decorators

## 148. Decorator

**Definition:**  
A decorator modifies or extends function/class behavior without directly changing its source code.

Syntax:

```python
@decorator
def function():
    pass
```

---

## 149. Function as Object

Python मध्ये functions first-class objects आहेत.

---

## 150. Higher-Order Function

Function accept करणारी किंवा function return करणारी function.

---

# PART 29 — Context Manager

## 151. Context Manager

**Definition:**  
A context manager manages setup and cleanup around a block of code.

Common:

```python
with open(...) as file:
    ...
```

Advanced:

```text
__enter__()
__exit__()
```

---

# PART 30 — Regular Expression

## 152. Regex

**Definition:**  
Regular Expression is a pattern used to search, match, validate or manipulate text.

Module:

```python
import re
```

Important:

```text
match()
search()
findall()
finditer()
sub()
split()
compile()
```

---

# PART 31 — Date & Time

## 153. `datetime`

Date/time handling साठी.

Important:

```text
date
time
datetime
timedelta
timezone
```

---

# PART 32 — Functional Programming

## 154. Functional Programming

Functions ला first-class values म्हणून वापरून computation design करण्याची programming style.

---

## 155. `map()`

प्रत्येक element वर function apply करतो.

---

## 156. `filter()`

Condition satisfy करणारे elements select करतो.

---

## 157. `reduce()`

Multiple values combine करून एक result तयार करतो.

Module:

```python
from functools import reduce
```

---

## 158. `zip()`

Multiple iterables pair करण्यासाठी.

```python
names = ["A", "B"]
ages = [20, 21]

list(zip(names, ages))
```

---

## 159. `enumerate()`

Index आणि value दोन्ही मिळवण्यासाठी.

```python
for index, value in enumerate(names):
    print(index, value)
```

---

# PART 33 — Collections Module

## 160. `collections`

Python standard library मधील specialized collection types.

---

## 161. Counter

Elements किती वेळा आले ते count करतो.

---

## 162. defaultdict

Missing key साठी default value देतो.

---

## 163. deque

Efficient double-ended queue.

---

## 164. namedtuple

Tuple ला named fields देण्यासाठी.

---

# PART 34 — Copying

## 165. Assignment

एकच object reference share होऊ शकतो.

---

## 166. Shallow Copy

Outer object copy होतो पण nested objects share होऊ शकतात.

Module:

```python
import copy
```

```python
copy.copy()
```

---

## 167. Deep Copy

Nested objects सुद्धा recursively copy करतो.

```python
copy.deepcopy()
```

---

# PART 35 — Memory Management

## 168. Memory Management

Python automatically memory manage करण्याचा प्रयत्न करतो.

Concepts:

```text
Object
Reference
Reference Counting
Garbage Collection
Heap
Stack
```

---

## 169. Garbage Collection

Unused objects ची memory reclaim करण्यासाठी Python garbage collector वापरतो.

---

## 170. Reference Counting

Object ला किती references आहेत हे track करण्याची mechanism.

---

# PART 36 — Python Packages

Important third-party packages:

```text
requests
FastAPI
Django
Flask
SQLAlchemy
Pydantic
pytest
pandas
numpy
```

---

# PART 37 — Database Programming

## 171. Database

**Definition:**  
A database is an organized system for storing and managing data.

---

## 172. SQL

**Definition:**  
SQL is a language used to interact with relational databases.

Important:

```text
SELECT
INSERT
UPDATE
DELETE
CREATE
ALTER
DROP
JOIN
GROUP BY
ORDER BY
```

---

## 173. Python + MySQL

Popular options:

```text
mysql-connector-python
PyMySQL
SQLAlchemy
```

---

## 174. CRUD

**Definition:**  
CRUD means:

```text
C → Create
R → Read
U → Update
D → Delete
```

---

# PART 38 — API

## 175. API

**Definition:**  
API stands for Application Programming Interface. It defines how software components communicate.

---

## 176. REST API

**Definition:**  
REST API is an API style commonly using HTTP methods and resource-oriented URLs.

---

## 177. HTTP Methods

```text
GET
POST
PUT
PATCH
DELETE
```

---

## 178. HTTP Status Codes

### 2xx

Success:

```text
200 OK
201 Created
204 No Content
```

### 4xx

Client errors:

```text
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
422 Unprocessable Content
```

### 5xx

Server errors:

```text
500 Internal Server Error
502 Bad Gateway
503 Service Unavailable
```

---

# PART 39 — HTTP Concepts

## 179. Request

Client → Server message.

---

## 180. Response

Server → Client message.

---

## 181. Headers

Request/response metadata.

---

## 182. Query Parameters

Example:

```text
/products?page=1&limit=10
```

---

## 183. Path Parameters

Example:

```text
/products/10
```

---

## 184. Request Body

POST/PUT/PATCH मध्ये data पाठवण्यासाठी.

Example:

```json
{
    "name": "Laptop",
    "price": 50000
}
```

---

# PART 40 — Multithreading

## 185. Process

**Definition:**  
A process is an independent running instance of a program.

---

## 186. Thread

**Definition:**  
A thread is a unit of execution within a process.

---

## 187. Multithreading

Multiple threads वापरून tasks concurrently handle करणे.

---

## 188. GIL

**Definition:**  
CPython's Global Interpreter Lock allows only one thread at a time to execute Python bytecode in a process.

I/O-bound tasks साठी threading useful असू शकते.

---

## 189. CPU-bound

CPU intensive tasks.

Examples:

```text
heavy calculations
image processing
large computations
```

---

## 190. I/O-bound

Input/output waiting tasks.

Examples:

```text
API calls
Database calls
File operations
Network operations
```

---

# PART 41 — Multiprocessing

## 191. Multiprocessing

Multiple processes वापरून काम execute करणे.

CPU-bound tasks साठी useful.

---

# PART 42 — Async Programming

## 192. Asynchronous Programming

**Definition:**  
A programming model where tasks can make progress without blocking the entire program while waiting for I/O.

---

## 193. Coroutine

`async def` function call केल्यावर coroutine object मिळतो.

---

## 194. `async`

Async function define करण्यासाठी.

---

## 195. `await`

Async operation ची result मिळेपर्यंत coroutine suspend करण्यासाठी.

---

## 196. `asyncio`

Python चे asynchronous programming framework/library.

---

## 197. Event Loop

Async tasks schedule आणि manage करतो.

---

## 198. `asyncio.gather()`

Multiple async tasks concurrently run करण्यासाठी.

---

# PART 43 — Threading vs Multiprocessing vs Async

| Technology | Best Use |
|---|---|
| Threading | I/O-bound blocking tasks |
| Multiprocessing | CPU-bound tasks |
| Asyncio | High-concurrency async I/O |

---

# PART 44 — Socket Programming

## 199. Socket

**Definition:**  
A socket is an endpoint for communication between programs over a network.

---

## 200. TCP

Reliable, connection-oriented protocol.

---

## 201. UDP

Connectionless, lightweight protocol.

---

## 202. Client

Server कडे request/connection initiate करणारा program.

---

## 203. Server

Client requests accept करून response देणारा program.

---

## 204. IP Address

Network device/application identify करण्यासाठी address.

---

## 205. Port

Network service/application identify करण्यासाठी number.

---

# PART 45 — Event-Driven Programming

## 206. Event

Program मध्ये घडणारी घटना.

Example:

```text
Button Click
User Login
Payment Completed
Order Created
```

---

## 207. Event Handler

Event झाल्यावर execute होणारा function.

---

## 208. Event Dispatcher

Event योग्य handlers कडे पाठवतो.

---

## 209. Callback

नंतर execute करण्यासाठी दुसऱ्या function ला दिलेले function.

---

## 210. Publish-Subscribe

Publisher event publish करतो आणि subscribers त्या event वर react करतात.

---

# PART 46 — Testing

## 211. Software Testing

**Definition:**  
Testing verifies whether software behaves as expected.

---

## 212. Unit Testing

Smallest unit/function independently test करणे.

---

## 213. Integration Testing

Multiple components together test करणे.

---

## 214. End-to-End Testing

Complete application flow test करणे.

---

## 215. pytest

Python मधील popular testing framework.

Example:

```python
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
```

---

# PART 47 — Debugging

## 216. Debugging

**Definition:**  
Finding and fixing errors/bugs in software.

Important:

```text
Breakpoint
Step Over
Step Into
Step Out
Watch
Call Stack
```

---

# PART 48 — Logging

## 217. Logging

**Definition:**  
Logging records application events and diagnostic information.

Python:

```python
import logging
```

Levels:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

---

# PART 49 — Security Basics

Python backend developer म्हणून:

```text
Authentication
Authorization
Password Hashing
JWT
OAuth2
CORS
CSRF
SQL Injection
Input Validation
Rate Limiting
Secrets Management
HTTPS
```

हे concepts समजणे आवश्यक आहे.

---

# PART 50 — Django

## 218. Django

**Definition:**  
Django is a high-level Python web framework for building web applications.

---

## 219. Django Project

पूर्ण Django application configuration.

---

## 220. Django App

Specific functionality/module.

Example:

```text
users
products
orders
payments
```

---

## 221. Django MVT

```text
Model
View
Template
```

---

## 222. Django URL

URL request योग्य view कडे route करतो.

---

## 223. Django View

Business/request handling logic.

---

## 224. Django Model

Database structure represent करणारा Python class.

---

## 225. Django Template

Presentation/UI layer.

---

## 226. Django ORM

Python objects/classes वापरून database access करण्याची सुविधा.

---

## 227. Migration

Model/database schema changes track/apply करण्याची system.

---

## 228. Django Admin

Database/application management साठी built-in admin interface.

---

## 229. Middleware

Request आणि response processing pipeline मध्ये काम करणारा component.

---

## 230. Django Authentication

Login, logout, users, permissions इत्यादी manage करण्याची सुविधा.

---

# PART 51 — Django REST Framework

## 231. DRF

**Definition:**  
Django REST Framework is a toolkit for building Web APIs with Django.

---

## 232. Serializer

Python/Django objects ↔ JSON representation conversion आणि validation.

---

## 233. APIView

Class-based API view.

---

## 234. GenericAPIView

Reusable generic API functionality देणारा base class.

---

## 235. ViewSet

Related API operations एका class मध्ये organize करण्याची सुविधा.

---

## 236. Router

ViewSets साठी URLs automatically generate करण्यास मदत करतो.

---

## 237. Permissions

User ला specific API operation करण्याची परवानगी आहे का ते control करतात.

---

# PART 52 — FastAPI

## 238. FastAPI

**Definition:**  
FastAPI is a modern Python framework for building APIs using Python type hints.

---

## 239. Pydantic

**Definition:**  
Pydantic is used for data validation and parsing using Python type annotations.

---

## 240. BaseModel

Request/response data models define करण्यासाठी.

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
```

---

## 241. Field

Advanced validation/configuration साठी.

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(min_length=2)
    price: float = Field(gt=0)
```

---

## 242. APIRouter

API routes modularize करण्यासाठी.

```python
router = APIRouter(
    prefix="/api/products",
    tags=["Products"]
)
```

---

## 243. Dependency Injection

**Definition:**  
Dependency Injection means providing required dependencies to a component instead of creating them internally.

FastAPI:

```python
Depends()
```

---

## 244. HTTPException

API मध्ये HTTP error response देण्यासाठी.

```python
raise HTTPException(
    status_code=404,
    detail="Product not found"
)
```

---

## 245. Middleware

सर्व किंवा specific requests/responses वर common processing करण्यासाठी.

---

## 246. Authentication

User कोण आहे हे verify करणे.

---

## 247. Authorization

User ला काय access आहे हे determine करणे.

---

## 248. JWT

**Definition:**  
JSON Web Token is a compact token format commonly used for authentication/authorization.

---

# PART 53 — Backend Architecture

## 249. Layered Architecture

Common layers:

```text
Controller / Router
        ↓
Service
        ↓
Repository
        ↓
Database
```

---

## 250. Controller / Router

HTTP request handle करतो.

---

## 251. Service Layer

Business logic ठेवतो.

---

## 252. Repository Layer

Database access logic ठेवतो.

---

## 253. Model

Data/entity representation.

---

## 254. Schema

Input/output validation structure.

---

# PART 54 — Design Principles

## 255. DRY

**Don't Repeat Yourself**

Same logic unnecessary repeated करू नये.

---

## 256. KISS

**Keep It Simple, Stupid**

Unnecessary complexity avoid करावी.

---

## 257. YAGNI

**You Aren't Gonna Need It**

Need नसलेला feature आधीच implement करू नये.

---

## 258. SOLID

Object-oriented design चे five principles:

```text
S → Single Responsibility
O → Open/Closed
L → Liskov Substitution
I → Interface Segregation
D → Dependency Inversion
```

---

# PART 55 — Clean Architecture

Common idea:

```text
API
 ↓
Application / Service
 ↓
Domain
 ↓
Infrastructure
```

Goal:

- Low coupling
- High maintainability
- Testability
- Separation of concerns

---

# PART 56 — Git & Python Projects

Important Git commands:

```bash
git init
git clone
git status
git add .
git commit
git push
git pull
git branch
git checkout
git switch
git merge
git log
```

Python developer म्हणून Git/GitHub येणे आवश्यक आहे.

---

# PART 57 — Environment Variables

Sensitive/config values code मध्ये hardcode करू नयेत.

Example:

```text
DATABASE_URL
SECRET_KEY
JWT_SECRET
API_KEY
```

`.env` file वापरू शकतो.

Popular library:

```text
python-dotenv
```

---

# PART 58 — Python Project Structure

Typical backend project:

```text
project/
│
├── app/
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   ├── services/
│   ├── repositories/
│   ├── database/
│   └── utils/
│
├── tests/
├── .env
├── requirements.txt
├── .gitignore
└── README.md
```

---

# PART 59 — Important Python Advanced Topics

हे topics पुढच्या level ला कर:

```text
Descriptors
Properties
@property
__slots__
Dataclasses
Protocols
Typing
Generics
Type Hints
Callable
Optional
Union
Literal
TypeAlias
Pattern Matching
Structural Pattern Matching
Contextlib
Functools
Itertools
Async Generators
Async Context Managers
Async Iterators
Metaclasses
Descriptors
Dependency Injection
Design Patterns
```

---

# PART 60 — Type Hints

## 259. Type Hint

**Definition:**  
Type hints describe expected types of variables, parameters and return values.

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

# PART 61 — Dataclass

## 260. Dataclass

**Definition:**  
A dataclass is a convenient way to create classes primarily used for storing data.

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
```

---

# PART 62 — Properties

## 261. `@property`

Method ला attribute सारखे access करण्याची सुविधा.

```python
class Student:

    @property
    def name(self):
        return self._name
```

---

# PART 63 — Design Patterns

Important Python design patterns:

```text
Singleton
Factory
Abstract Factory
Builder
Strategy
Observer
Repository
Dependency Injection
Adapter
Decorator
Facade
```

Backend मध्ये especially:

```text
Repository Pattern
Service Pattern
Factory Pattern
Dependency Injection
Strategy Pattern
```

important आहेत.

---

# PART 64 — Python Performance

Important concepts:

```text
Time Complexity
Space Complexity
Big O
Memory Usage
Lazy Evaluation
Generators
Caching
Profiling
Optimization
```

---

# PART 65 — Python Interview Topics

Interview साठी हे questions नक्की prepare कर:

### Basic

1. What is Python?
2. Features of Python?
3. Python interpreted आहे का?
4. Python dynamically typed म्हणजे काय?
5. Mutable vs immutable?
6. List vs tuple?
7. Set vs dictionary?
8. `is` vs `==`?
9. `*args` vs `**kwargs`?
10. `pass` vs `continue` vs `break`?

### Functions

11. Function म्हणजे काय?
12. Parameter vs argument?
13. Return vs print?
14. Lambda?
15. Recursion?
16. Scope?
17. LEGB?

### OOP

18. Class vs object?
19. Constructor?
20. `self`?
21. Instance vs class variable?
22. Class method vs static method?
23. Inheritance?
24. Polymorphism?
25. Encapsulation?
26. Abstraction?
27. Method overriding?
28. Multiple inheritance?

### Advanced

29. Iterator?
30. Generator?
31. `yield`?
32. Decorator?
33. Context manager?
34. Shallow copy vs deep copy?
35. Garbage collection?
36. GIL?
37. Thread vs process?
38. Async vs threading?

### Backend

39. API म्हणजे काय?
40. REST API?
41. GET vs POST?
42. PUT vs PATCH?
43. Authentication vs Authorization?
44. JWT?
45. Middleware?
46. Dependency Injection?
47. Repository Pattern?
48. Service Layer?
49. ORM?
50. CRUD?

### FastAPI

51. FastAPI काय आहे?
52. Pydantic काय आहे?
53. BaseModel?
54. Field?
55. APIRouter?
56. Depends?
57. HTTPException?
58. async/await?
59. Middleware?
60. Swagger/OpenAPI?

### Django

61. Django काय आहे?
62. MVT?
63. Model?
64. View?
65. Template?
66. ORM?
67. Migration?
68. Middleware?
69. Django Admin?
70. DRF?

---

# 🎯 Complete Python Learning Map

शेवटी तुला Python मध्ये हा flow येणे अपेक्षित आहे:

```text
PYTHON
│
├── Fundamentals
│   ├── Syntax
│   ├── Variables
│   ├── Data Types
│   ├── Operators
│   ├── Input/Output
│   └── Conditions
│
├── Control Flow
│   ├── if
│   ├── for
│   ├── while
│   ├── break
│   ├── continue
│   └── pass
│
├── Functions
│   ├── Parameters
│   ├── Arguments
│   ├── Return
│   ├── Lambda
│   ├── *args
│   ├── **kwargs
│   └── Recursion
│
├── Collections
│   ├── List
│   ├── Tuple
│   ├── Set
│   ├── Dictionary
│   ├── Comprehension
│   └── collections module
│
├── Error Handling
│   ├── try
│   ├── except
│   ├── else
│   ├── finally
│   └── raise
│
├── Files
│   ├── TXT
│   ├── JSON
│   └── CSV
│
├── OOP
│   ├── Class
│   ├── Object
│   ├── Constructor
│   ├── self
│   ├── Encapsulation
│   ├── Inheritance
│   ├── Polymorphism
│   └── Abstraction
│
├── Advanced Python
│   ├── Iterator
│   ├── Generator
│   ├── Decorator
│   ├── Context Manager
│   ├── Regex
│   ├── Dataclass
│   ├── Type Hints
│   └── Async
│
├── Database
│   ├── SQL
│   ├── MySQL
│   ├── SQLite
│   ├── ORM
│   └── SQLAlchemy
│
├── Networking
│   ├── HTTP
│   ├── REST
│   ├── API
│   └── Socket
│
├── Concurrency
│   ├── Threading
│   ├── Multiprocessing
│   ├── Asyncio
│   ├── async
│   └── await
│
├── Web Development
│   ├── Django
│   ├── Django REST Framework
│   └── FastAPI
│
├── Software Engineering
│   ├── SOLID
│   ├── DRY
│   ├── KISS
│   ├── Clean Architecture
│   ├── Design Patterns
│   └── Testing
│
└── Professional Development
    ├── Git
    ├── GitHub
    ├── Debugging
    ├── Logging
    ├── Security
    ├── Deployment
    └── Interview Preparation
```

################################################################################
################################################################################


हो Sachin. खाली **Python Interview Questions 1–70** चे **Definition + English Explanation + Marathi Explanation + Example + Interview Answer + Important Points** देतो. हे **Fresher Python Developer / Backend / FastAPI / Django interview** साठी तयार केले आहे.

---

# 🐍 PART 65 — PYTHON INTERVIEW QUESTIONS & ANSWERS

# 🔹 SECTION 1 — BASIC PYTHON

---

## 1. What is Python?

### Definition
**Python is a high-level, interpreted, general-purpose programming language.**

### Marathi
Python ही high-level, interpreted आणि general-purpose programming language आहे.

### Python कुठे वापरतात?

- Web Development
- Backend Development
- REST API
- Automation
- Data Science
- AI/ML
- Testing
- Scripting
- Desktop Applications

### Example

```python
name = "Sachin"
print(name)
```

### Interview Answer

> Python is a high-level, interpreted, dynamically typed and general-purpose programming language known for its simple syntax and large ecosystem of libraries.

### Important
Python मध्ये readability आणि developer productivity वर जास्त focus आहे.

---

# 2. What are the features of Python?

### Definition
Features म्हणजे Python ची important characteristics.

### Main Features

1. Easy to learn
2. Readable syntax
3. High-level
4. Interpreted execution model
5. Dynamically typed
6. Object-oriented
7. Cross-platform
8. Open source
9. Large standard library
10. Huge third-party ecosystem
11. Automatic memory management
12. Supports multiple programming paradigms

### Example

```python
x = 10
print(x)
```

### Interview Answer

> Python provides simple syntax, dynamic typing, object-oriented programming, automatic memory management, cross-platform support and a large ecosystem of libraries.

---

# 3. Is Python interpreted?

### Short Answer

**Yes, Python is commonly described as an interpreted language.**

पण technically Python implementation execution थोडे अधिक complex आहे.

### CPython मध्ये basic flow

```text
Python Source Code
       ↓
Bytecode
       ↓
Python Virtual Machine
       ↓
Execution
```

Python source code internally bytecode मध्ये compile होतो आणि CPython runtime तो execute करतो.

### Interview Answer

> Python is generally called an interpreted language. In CPython, source code is first compiled into bytecode, which is then executed by the Python virtual machine.

### Important

Interview मध्ये फक्त:

> Python is an interpreted language.

असे म्हणणे basic level ला acceptable आहे; पण advanced interview मध्ये bytecode mention कर.

---

# 4. What is dynamically typed language?

### Definition

**In a dynamically typed language, variable types are determined at runtime rather than being explicitly declared for every variable.**

### Example

```python
x = 10

x = "Sachin"
```

पहिले:

```text
x → int
```

नंतर:

```text
x → str
```

Python मध्ये variable ला fixed datatype declare करावा लागत नाही.

### Marathi

Python मध्ये:

```python
x = 10
```

असे लिहितो.

```python
int x = 10
```

असे लिहिण्याची गरज नाही.

### Important

Python **dynamically typed** आहे.

Python **strongly typed** देखील मानला जातो; incompatible types आपोआप arbitrary conversion होत नाही.

---

# 5. Mutable vs Immutable

## Mutable

**Definition:**  
Object तयार झाल्यानंतर त्याची contents बदलता येत असतील तर object mutable आहे.

Examples:

```text
list
dict
set
```

Example:

```python
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
```

Output:

```text
[100, 20, 30]
```

---

## Immutable

**Definition:**  
Object तयार झाल्यानंतर त्याची value/content directly बदलता येत नसेल तर object immutable आहे.

Examples:

```text
int
float
bool
str
tuple
```

Example:

```python
name = "Sachin"

# name[0] = "R"
```

हे allowed नाही.

### Interview Answer

> Mutable objects can be changed after creation, while immutable objects cannot be changed after creation. Lists, dictionaries and sets are mutable, while strings, integers and tuples are immutable.

---

# 6. List vs Tuple

| List | Tuple |
|---|---|
| Mutable | Immutable |
| `[]` | `()` |
| More methods | Fewer methods |
| Can modify | Cannot modify |
| Generally used for changing collections | Useful for fixed collections |

### Example

```python
my_list = [10, 20, 30]

my_list[0] = 100
```

Works.

Tuple:

```python
my_tuple = (10, 20, 30)

# my_tuple[0] = 100
```

Error.

### Interview Answer

> A list is ordered and mutable, whereas a tuple is ordered and immutable. I use a list when data may change and a tuple when the collection should remain fixed.

---

# 7. Set vs Dictionary

## Set

**Definition:**  
A set is a collection of unique elements.

```python
numbers = {10, 20, 30}
```

Set मध्ये duplicate elements ठेवले जात नाहीत.

---

## Dictionary

**Definition:**  
A dictionary stores data as key-value pairs.

```python
student = {
    "name": "Sachin",
    "age": 24
}
```

### Difference

| Set | Dictionary |
|---|---|
| Values/elements | Key-value pairs |
| Unique elements | Keys must be unique |
| `{1,2,3}` | `{"id":1}` |

### Important

Empty:

```python
{}
```

हा **empty dictionary** आहे.

Empty set:

```python
set()
```

---

# 8. `is` vs `==`

हा खूप important interview question आहे.

## `==`

**Definition:**  
Checks whether two objects have equal values.

```python
a = [1, 2]
b = [1, 2]

print(a == b)
```

Output:

```text
True
```

---

## `is`

**Definition:**  
Checks whether two references point to the same object.

```python
print(a is b)
```

Output generally:

```text
False
```

कारण दोन वेगळे list objects आहेत.

### Simple Rule

```text
== → Value equality
is → Object identity
```

### Important

`is` values compare करण्यासाठी वापरू नये.

Common:

```python
if value is None:
    ...
```

---

# 9. `*args` vs `**kwargs`

## `*args`

Multiple positional arguments accept करण्यासाठी.

```python
def add(*args):
    print(args)

add(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

`args` internally tuple असतो.

---

## `**kwargs`

Multiple keyword arguments accept करण्यासाठी.

```python
def student(**kwargs):
    print(kwargs)

student(name="Sachin", age=24)
```

Output:

```text
{'name': 'Sachin', 'age': 24}
```

`kwargs` internally dictionary असतो.

### Interview Answer

> `*args` collects variable-length positional arguments as a tuple, while `**kwargs` collects variable-length keyword arguments as a dictionary.

---

# 10. `pass` vs `continue` vs `break`

## `pass`

**Definition:**  
Does nothing; used as a placeholder.

```python
if True:
    pass
```

---

## `continue`

**Definition:**  
Skips the current loop iteration.

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

---

## `break`

**Definition:**  
Terminates the loop completely.

```python
for i in range(5):

    if i == 2:
        break

    print(i)
```

### Remember

```text
pass     → Do nothing
continue → Skip current iteration
break    → Stop loop
```

---

# 🔹 SECTION 2 — FUNCTIONS

# 11. What is a Function?

### Definition

**A function is a reusable block of code designed to perform a specific task.**

### Example

```python
def add(a, b):
    return a + b
```

Call:

```python
result = add(10, 20)
```

### Benefits

- Code reuse
- Maintainability
- Readability
- Testing easy
- Avoid repetition

---

# 12. Parameter vs Argument

### Parameter

Function definition मधील variable.

```python
def add(a, b):
```

`a` and `b` = parameters.

### Argument

Function call करताना pass केलेली value.

```python
add(10, 20)
```

`10` and `20` = arguments.

### Interview Answer

> A parameter is a variable defined in the function definition, while an argument is the actual value passed during a function call.

---

# 13. Return vs Print

## `print()`

Screen वर output display करतो.

```python
def add(a, b):
    print(a + b)
```

## `return`

Function मधून value caller कडे परत पाठवतो.

```python
def add(a, b):
    return a + b
```

### Important

```python
result = add(10, 20)
```

`return` असल्यामुळे result मध्ये value मिळते.

### Interview Answer

> `print()` displays a value, while `return` sends a value back to the caller and can be stored or used by other code.

---

# 14. What is Lambda?

### Definition

**Lambda is a small anonymous function written using the `lambda` keyword.**

Syntax:

```python
lambda arguments: expression
```

Example:

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

### Use

Short operations:

```python
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x*x, numbers))
```

### Important

Complex business logic साठी normal `def` function अधिक readable असतो.

---

# 15. What is Recursion?

### Definition

**Recursion is a technique where a function calls itself.**

Example:

```python
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)
```

```python
print(factorial(5))
```

Output:

```text
120
```

### Important

Recursion मध्ये **base condition** आवश्यक आहे.

नाहीतर infinite recursion होऊ शकते.

---

# 16. What is Scope?

### Definition

**Scope defines where a variable can be accessed in a program.**

Python मध्ये major scopes:

```text
Local
Enclosing
Global
Built-in
```

---

## Local

```python
def test():
    x = 10
```

`x` local आहे.

---

## Global

```python
x = 100

def test():
    print(x)
```

---

# 17. What is LEGB?

### Definition

**LEGB is the order Python uses to search for a variable name.**

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

Example:

```python
x = "global"

def outer():

    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()
```

Python आधी Local scope मध्ये शोधतो.

---

# 🔹 SECTION 3 — OOP

# 18. Class vs Object

## Class

**Definition:**  
A class is a blueprint/template for creating objects.

```python
class Student:
    pass
```

## Object

**Definition:**  
An object is an instance of a class.

```python
student1 = Student()
```

### Simple

```text
Class  → Blueprint
Object → Actual instance
```

Real-world:

```text
Class  → Car design
Object → Actual car
```

---

# 19. What is Constructor?

### Definition

Constructor is commonly the initialization method used to initialize a newly created object.

Python मध्ये:

```python
__init__()
```

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Object:

```python
student = Student("Sachin", 24)
```

`__init__()` automatically called होतो.

### Important

Technically Python object creation आणि initialization वेगळ्या concepts आहेत (`__new__` आणि `__init__`). Interview मध्ये `__init__` ला constructor म्हणणे common आहे.

---

# 20. What is `self`?

### Definition

`self` current object instance ला refer करते.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

जर:

```python
s1 = Student("Sachin")
```

तर `self` म्हणजे `s1`.

जर:

```python
s2 = Student("Rahul")
```

तर `self` म्हणजे `s2`.

### Important

`self` Python keyword नाही; तो conventional parameter name आहे.

---

# 21. Instance Variable vs Class Variable

## Instance Variable

प्रत्येक object ची independent value.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

---

## Class Variable

Class level वर define केलेली shared attribute.

```python
class Student:

    college = "ABC"
```

### Difference

```text
Instance variable → Object-specific
Class variable    → Class-level/shared
```

---

# 22. Class Method vs Static Method

## Class Method

`@classmethod`

Class ला `cls` द्वारे access करते.

```python
class Student:

    college = "ABC"

    @classmethod
    def change_college(cls, name):
        cls.college = name
```

---

## Static Method

`@staticmethod`

Class किंवा instance state ची आवश्यकता नसलेली utility operation.

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
```

### Difference

| Class Method | Static Method |
|---|---|
| `@classmethod` | `@staticmethod` |
| `cls` parameter | No automatic `cls/self` |
| Class state access | Usually independent utility |

---

# 23. What is Inheritance?

### Definition

**Inheritance allows a child class to reuse or extend functionality of a parent class.**

Example:

```python
class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):
    pass
```

```python
dog = Dog()
dog.speak()
```

### Types

```text
Single
Multiple
Multilevel
Hierarchical
Hybrid
```

---

# 24. What is Polymorphism?

### Definition

**Polymorphism means the same interface or method name can have different behavior depending on the object.**

Example:

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")
```

```python
animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

Output:

```text
Bark
Meow
```

---

# 25. What is Encapsulation?

### Definition

**Encapsulation means bundling data and methods together and controlling access to internal state.**

Python:

```python
class Account:

    def __init__(self):
        self.__balance = 1000
```

`__balance` name-mangling करते.

### Important

Python मध्ये Java सारखा strict `private` keyword नाही.

---

# 26. What is Abstraction?

### Definition

**Abstraction means hiding implementation details and exposing only necessary functionality.**

Real-world:

ATM वापरताना:

```text
Withdraw
Deposit
Balance
```

दिसते.

पण internally transaction कशी process होते ते दिसत नाही.

---

# 27. What is Method Overriding?

### Definition

**When a child class provides its own implementation of a method defined in the parent class, it is method overriding.**

```python
class Animal:

    def sound(self):
        print("Animal")


class Dog(Animal):

    def sound(self):
        print("Bark")
```

Dog ची `sound()` parent method override करते.

---

# 28. What is Multiple Inheritance?

### Definition

**Multiple inheritance means a class inherits from more than one parent class.**

```python
class A:
    pass


class B:
    pass


class C(A, B):
    pass
```

Python multiple inheritance support करतो.

### Important Concept

```text
MRO
```

MRO = Method Resolution Order.

Check:

```python
print(C.mro())
```

---

# 🔹 SECTION 4 — ADVANCED PYTHON

# 29. What is Iterator?

### Definition

**An iterator is an object that returns items one at a time and follows the iterator protocol.**

Important methods:

```text
__iter__()
__next__()
```

Example:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
```

Output:

```text
10
20
```

---

# 30. What is Generator?

### Definition

**A generator is a special iterator that produces values lazily, usually using `yield`.**

Example:

```python
def numbers():

    yield 1
    yield 2
    yield 3
```

Use:

```python
for number in numbers():
    print(number)
```

### Advantage

Memory efficient.

सर्व values एकदम memory मध्ये ठेवण्याऐवजी आवश्यकतेनुसार generate करतो.

---

# 31. What is `yield`?

### Definition

`yield` function मधून एक value produce करून function ची state preserve करते आणि पुढच्या `next()` वर execution resume होऊ शकते.

Example:

```python
def test():
    yield 10
    yield 20
```

`yield` वापरल्यामुळे function generator function बनते.

---

# 32. What is Decorator?

### Definition

**A decorator is a callable that modifies or extends the behavior of another function or class without directly changing its source code.**

Example:

```python
def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper
```

Use:

```python
@decorator
def hello():
    print("Hello")
```

### FastAPI Example

```python
@app.get("/")
def home():
    return {"message": "Hello"}
```

इथे `@app.get("/")` हा decorator आहे.

---

# 33. What is Context Manager?

### Definition

**A context manager manages setup and cleanup around a block of code.**

Example:

```python
with open("data.txt") as file:
    data = file.read()
```

File automatically close होण्यास मदत होते.

### Advanced

Context manager protocol:

```text
__enter__()
__exit__()
```

---

# 34. Shallow Copy vs Deep Copy

## Shallow Copy

Outer object copy होतो; nested objects references share करू शकतात.

```python
import copy

new_data = copy.copy(data)
```

---

## Deep Copy

Nested objects सुद्धा recursively copy होतात.

```python
new_data = copy.deepcopy(data)
```

### Difference

```text
Shallow → Nested objects may be shared
Deep    → Nested objects copied
```

---

# 35. Garbage Collection

### Definition

**Garbage collection is the process of reclaiming memory from objects that are no longer needed.**

Python automatic memory management provide करतो.

CPython मध्ये:

```text
Reference Counting
+
Cyclic Garbage Collector
```

important mechanisms आहेत.

---

# 36. What is GIL?

### Definition

**GIL stands for Global Interpreter Lock.**

CPython मध्ये GIL मुळे एका process मध्ये एका क्षणी साधारणपणे एक thread Python bytecode execute करू शकतो.

### Important

GIL चा अर्थ:

> Python मध्ये threads कधीच useful नाहीत

असा नाही.

I/O-bound कामांमध्ये threads useful असू शकतात.

CPU-bound pure Python workloads साठी multiprocessing उपयोगी ठरू शकते.

---

# 37. Thread vs Process

## Thread

Process मधील execution unit.

## Process

Independent program execution environment.

| Thread | Process |
|---|---|
| Same process memory share करू शकतात | Separate memory space |
| Lightweight | Heavier |
| I/O-bound useful | CPU-bound useful |
| GIL affects Python bytecode execution in CPython | Separate processes can execute independently |

---

# 38. Async vs Threading

## Threading

Multiple threads वापरतात.

## Async

Event loop आणि coroutines वापरतात.

### Async Example

```python
async def get_data():
    result = await fetch_data()
    return result
```

### Comparison

```text
Threading
→ Multiple threads

Async
→ Event loop + coroutines

Threading
→ Blocking I/O handle करण्यासाठी useful

Async
→ High-concurrency async I/O साठी useful
```

---

# 🔹 SECTION 5 — BACKEND

# 39. What is API?

### Definition

**API stands for Application Programming Interface. It is a defined way for software components to communicate.**

Example:

```text
Frontend
   ↓
API
   ↓
Backend
   ↓
Database
```

उदा.:

```text
GET /api/products
```

Frontend API call करतो.

Backend response देतो.

---

# 40. What is REST API?

### Definition

**REST stands for Representational State Transfer. REST is an architectural style for designing network APIs.**

REST API मध्ये resources आणि HTTP methods वापरतात.

Example:

```text
GET    /products
GET    /products/10
POST   /products
PUT    /products/10
PATCH  /products/10
DELETE /products/10
```

---

# 41. GET vs POST

## GET

Data retrieve करण्यासाठी.

```http
GET /products
```

## POST

New resource/data create करण्यासाठी.

```http
POST /products
```

### Difference

| GET | POST |
|---|---|
| Read/retrieve | Create/submit |
| Usually query/path data | Usually request body |
| Safe/idempotent semantics | Generally not idempotent |
| Should not modify resource | Usually creates/causes state change |

---

# 42. PUT vs PATCH

## PUT

**Definition:**  
Usually represents replacing/updating a resource as a whole.

## PATCH

**Definition:**  
Used for partial modification of a resource.

Example:

PUT:

```json
{
    "name": "Laptop",
    "price": 50000,
    "category": "Electronics"
}
```

PATCH:

```json
{
    "price": 55000
}
```

### Simple

```text
PUT   → Full replacement/update
PATCH → Partial update
```

---

# 43. Authentication vs Authorization

## Authentication

**Definition:**  
Authentication verifies who the user is.

Example:

```text
Username
Password
OTP
JWT
```

---

## Authorization

**Definition:**  
Authorization determines what an authenticated user is allowed to do.

Example:

```text
Admin → Delete Product
User  → View Product
```

### Remember

```text
Authentication → Who are you?
Authorization  → What can you do?
```

---

# 44. What is JWT?

### Definition

**JWT stands for JSON Web Token. It is a compact token format commonly used to carry signed claims between parties.**

Typical flow:

```text
Login
  ↓
Username + Password
  ↓
Server validates
  ↓
JWT generated
  ↓
Client stores token
  ↓
Client sends token
  ↓
Server verifies token
```

JWT structure:

```text
Header.Payload.Signature
```

### Important

JWT is usually **signed**, not automatically encrypted.

---

# 45. What is Middleware?

### Definition

**Middleware is software that processes requests/responses as they pass through an application pipeline.**

Flow:

```text
Client
  ↓
Middleware
  ↓
Route
  ↓
Response
  ↓
Middleware
  ↓
Client
```

Uses:

- Logging
- Authentication checks
- CORS
- Timing
- Headers
- Request processing

---

# 46. What is Dependency Injection?

### Definition

**Dependency Injection is a design technique where required dependencies are provided to a component rather than the component creating them itself.**

Example:

```python
def get_service():
    return ProductService()
```

FastAPI:

```python
@app.get("/products")
def get_products(
    service = Depends(get_service)
):
    return service.get_all()
```

### Benefit

- Loose coupling
- Testability
- Reusability
- Easier maintenance

---

# 47. What is Repository Pattern?

### Definition

**Repository Pattern separates data-access logic from business logic.**

Architecture:

```text
Router
   ↓
Service
   ↓
Repository
   ↓
Database
```

Repository:

```python
class ProductRepository:

    def get_all(self):
        # database logic
        pass
```

Service:

```python
class ProductService:

    def __init__(self, repository):
        self.repository = repository
```

### Benefit

Database code एकाच layer मध्ये ठेवता येतो.

---

# 48. What is Service Layer?

### Definition

**Service Layer contains application/business logic.**

Example:

```text
Router
  ↓
ProductService
  ↓
ProductRepository
  ↓
MySQL
```

Service मध्ये:

- Validation
- Business rules
- Calculations
- Workflow
- Multiple repository operations

ठेवता येतात.

---

# 49. What is ORM?

### Definition

**ORM stands for Object-Relational Mapping. It maps programming language objects/classes to relational database tables.**

Without ORM:

```sql
SELECT * FROM products;
```

ORM style:

```python
Product.objects.all()
```

Popular Python ORM:

```text
SQLAlchemy
Django ORM
```

### Benefits

- Less SQL boilerplate
- Object-oriented database interaction
- Reusable models
- Easier relationships

---

# 50. What is CRUD?

### Definition

CRUD represents four basic database operations.

```text
C → Create
R → Read
U → Update
D → Delete
```

REST example:

```text
POST   → Create
GET    → Read
PUT/PATCH → Update
DELETE → Delete
```

---

# 🔹 SECTION 6 — FASTAPI

# 51. What is FastAPI?

### Definition

**FastAPI is a modern Python web framework for building APIs using Python type hints.**

Features:

- Type hints
- Validation
- Automatic OpenAPI
- Swagger UI
- Async support
- Dependency Injection
- High performance
- Pydantic integration

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello"}
```

---

# 52. What is Pydantic?

### Definition

**Pydantic is a Python library used for data validation and parsing using type annotations.**

Example:

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
```

Request:

```json
{
    "name": "Laptop",
    "price": 50000
}
```

Pydantic data validate/parse करण्यास मदत करतो.

---

# 53. What is BaseModel?

### Definition

`BaseModel` हा Pydantic चा base class आहे ज्याच्या माध्यमातून data models define करता येतात.

```python
from pydantic import BaseModel

class ProductCreate(BaseModel):

    name: str
    price: float
```

हे model:

- Validation
- Parsing
- Serialization

साठी उपयोगी आहे.

---

# 54. What is Field?

### Definition

`Field()` Pydantic model fields साठी additional validation/configuration define करण्यासाठी वापरतो.

Example:

```python
from pydantic import BaseModel, Field

class Product(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=100
    )

    price: float = Field(
        gt=0
    )
```

### Meaning

```text
min_length=2
→ कमीत कमी 2 characters

max_length=100
→ maximum 100 characters

gt=0
→ greater than 0
```

---

# 55. What is APIRouter?

### Definition

**APIRouter is used to organize and modularize FastAPI route definitions.**

Example:

```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/products",
    tags=["Products"]
)
```

Route:

```python
@router.get("/")
def get_products():
    return []
```

Main app मध्ये:

```python
app.include_router(router)
```

### Benefit

Large project मध्ये routes separate files मध्ये ठेवता येतात.

---

# 56. What is `Depends()`?

### Definition

`Depends()` FastAPI मध्ये dependency injection साठी वापरतो.

Example:

```python
from fastapi import Depends

def get_service():
    return ProductService()


@app.get("/products")
def get_products(
    service = Depends(get_service)
):
    return service.get_all()
```

### Uses

- Database session
- Service
- Authentication
- Current user
- Common validation
- Shared logic

---

# 57. What is HTTPException?

### Definition

`HTTPException` API मध्ये HTTP error response generate करण्यासाठी वापरतो.

Example:

```python
from fastapi import HTTPException

if product is None:

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
```

Response:

```json
{
    "detail": "Product not found"
}
```

---

# 58. What are `async` and `await`?

## `async`

Coroutine function define करते.

```python
async def get_data():
    pass
```

## `await`

Async operation ची result येईपर्यंत current coroutine suspend करते.

```python
async def get_data():
    result = await fetch_data()
    return result
```

### Important

`async` वापरल्यामुळे प्रत्येक code automatically faster होत नाही.

Async विशेषतः I/O-bound/high-concurrency workloads मध्ये useful आहे.

---

# 59. Middleware in FastAPI

FastAPI मध्ये middleware request/response processing साठी वापरू शकतो.

Example:

```python
@app.middleware("http")
async def log_requests(request, call_next):

    response = await call_next(request)

    return response
```

Flow:

```text
Request
   ↓
Middleware
   ↓
Route
   ↓
Response
   ↓
Middleware
   ↓
Client
```

---

# 60. Swagger / OpenAPI

## OpenAPI

**Definition:**  
OpenAPI is a standard specification for describing HTTP APIs.

FastAPI OpenAPI schema automatically generate करते.

## Swagger UI

Interactive API documentation interface.

Usually:

```text
/docs
```

FastAPI application मध्ये Swagger UI accessible असते.

Alternative documentation:

```text
/redoc
```

### Benefit

Frontend developer किंवा tester browser मधून API test करू शकतो.

---

# 🔹 SECTION 7 — DJANGO

# 61. What is Django?

### Definition

**Django is a high-level Python web framework designed for building web applications quickly and securely.**

Features:

- ORM
- Authentication
- Admin
- URL routing
- Templates
- Forms
- Middleware
- Security features
- Scalable architecture

---

# 62. What is MVT?

Django commonly **MVT — Model View Template** architecture वापरतो.

### Model

Database/data layer.

### View

Request handling/business flow.

### Template

Presentation/UI layer.

Flow:

```text
User
 ↓
URL
 ↓
View
 ↓
Model
 ↓
Database
 ↓
View
 ↓
Template
 ↓
User
```

---

# 63. What is Model?

### Definition

**A Django Model is a Python class that represents data structure and is mapped to database tables through Django ORM.**

Example:

```python
class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.FloatField()
```

Database table generate करण्यासाठी migrations वापरतात.

---

# 64. What is View?

### Definition

**A Django View is code that receives a request and returns a response.**

Example:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello")
```

View:

```text
Request
 ↓
View
 ↓
Response
```

---

# 65. What is Template?

### Definition

**A Django Template is a presentation file used to generate dynamic HTML.**

Example:

```html
<h1>Hello {{ name }}</h1>
```

Django template engine variable render करू शकतो.

---

# 66. What is Django ORM?

### Definition

**Django ORM allows developers to interact with relational databases using Python objects and query methods instead of writing raw SQL for every operation.**

Example:

```python
Product.objects.all()
```

Filter:

```python
Product.objects.filter(price__gt=1000)
```

Get:

```python
Product.objects.get(id=1)
```

---

# 67. What is Migration?

### Definition

**Migration is Django's mechanism for tracking and applying database schema changes based on model changes.**

Commands:

```bash
python manage.py makemigrations
```

नंतर:

```bash
python manage.py migrate
```

### Difference

```text
makemigrations
→ Migration files तयार करतो

migrate
→ Database मध्ये changes apply करतो
```

---

# 68. What is Middleware in Django?

### Definition

**Django middleware is a layer of hooks that processes requests and responses globally or across selected request processing stages.**

Uses:

- Authentication
- Security
- Sessions
- Logging
- Custom request processing

Flow:

```text
Request
 ↓
Middleware
 ↓
View
 ↓
Middleware
 ↓
Response
```

---

# 69. What is Django Admin?

### Definition

**Django Admin is a built-in administrative interface for managing application data through registered models.**

Example:

```python
from django.contrib import admin
from .models import Product

admin.site.register(Product)
```

Admin site वर Product manage करता येतो.

### Benefits

- Quickly manage database records
- CRUD operations
- User management
- Internal administration

---

# 70. What is DRF?

### Full Form

**DRF = Django REST Framework**

### Definition

**Django REST Framework is a powerful toolkit for building Web APIs with Django.**

---

## DRF Important Components

### 1. Serializer

**Definition:**  
Serializer converts/validates complex data such as model instances into representations such as JSON and can also validate incoming data.

Example:

```python
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
```

---

### 2. APIView

Class-based API endpoint.

```python
class ProductAPIView(APIView):

    def get(self, request):
        ...
```

---

### 3. Generic Views

Common CRUD patterns quickly implement करण्यासाठी.

Examples:

```text
ListAPIView
CreateAPIView
RetrieveAPIView
UpdateAPIView
DestroyAPIView
```

---

### 4. ViewSet

Related CRUD operations एका class मध्ये organize करता येतात.

```python
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

---

### 5. Router

ViewSet साठी URLs automatically generate करण्यास मदत.

```python
router.register(
    "products",
    ProductViewSet
)
```

---

### 6. Authentication

DRF मध्ये authentication methods:

```text
SessionAuthentication
BasicAuthentication
TokenAuthentication
JWT-based authentication
```

---

### 7. Permissions

User ला API access आहे की नाही ते control करतात.

Examples:

```text
AllowAny
IsAuthenticated
IsAdminUser
```

Custom permissions सुद्धा बनवता येतात.

---

### 8. Pagination

Large data छोटे pages मध्ये return करण्यासाठी.

Example:

```text
/products?page=1
/products?page=2
```

---

### 9. Filtering

Data specific criteria नुसार filter करण्यासाठी.

Example:

```text
/products?category=mobile
```

---

# 🔥 70 Questions — One-Line Revision

Interview आधी हे quick revision कर:

```text
1. Python       → High-level, general-purpose language
2. Features     → Simple, dynamic, object-oriented, ecosystem
3. Interpreted  → Source → bytecode → runtime execution
4. Dynamic type → Type determined at runtime
5. Mutable      → Can change after creation
6. List/Tuple   → Mutable vs immutable
7. Set/Dict     → Unique values vs key-value pairs
8. is/==        → Identity vs equality
9. args/kwargs  → Positional tuple vs keyword dictionary
10. break/etc   → Stop / skip / do nothing

11. Function     → Reusable code block
12. Parameter    → Definition variable
13. Return       → Sends value to caller
14. Lambda       → Anonymous small function
15. Recursion    → Function calls itself
16. Scope        → Variable accessibility
17. LEGB         → Local, Enclosing, Global, Built-in

18. Class        → Blueprint
19. Object       → Class instance
20. self         → Current instance
21. Instance var → Object-specific
22. Class method → Class-level method
23. Inheritance  → Reuse parent functionality
24. Polymorphism → Same interface, different behavior
25. Encapsulation → Bundle/control state
26. Abstraction  → Hide implementation
27. Overriding   → Child replaces parent method
28. Multiple inh → Multiple parent classes

29. Iterator     → Produces items one by one
30. Generator    → Lazy iterator
31. yield        → Produces value and suspends state
32. Decorator    → Extends behavior
33. Context mgr  → Setup + cleanup
34. Copy         → Shallow vs deep
35. GC           → Reclaims unused memory
36. GIL          → CPython bytecode execution lock
37. Thread       → Lightweight execution unit
38. Async        → Concurrent I/O using event loop

39. API          → Software communication interface
40. REST         → Resource-oriented HTTP API style
41. GET/POST     → Retrieve/create
42. PUT/PATCH    → Full/partial update
43. AuthN/AuthZ  → Who are you / what can you do
44. JWT          → Signed token format
45. Middleware   → Request/response pipeline
46. DI           → Inject dependencies
47. Repository   → Data access abstraction
48. Service      → Business logic
49. ORM          → Object-database mapping
50. CRUD         → Create, Read, Update, Delete

51. FastAPI      → Python API framework
52. Pydantic     → Validation/parsing
53. BaseModel    → Pydantic data model
54. Field        → Field constraints/configuration
55. APIRouter    → Route organization
56. Depends      → Dependency injection
57. HTTPException → API error response
58. async/await  → Async programming
59. Middleware   → Cross-cutting request/response logic
60. OpenAPI      → API specification

61. Django       → Python web framework
62. MVT          → Model View Template
63. Model        → Data/database representation
64. View         → Request/response logic
65. Template     → Presentation
66. ORM          → Database abstraction
67. Migration    → Schema change management
68. Middleware   → Request/response hooks
69. Admin        → Built-in management UI
70. DRF         → Django API toolkit
```

## 🎯 Interview मध्ये उत्तर देण्याचा Best Format

प्रत्येक technical question साठी हा format वापर:

**1. Definition → 2. Simple Explanation → 3. Example → 4. Real-world use → 5. Difference/Important point**

उदा. **Dependency Injection** विचारले तर:

> **Definition:** Dependency Injection is a design technique where dependencies are provided to a component instead of being created inside it.  
>
> **Simple Explanation:** म्हणजे class ने स्वतः dependency create करण्याऐवजी ती बाहेरून receive करणे.  
>
> **Example:** FastAPI मध्ये `Depends()` वापरून service किंवा database dependency inject करता येते.  
>
> **Benefit:** Loose coupling, easy testing आणि maintainability.

अशा प्रकारे उत्तर दिल्यास **फक्त definition पाठ केलेली नसून concept समजलेला आहे** हे interviewer ला दिसते.

