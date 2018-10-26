#!/usr/bin/env python3
import operator
op = {
        '+': operator.add ,
        '-': operator.sub, 
        '*':operator.mul,
        '/':operator.floordiv
}
def calculate(arg):
    #stack for the calculator 
    # take input and tokenize it 
    #process tokens 
    stack =[]
    tokens = arg.split()
    for token in tokens:
        try: 
            value= int (token)
            stack.append(value)
        except ValueError:
            val1=stack.pop()
            val2=stack.pop()
            func = op[token]
            stack.append(func(val1,val2))          
            return stack[0]
        
    pass
def main():
    while True:
       print( calculate (input('rpn calc> ')) )

if __name__== '__main__':
    main()

