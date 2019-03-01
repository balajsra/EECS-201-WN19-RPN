#!/usr/bin/env python3

import math

def calculate(expression):
    if expression in ["quit", "q", "exit"]:
        exit()

    stack = expression.split()
    
    result = 0
    
    operation = stack.pop()
    a = 0
    b = 0

    if len(stack) == 1:
        a = float(conv_const(stack.pop()))

        if operation == "!":
            result = factorial(a)
        elif operation == "~":
            a = int(a)
            
            result = ~a

    elif len(stack) == 2:
        if operation in ["+", "-", "*", "/", "%",
        "^", "//", "&", "|", "<<", ">>"]:
            b = float(conv_const(stack.pop()))
            a = float(conv_const(stack.pop()))

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
            elif operation == "&":
                a = int(a)
                b = int(b)

                result = a & b
            elif operation == "|":
                a = int(a)
                b = int(b)

                result = a | b
            elif operation == "<<":
                a = int(a)
                b = int(b)

                result = a << b
            elif operation == ">>":
                a = int(a)
                b = int(b)

                result = a >> b
        elif operation in ["cos", "sin", "tan"]:
            angle = stack.pop()
            a = float(conv_const(stack.pop()))

            if angle == "deg":
                a = math.radians(a)
            
            if operation == "cos":
                result = math.cos(a)
            elif operation == "sin":
                result = math.sin(a)
            elif operation == "tan":
                result = math.tan(a)
        elif operation in ["acos", "asin", "atan"]:
            angle = stack.pop()
            a = float(conv_const(stack.pop()))

            if operation == "acos":
                result = math.acos(a)
            elif operation == "asin":
                result = math.asin(a)
            elif operation == "atan":
                result = math.atan(a)
            
            if angle == "deg":
                result = math.degrees(result)

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


def conv_const(string):
    if string == "pi":
        return math.pi
    elif string == "e":
        return math.e
    else:
        return string


if __name__ == '__main__':
    main()
