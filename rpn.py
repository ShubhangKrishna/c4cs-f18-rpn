#!/usr/bin/env python3
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
            if token=='+':

                stack.append((val1+val2)) 
            elif token == '-':
                stack.append((val1-val2))
            elif token == '*':
                stack.append((val1*val2)) 
            elif token == '/':
                stack.append((val1/val2)) 
            
            return stack[0]
        
    pass
def main():
    while True:
       print( calculate (input('rpn calc> ')) )

if __name__== '__main__':
    main()

