from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract,
              "*": multiply, "/": divide }


def calculator():
    print(logo)
    first_number = float(input("Enter first number: "))

    should_accumulate = True
    while should_accumulate:
        for key in operations:
            print(f"{key}")
        sign = input("Pick an operation: ")

        second_number = float(input("Enter second number: "))

        result = operations[sign](first_number, second_number)

        print(f"{first_number} {sign} {second_number} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, "
                       f"or type 'n' to start a new calculation: ")

        if choice == "y":
            first_number = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()