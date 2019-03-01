#!/usr/bin/env python3

def calculate(expression):
    stack = expression.split()

    a = stack.pop()
    b = stack.pop()
    operation = stack.pop()

    result = 0

    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        result = a / b

    return result


def main():
    stack = []
    
    while True:
        expression = input("rpn calc> ")

        print(calculate(expression))


if __name__ == '__main__':
    main()
