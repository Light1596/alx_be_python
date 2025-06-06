def perform_operation(num1, num2,operation):
     """
    Performs an arithmetic operation.
    Args:
        num1 (int/float): The first number.
        num2 (int/float): The second number.
        operation (str): The operation to perform ('add', 'subtract', etc.).
    """
    match operation:
        case 'add':
            return num1 + num2

        case 'subtract':
            return num1 - num2

        case 'multiply':
            return num1 * num2

        case 'divide':
            return num1 / num2
