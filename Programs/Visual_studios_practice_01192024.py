"""
The following notes come from w3Schools.com Python tutorial

"""
print("Hello, World!")


if 5 > 2:
    print("Five is greater than two!")

if 5> 2:
    print("Five is live!")

x = 5
y = "Hello, World!"

print(x)
print(y)

# This is a comment 

# This is a multiline
# Comment

""" 
(open and closed triple quotes)
This is also a multi-line comment 
since Python ignors strings that are not assigned a variable.

"""

# In Python, variables are created when you assign a value to it.
# It is not necessary to declare a variable

x = 5 # The variable is x and the value assigned to the variable is 5
y = "John" # The variable is y and the value assinged to the variable is the string John
print(x)
print(y)


# Casting is when a variable type is specified before the assigned value
x = str(3) # The value will print as a string '3'
y = int(3) # The value will print with a data type of integer 3
z = float(3) # The value will print with a data type of float 3.0

print(x, y, z)

#To get the data type of a variable, you can use the type() function
x = 5
y = "Felicia"
print(type(x))
print(type(y))

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-a, 0-9, and _)
Variable names are case-sensitive
Variable names cannot be any of the Python keywords

"""

# Pytho allows you to assign values to multiple variables in one line
x, y, z, = "Cordell", "Felicia", "Christina"
print("x is", x, " y is ", y, "and z is ", z)

# You can also assign the same value to multiple variables
x = y = z = "Orange"
print("1 ", x, ", 2 ", y, ", 3", z )

# If you have a collection of values in a list tuple, etc. Python allows you to extract the values into variables.  This is called unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)

# List are used to store multiple items in a single variable
thislist = ["school", "work", "hobby"]
print(thislist)

# To determine how many items a list has, use the len() function
print(len(thislist))

# A list can contain different data types
list1 = ["Exercise", 4, True, "date"]
print(list1)

# To Access items in a list, reer to the index number
print(thislist[1])

# Negative indexing a list from the end
print(thislist[-2])

# Accessing a range of indexes by specifying where to start and where to end the range. This will accessing the beginning of the list to index 1
print(thislist[:1])

# Tuples also store multiple items in a single variable.  Other data types in Python that store collections of data are Set, Dictionary, and of course, List
mytuple = ("apple", "banana", "orange")
print(mytuple)

# Tuple can have one item. Just make sure to follow the item with a comma
yourtuple = ("scarf",)
print(yourtuple)
print(len(yourtuple))

# A tuple() constructor is created when the type is declared or casted before the data's values
a_tuple = tuple(("water", "gas", "heat")) # double parentheses must be used
print(a_tuple)
print(type(a_tuple))
print(len(a_tuple))

# You access tuple items by refering to the index number inside square brackets
print(a_tuple[1])

# Check if an item is present in the tuple
if "water" in a_tuple:
    print("Yes, 'water' is in the a_tuple")

print("")
print("")

#Convert the tuple into a list
c_A_tuple = ("students", "teachers", "citizens")
print(c_A_tuple)
print(type(c_A_tuple))
b_A_list = list(c_A_tuple)
print(b_A_list)
print(type(b_A_list))

#Convert the list to a tuple
is_A_list = ["Monday", True, 5]
print(is_A_list)
print(type(is_A_list))

is_A_tuple = tuple(is_A_list)
print(is_A_tuple)
print(type(is_A_tuple))

# You can loop through the tuple items by using a for loop
tuple_loop = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
for x in tuple_loop:
    print(x)

print("")
for i in range(len(tuple_loop)):
    print(tuple_loop[i])

# You can use a while loop to loop through a tuple
# by referring to the length of the indexes in the tuple
while i < len(tuple_loop):
    print(tuple_loop[i])
    i = i + 1

# The index() function searches a collection of data and returns the position
# of index where the value is found
print(tuple_loop.index("Wednesday"))

# A dictionary in Python is a key:value pair collection of data
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
