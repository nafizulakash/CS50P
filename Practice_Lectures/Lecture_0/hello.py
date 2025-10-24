#Say hello to the world
print("hello, world")

#Ask user for their name
name = input("What's your name? ")

#Say hello to user

"""print("Hello, " + name)
print("Hi,",name)"""

#format string
#If we put an f before quotes
#we can directly insert variables inside {} within the string.
"""

print(f"Hello, {name}")

"""

# We can use """  """ for multi line comment. 
# In between whatever we write will be counted as comment in python.
"""
print("Hello Nafiz")

"""

#Print function end line by default. 
#(end = "\n")---> is set to by default 
"""print("Hello")
print(name)"""

#override the value of function end 
#not end line (\n) by default.
#Or change function default end parameter
"""print("Do not create a line by default: ")
print("Hello ", end="")
print(name) """

#override the value of sep in print function

"""
print("Hello", name, sep = "???")

"""

#2 types of parametere. 
# 1. Named Parameter(end=" ", sep=" " ) 
# 2. Posetional parameter(our normal parameters)

# print " " or ' '
# \ work as escape charecter

"""
print('Hello "Friend"', name)
print('Hello \"My Friend\"', name)

"""



# Remove white space from string. 
# IF user press a lot of spaces unintentionally 
"""
name = name.strip()
"""

# Capitalized very first letter of string
"""
name = name.capitalize()
print(f"Hello, {name}")
"""

# Capitalize first latter of each word

"""
name = name.title()
print(f"Hello, {name}")
"""

# We can chain method togatehr

# Remove white spaces and Capitalized

"""
name = name.strip().title()
print(f"Hello, {name}")

"""


# We can even do it while taking input

address = input ("Where are you from: ").strip().title()
print(f"I am from {address}")

