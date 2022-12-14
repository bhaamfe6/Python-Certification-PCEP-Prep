# Python Tools

## Python Data Types

--- 
| Text Type:      | str                  | string       |
| :---            | :---                 | :---         |
| Boolean Type:   |  bool                | True or False         |
| Numeric Type:   |  int, float, complex | numbers      |
| Binary Types:   | bytes, bytearray, memoryview | binary memory         |
| Sequence Types: | list, tuple, range   | ordered data | 
| Mapping Type:   | dict                 | dictionary   |  
|Set Types:       | set, frozenset       | unordered data |
| None Type:      | NoneType             |   


---

**Specifying a variable type can be done by casting**

Casting is done using constructor functions:
- int() : constructs an integer number from an integer literal, a float literal (by removing all decimals), or string literal (providing the string represents a whole number).
- float() : constructs a float number from an integer literal
- str() : constructs a string from a wide variety of data types.

Example of integer casting<br>
![example of integer casting](image/integer_casting.png)

Example of float casting<br>
![example of float casting](image/float_casting.png)

Example of string casting<br>
![example string casting](image/string_casting.png)


## Stored Collections of Data


---
| List     | ordered, changeable, indexed, and allow duplicate values  | created with []      |
|:---      | :--- | :--- |
| Tuples   | ordered, unchangeable, indexed, and allow duplicates values | created with ()      |
| Set      | unordered, unchangeable, and unindexed | created with {}     |
| Dictionary | ordered, changeable and do not allow duplicates | store in `key:value` pairs     |
---

Example of syntax for a List.<br>
![example of a list](image/list_example.png)<br>

Example of syntax for a Tuple.<br>
![example of a tuple](image/tuple_example.png)<br>

Example of syntax for a Set.<br>
![example of a set](image/set_example.png)<br>

Example of syntax for a Dictionary.<br>
![example of a dictionary](image/dictionary_example.png)<br>

# Python Conditions and If Statements

Logical conditions from mathematics:
- Equals: a == b
- Not Equals: a!= b
- Less than: a < b
- Greater than: a > b
- Greater than or equal to: a >= b

If statements use the if keyword.
<br>
![Example of `if` statement](image/if_statement_example.png)<br>

This is the outcome of the if statement example.<br>
![if statement outcome](image/outcome_of_if_statement.png)<br>

The `elif` keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

Example of elif syntax.<br>
![example of elif syntax](image/elif_example.png)<br>

The `else` keyword ends the the `if`, `elif`, `else` loop. 

Example of Else syntax.<br>
![example of else syntax](image/else_example.png)<br>

## Python Loops

Python has two primitive loop commands:
- while loops
- for loops

While loops execute a set of statements as long as the condition is met.

Example of while loop.<br>
![while loop syntax](image/while_loop_example.png)<br>

**The break Statement**

The `break` statement stops the loop even if the while condition is true.

Use of break statement.<br>
![use of break statement](image/break_statement.png)<br>

## Python for Loops

A `for` loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

Example of for loop.<br>
![exmple of for loop](image/for_loop.png)<br>

The break statement can stop a for loop as well.


