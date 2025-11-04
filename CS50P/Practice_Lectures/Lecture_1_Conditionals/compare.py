                   
                    #========== CONDITIONALS =============


# USe of if/else/elif/ conditions


first_number = int(input("What is the value of first Number?: "))
second_number = int(input("What is the value of second number?: "))

"""

if first_number > second_number:
    print(f"The first number {first_number} is greater than the Second number {second_number}")

elif first_number < second_number :
    print(f"The Second number {second_number} is greater than the first number {first_number}")

 # else catches all remaining cases after if/elif conditions are checked
 # when the thing is obvious and we don't add any condition we use else. 
else: 
    print(f"First number {first_number} is equal to the Second number {second_number}")

"""


# Use of "OR" and "AND"

# OR = True if at least one condition is True among  all of the conditions.

"""

if first_number > second_number or first_number < second_number :
    print(f"First number {first_number} is not equal to Second number {second_number}")

else:
    print(f"First number {first_number} is equal to the Second number {second_number}")

"""

# We can optimize same code more efficiently by asking less question. 
# Optimization: Using != is more efficient than checking both > and <
# Or by adding less conditions

if first_number != second_number:
    print(f"First number {first_number} is not equal to the second number {second_number}")

else:
    print(f"First number {first_number} is equal to the second number {second_number}")