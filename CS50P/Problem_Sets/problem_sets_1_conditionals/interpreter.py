def interpreter():
    arithmatic =input("Enter an arithmatic expression(1 + 1): ").strip()

    x, y, z= arithmatic.split()

    x = float(x)
    z = float(z)

    if y == "+":
        sum = float(x + z)
        print(f"{sum:.1f}")

    elif y == "-":
        sub = float(x - z) 
        print(f"{sub:.1f}")

    elif y == "*" or y == "x":
        multi = float(x * z)
        print(f"{multi:.1f}")

    elif y == "/":
        div = float(x / z)
        print(f"{div:.1f}")


interpreter()