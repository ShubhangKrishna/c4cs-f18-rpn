#!/usr/bin/env python3

import operator
import math 

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.__pow__,
    'A': operator.__and__,
    'V': operator.__or__,
    'N': operator.__not__,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'pi': math.pi,
    'e': math.exp,
    '//': operator.__floordiv__,

}

def calculateR(myarg):
    stack = list()
    for token in myarg.split():
        try:
            if (token=='pi'):
                token=math.pi
            elif (token=='e'):
                token=math.exp    
            token = float(token)
            stack.append(token)
        except ValueError:
            if len(token) != 3:
                function = operators[token]
                arg2 =float(stack.pop())
                arg1 =float(stack.pop())
                result = function(arg1, arg2)
                stack.append(result)

            else: 
                function = operators[token]
                arg1= stack.pop()
                result = function(math.radians(arg1))
                stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def calculateL(myarg):
    stack = list()
    for token in myarg.split():
        try:
            if (token=='pi'):
                token=math.pi
            elif (token=='e'):
                token=math.exp
            token = int(token)
            stack.append(token)
        except ValueError:
            if len(token) != 3:
                function = operators[token]
                arg2 =int(stack.pop())
                arg1 =int(stack.pop())
                result = function(arg1, arg2)
                stack.append(result)

            else:
                function = operators[token]
                arg1= stack.pop()
                result = function(math.radians(arg1))
                stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def calculateD(myarg):
    stack = list()
    for token in myarg.split():
        try:
            if (token=='pi'):
                token=math.pi
            elif (token=='e'):
                token=math.exp
            token = float(token)
            stack.append(token)
        except ValueError:
            if len(token) != 3:
                function = operators[token]
                arg2 =float(stack.pop())
                arg1 =float(stack.pop())
                result = function(arg1, arg2)
                stack.append(result)
            else:
                function = operators[token]
                arg1= float(stack.pop())
                result = function(math.radians(arg1* (math.pi/180)))
                stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    
    while True:
        k=input("Degree or Radian or Logical ?(1/2/3)> ")
        if k==1: 
            result = calculateD(input("rpn calc> "))
            print("Result: ", result)
        elif k==2: 
            result = calculateR(input("rpn calc> "))
        else: 
            result=calculateL(input("rpn calc> "))
if __name__ == '__main__':
    main()
