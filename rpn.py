#!/usr/bin/env python3


def calculate(expression):
    if expression in ["quit", "q", "exit"]:
        exit()

    stack = expression.split()

    operation = stack.pop()
    b = float(stack.pop())
    a = float(stack.pop())

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
