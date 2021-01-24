from tkinter import *

equation = "0"
expression = [0]
num_flag = 1

def evaluate(a, b, op):
    if op == '/':
        return a/b
    elif op == '*':
        return a*b
    elif op == '+':
        return a+b
    elif op == '-':
        return a-b

def precedence(op):
    if op == '/':
        return 4
    elif op == '*':
        return 3
    elif op == '+':
        return 2
    elif op == '-':
        return 1
    return 0


def pressnum(val):
    global equation
    global expression
    global num_flag
    if num_flag:
        num = expression.pop()
        temp = num * 10 + val
        expression.append(temp)
    else:
        expression.append(val)
        num_flag = 1
    if equation[0] == '0':
        equation = str(val)
    else:
        equation = equation + str(val)
    inp.set(equation)
    print(expression)


def pressop(op):
    global equation
    global expression
    global num_flag
    if num_flag:
        expression.append(op)
        equation = equation + op
        inp.set(equation)
    num_flag = 0
    print(expression)


def pressclear():
    global equation
    global expression
    global num_flag
    temp = ""
    if type(expression[-1]) == str:
        num_flag = 1
    else:
        num_flag = 0
    if expression and equation:
        expression.pop()
        equation = equation[:-1]
    else:
        expression = [0]
        equation = "0"
    inp.set(equation)

def pressenter():
    global equation
    global expression
    global num_flag

    stack = []
    postfix = []
    for i in expression:
        if type(i) == str:
            while stack and precedence(i) < precedence(stack[-1]):
                postfix.append(stack.pop())
            stack.append(i)
        else:
            postfix.append(i)
        print(stack)
    print(postfix)
    for i in stack[-1::-1]:
        postfix += i
    print(postfix)
    stack = []
    for i in postfix:
        if precedence(i) == 0:
            stack.append(i)
        else:
            b = stack.pop()
            a = stack.pop()
            temp = evaluate(a, b, i)
            stack.append(temp)
    expression = [float(stack.pop())]
    equation = str(expression[0])
    inp.set(equation)

def allclear():
    global equation
    global expression
    expression = [0]
    equation = "0"
    inp.set(equation)


master = Tk()
master.title("Calculator")
master.geometry("400x400")
master.configure(background="White")
master.resizable(0, 0)

entry = Frame(master, bg="white")
entry.pack(expand="True", fill="both")

f1 = Frame(master, bg="white")
f1.pack(expand="True", fill="both")

f2 = Frame(master, bg="grey")
f2.pack(expand="True", fill="both")

f3 = Frame(master, bg="grey")
f3.pack(expand="True", fill="both")

f4 = Frame(master, bg="grey")
f4.pack(expand="True", fill="both")

# Frame1
inp = StringVar()
entry_field = Label(entry, textvariable=inp, anchor=SE, font=("Ariel", 22), background="white")
entry_field.pack(expand="True", fill="both")

# Frame 2
button7 = Button(f1, text="7", font="Bahnscrift", relief=GROOVE, border=0, command=lambda: pressnum(7))
button7.pack(side="left", expand=True, fill="both")

button8 = Button(f1, text="8", font="Bahnscrift", relief=GROOVE, border=0, command=lambda: pressnum(8))
button8.pack(side="left", expand=True, fill="both")

button9 = Button(f1, text="9", font="Ariel", relief=GROOVE, border=0, command=lambda: pressnum(9))
button9.pack(side="left", expand=True, fill="both")

buttonDiv = Button(f1, text="/", font="Ariel", relief=GROOVE, border=0, command=lambda: pressop("/"))
buttonDiv.pack(side="left", expand=True, fill="both")

# Frame3
button4 = Button(f2, text="4", font="Ariel", relief=GROOVE, border=0, command=lambda: pressnum(4))
button4.pack(side="left", expand=True, fill="both")

button5 = Button(f2, text="5", font="Ariel", relief=GROOVE, border=0, command=lambda: pressnum(5))
button5.pack(side="left", expand=True, fill="both")

button6 = Button(f2, text="6", font="Ariel", relief=GROOVE, border=0, command=lambda: pressnum(6))
button6.pack(side="left", expand=True, fill="both")

buttonMul = Button(f2, text="*", font="Ariel", relief=GROOVE, border=0, command=lambda: pressop("*"))
buttonMul.pack(side="left", expand=True, fill="both")

# Frame4
button1 = Button(f3, text="1", font="Ariel", relief=GROOVE, border=0, command=lambda: pressnum(1))
button1.pack(side="left", expand=True, fill="both")

button2 = Button(f3, text="2", font="Ariel", relief=GROOVE, border=0, command=lambda: pressnum(2))
button2.pack(side="left", expand=True, fill="both")

button3 = Button(f3, text="3", font="Ariel", relief=GROOVE, border=0, command=lambda: pressnum(3))
button3.pack(side="left", expand=True, fill="both")

buttonSub = Button(f3, text="-", font="Ariel", relief=GROOVE, border=0, command=lambda: pressop("-"))
buttonSub.pack(side="left", expand=True, fill="both")

# Frame5
buttonAC = Button(f4, text="AC", font="Ariel", relief=GROOVE, border=0, command=lambda: allclear())
buttonAC.pack(side="left", expand=True, fill="both")

button0 = Button(f4, text="0", font="Ariel", relief=GROOVE, border=0, command=lambda: pressnum(0))
button0.pack(side="left", expand=True, fill="both")

buttonEq = Button(f4, text="=", font="Ariel", relief=GROOVE, border=0, command=lambda: pressenter())
buttonEq.pack(side="left", expand=True, fill="both")

buttonAdd = Button(f4, text="+", font="Ariel", relief=GROOVE, border=0, command=lambda: pressop("+"))
buttonAdd.pack(side="left", expand=True, fill="both")

master.mainloop()
