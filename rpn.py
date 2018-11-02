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
    stack =arg.split()
    while len(stack)>1:
        token=stack.pop()
        try: 
            value= int (token)
            stack.append(value)
        except ValueError:
            val1=int(stack.pop())
            val2=int(stack.pop())
            func = op[token]
            stack.append(str(func(val1,val2)))          
    return int(stack[0])
        
    pass
def main():
    while True:
       print( calculate (input('rpn calc> ')) )

if __name__== '__main__':
    main()

