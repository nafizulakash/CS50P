"""

number = int(input("Input a number: "))

if number % 2 == 0:
    print(f"{number} is an even number")

else:
    print(f"{number} is an odd number")

"""

                      #======== BOOLEAN ============

# Boolean is a data type.
#Boolean Data Type:
#Represents truth values: True or False 
#Used for logical operations and conditions

def main():
    number = int(input("Input a number: "))

    if is_even(number):
        print(f"{number} is an even number.")
    
    else:
        print(f"{number} is an odd number.")


def is_even(n):

    # if n % 2 == 0:
    #     return True # While asking for boolean return "True" or "False" must be capitalized.
    
    # else:
    #     return False
# We can optimize it bt reducing the lines

    # return True if n % 2 == 0 else  False

# More optimized versiont. As it is a boolean condition with will return yes/no or true/ false by default
# n % 2 == 0 already evaluates to True or False, so we can return it directly

    return n % 2 == 0    


main()