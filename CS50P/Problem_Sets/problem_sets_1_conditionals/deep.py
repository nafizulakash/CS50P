def greatest_question():
    question = input("What is the Great Question of Life, the Universe and Everything? ").strip().lower()
# "Lower ()" - turns everything into lowercase letter. To make everything case insesitive
# "strip()" - user might add white space before of after by mistake

    match question:
        case "42" | "forty-two" |  "forty two":
            print("Yes")
        case _:
            print("No")

greatest_question()