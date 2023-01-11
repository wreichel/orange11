def sum(a, b) -> float:
    return a + b


def sub(a, b) -> float:
    return a - b


def mul(a, b) -> float:
    return a * b


def div(a, b) -> float:
    return a / b


def get_calculation(operation, a, b) -> float:
    if operation == "+":
        return sum(a, b)
    elif operation == "-":
        return sub(a, b)
    elif operation == "*":
        return mul(a, b)
    elif operation == "/":
        return div(a, b)
