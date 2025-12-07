import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calc():
    print(art.logo)
    f_number = float(input("What's the first number?: "))
    keep_calculating = True
    while keep_calculating:
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation: ")
        s_number = float(input("What's the second number?: "))
        f_result = operations[operator](f_number, s_number)
        print(f"{f_number} {operator} {s_number} = {f_result}")
        keep = input(f"Type 'y' to continue calculating with {f_result}, or type 'n' to start a new calculation:").lower()
        if keep == "y":
            f_number = f_result
            print(f_number)
        else:
            keep_calculating = False
            calc()
calc()
