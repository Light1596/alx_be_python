num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

symbol = input("Choose the operation (+, -, *, /): ")

match symbol:
    case "+":
        print(f"The result is {num1 + num2}")

    case "-":
        print(f"The result is {num1 - num2}")

    case "*":
        print(f"The result is {num1 * num2}")

    case "/":
        print(f"The result is {num1 / num2}")

    case _:
        print("Please choose from one of the operators above")

