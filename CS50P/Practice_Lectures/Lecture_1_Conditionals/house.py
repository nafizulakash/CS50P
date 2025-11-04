
# USE OF "MATCH" keyword



name = input("What's your name? ").capitalize()

match name:
    case "Akash" | "Nafizul": # here "|" works as or. also compiles 2 match conditions with same outcome
        print(f"{name} is from Manikganj.")

    # case "Nafizul":
    #     print(f"{name} is from Manikganj.")

    case "Saif":
        print(f"{name} is from Chuadanga.")

    case "Saad":
        print(f"{name} is from Dinajpur.")

    case _: # "Case _:" works as "else" from if/else and will handle all undefined input
        print(f"{name} who?")


# Match with boolean operator. 
# We need to calculte boolean before to work in match operator

"""

number = int(input("Any number: "))
is_even = (number % 2 == 0)

match is_even:
    case True:
        print("even")
    case False:
        print("odd")

"""