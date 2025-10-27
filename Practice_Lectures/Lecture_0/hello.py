#Say hello to the world
"""
print("hello, world")

"""
#Ask user for their name
"""
name = input("What's your name? ")
"""

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
# f is formatted string. 
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

"""
address = input ("Where are you from: ").strip().title()
print(f"I am from {address}")

"""

#split string

"""
name = input("What's your name? ").strip().title()

first, last = name.split()

print(f"Hello {first}")
print(f"Hey {last}")

"""


                          # ==== function ====

# how to create a function
# how to pass/ set parameter to a function
# Scope of veriable (local, global)

"""

def hello (to = "World"): # Setting a default value to the parameter if any value is not passed
    print(f"Hello, {to}")

hello()
name = input("What is your name ?: ")
hello(name)

"""

# We need to define a function before calling it. 
# but ina project we might need to use so many function. 
# so the code might look like def, def, def def,. 
# so instead we define the main function first and 
# the other necessey funtion later based on our need.
# and we call the main funtion at the very end of the code

"""

def main ():
    name1 = input ("What is your name2? : ") # local veriable
    hello(name1, name2)
    
name2 = input ("What is your name1? : ") # Global veriable

def hello(to,x):
    print(f"Hello, {to},{x}")
    
main()
"""


                          # ==== Recursion ====

#recursive function calls it self 
#Eventually Python will throw a RecursionError 
# when the maximum recursion depth is reached (~1000 by default).

"""

def main ():
    name1 = input ("What is your name2? : ") # local veriable
    hello(name1, name2)
    main()
    
name2 = input ("What is your name1? : ") # Global veriable

def hello(to,x):
    print(f"Hello, {to},{x}")
    
main()

"""


# How to use  "Return" in function

def main ():
    x = int(input("What is the value of X?: "))
    print(f"The squared value of x is: {square(x)}")

def square(n):
    return n * n
    """
    return n**2  # we can use this 2 method also for square 
    return pow (n,2)
    """
    

main()







