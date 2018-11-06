from Tkinter import *
from rpnfgui import calculate 
calculator = Tk()
calculator.title('Calcualtor')
calculator.geometry('250x319')

screen = Frame(calculator, bd=2, width=300, height=325,bg='LightCyan')
buttons = Frame(calculator, bd=2, width=300, height=325,bg='honeydew2')
screen.grid(column=0, row=0, padx=25, pady=25)
buttons.grid(column=0, row=1, padx=25)
numbers=["7", "4", "1", "8", "5", "2", "9", "6", "3"]
def calc():

    r=results.get()
    results.delete(0,END)
    s=""
    for i in r: 
        temp=str(i)
        s=s+temp
    ans=calculate(s)
    results.insert(0,ans)
def appear1():
    results.insert(END, "1")
    return
def appear2():
    results.insert(END, "2")
    return
def appear3():
    results.insert(END, "3")
    return
def appear4():
    results.insert(END, "4")
    return
def appear5():
    results.insert(END, "5")
    return
def appear6():
    results.insert(END, "6")
    return
def appear7():
    results.insert(END, "7")
    return
def appear8():
    results.insert(END, "8")
    return
def appear9():
    results.insert(END, "9")
    return
def appear0():
    results.insert(END, "0")
    return
def appearADD():
    results.insert(END, "+")
    return
def appearSUB():
    results.insert(END, "-")
    return
def appearDIV():
    results.insert(END, "/")
    return
def appearMUL():
    results.insert(END, "*")
    return
def clear():
    results.delete(0,END)
    return
def space():
    results.insert(END," ")
    return 
def appearpow():
    eruslts.insert(END,"^")
    return 
#Button(buttons, bg="White", text=numbers[index], width=5, height=2, appear).grid(padx=5, pady=5, row=index%3, column=index/3)
Button(buttons, text = '1',bg='LightCyan',font='Helvetica 16 bold ',command=appear1).grid(row = 1, column = 0)
Button(buttons, text = '2',bg='LightCyan',font='Helvetica 16 bold ',command=appear2).grid(row = 1, column = 1)
Button(buttons, text = '3',bg='LightCyan',font='Helvetica 16 bold ',command=appear3).grid(row = 1, column = 2)
Button(buttons, text = '4',bg='LightCyan',font='Helvetica 16 bold ', command=appear4).grid(row = 2, column = 0)
Button(buttons, text = '5',bg='LightCyan',font='Helvetica 16 bold ',command=appear5).grid(row = 2, column = 1)
Button(buttons, text = '6',bg='LightCyan',font='Helvetica 16 bold ',command=appear6).grid(row = 2, column = 2)
Button(buttons, text = '7',bg='LightCyan',font='Helvetica 16 bold ', command=appear7).grid(row = 3, column = 0)
Button(buttons, text = '8',bg='LightCyan', font='Helvetica 16 bold ',command=appear8).grid(row = 3, column = 1)
Button(buttons, text = '9',bg='LightCyan',font='Helvetica 16 bold ',command=appear9).grid(row = 3, column = 2)
Button(buttons, text = '0',bg='LightCyan', font='Helvetica 16 bold ',command=appear0).grid(row = 4, column = 1)
Button(buttons, text = '=',font='Helvetica 16 bold ',bg='LightCyan',command=calc).grid(row = 4, column = 0)
Button(buttons, text = 'C',font='Helvetica 16 bold ',bg='LightCyan',command=clear).grid(row = 6, column = 0)
Button(buttons, text = 'S',font='Helvetica 16 bold ',bg='LightCyan',command=space).grid(row = 6, column = 1)
Button(buttons, text = '^',font='Helvetica 16 bold ',bg='LightCyan',command=appearpow).grid(row = 4, column = 2)


##Button(buttons, text = 'exit', font='Helvetica 16 bold ',bg='LightCyan',).grid(row = 4, column = 3)
Button(buttons, text = '+',font='Helvetica 16 bold ',bg='LightCyan',command=appearADD).grid(row = 5, column = 0)
Button(buttons, text = '-',font='Helvetica 16 bold ' ,bg='LightCyan',command=appearSUB).grid(row = 5, column = 1)
Button(buttons, text = '*',font='Helvetica 16 bold ' ,bg='LightCyan',command=appearMUL).grid(row = 5, column = 2)
Button(buttons, text = '/', font='Helvetica 16 bold ',bg='LightCyan',command=appearDIV).grid(row = 5, column = 3)


#zero= Button(buttons, bg="White", text="0", width=5, height=2)
#zero.grid(padx=5, pady=5, column=1, row=3)

##functions=["-", "+", "*", "/"]
##for index in range(4):
##    Button(buttons, bg="LightCyan",font='Helvetica 9 bold', text=functions[index], width=5, height=2).grid(padx=5, pady=5, row=index%4, column=3) 

 

numbers = StringVar()
results = Entry(screen, textvariable=numbers, width=30)
results.pack()

#calculator.buttonsloop()
calculator.mainloop()
