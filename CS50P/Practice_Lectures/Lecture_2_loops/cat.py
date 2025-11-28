                                       #=========== LOOPS ===========# 
# While loops
"""
i = 3


while i != 0:
    print(f"Meow")
    i = i - 1

"""

# same problem diffrent solution

"""
i = 0

while i < 3:
    print("Meow")
    #i = i + 1
    i += 1

    
    
"""

# For loops
"""
for i in [0, 1, 2]:
    print("Meow")

"""
#  diffrent answer
"""
for i in range(3):
    print("Meow")

    
"""
# In python if a situation arrive where 
# we need to use a variable in order to the 
# code to run but i won't use it again.
#  we can use "-" instead of the variable.
"""
for _ in range(3):
    print("Meow")

    
"""
# meow 3 times
"""
print("Meow \n" * 3,end = "") # I didn't know this before that this is possible in python. 

"""
# better approach

"""
while True: # infinine while look for something if we need toask that same thing again and again untill we get expected answer.
     n = int(input("What is n: "))

     if n > 0:
          break
     
for _ in range (n):
     print("Meow")

     
"""

# let's do it using function

def main ():
    number = get_number()
    meow(number)

def get_number():

    while True: 
     n = int(input("What is n: "))

     if n > 0:
          return n

def meow(n):
    for _ in range (n):
     print("Meow")


main()