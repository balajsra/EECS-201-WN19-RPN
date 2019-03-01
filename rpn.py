#!/usr/bin/env python3


def calculate(expression):
    if expression in ["quit", "q", "exit"]:
        exit()

    stack = expression.split()
    
    result = 0
    
    operation = stack.pop()
    a = 0
    b = 0

    if len(stack) == 1:
        a = float(stack.pop())

        if operation == "!":
            result = factorial(a)

    elif len(stack) == 2:
        b = float(stack.pop())
        a = float(stack.pop())

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            result = a / b
        elif operation == "%":
            result = a * (b / 100)
        elif operation == "^":
            result = a ** b
        elif operation == "//":
            result = a // b

    return result


def main():
    stack = []
    
    while True:
        expression = input("rpn calc> ")

        print(calculate(expression))


def factorial(num):
    if (num == 0) or (num == 1):
        return 1
        
    return num * factorial(num - 1)
        

if __name__ == '__main__':
    main()
