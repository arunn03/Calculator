from tkinter import *
from threading import Thread

def chgSign():
    text = entVar.get()
    try:
        if '-' not in text and text not in operators:
            entVar.set('-' + text)
        elif text[0] == '-' and text not in operators:
            entVar.set(text[1:])
    except:
        pass

def clear(event=None):
    entVar.set('')

def backSpace():
    text = entVar.get()
    try:
        entVar.set(text[:-1])
    except:
        pass

def zero():
    if entVar.get() != '':
        entVar.set(entVar.get() + '0')

def thread_submit(event=None):
    Thread(target=submit).start()

def submit():
    with open('log.txt', 'a') as f:
        f.write('Given Operation: "' + entVar.get() + '"\n')
        try:
            if '%' not in entVar.get():
                entVar.set(str(eval(entVar.get())))
            else:
                text = entVar.get()
                operand1 = float(text[:text.index('%')])
                operand2 = float(text[text.index('%')+1:])
                res = (operand2 / 100) * operand1
                entVar.set(str(res))
        except:
            entVar.set('ERROR  ')
        f.write('Result: "' + entVar.get() + '"\n')
    f.close()
    entry.icursor("end")

root = Tk()
root.title('Calculator')
root.iconbitmap('./res/icon.ico')
root.resizable(False, False)

# Variables
operators = ('+', '-', '*', '/', '%', '')
entVar = StringVar()
plusMinus = PhotoImage(file='./res/plusMinus.png')

# root widgets
entry = Entry(root, textvar=entVar, justify=RIGHT, borderwidth=6,
              width=18, cursor='', fg='black', bg='light green',
              font=('calculator', 20, 'bold'))
entry.pack()

# Button Frame
btnFrame = Frame(root, bg='sky blue')
btnPercent = Button(btnFrame, text='%', width=4, font=('arial', 14, 'bold'), borderwidth=5,
                    command=lambda: entVar.set(entVar.get() + '%'), bg='sky blue')
btnClear = Button(btnFrame, text='AC', width=4, font=('arial', 14, 'bold'), borderwidth=5,
                  command=clear, bg='sky blue')
btnBackspace = Button(btnFrame, text='«', width=4, font=('arial', 14, 'bold'), borderwidth=5,
                      command=backSpace, bg='sky blue')
btnSlash = Button(btnFrame, text='/', width=4, font=('arial', 14, 'bold'), borderwidth=5,
                  command=lambda: entVar.set(entVar.get() + '/'), bg='sky blue')
btn7 = Button(btnFrame, text='7', width=4, font=('arial', 14, 'bold'), borderwidth=5,
              command=lambda: entVar.set(entVar.get() + '7'), bg='sky blue')
btn8 = Button(btnFrame, text='8', width=4, font=('arial', 14, 'bold'), borderwidth=5,
              command=lambda: entVar.set(entVar.get() + '8'), bg='sky blue')
btn9 = Button(btnFrame, text='9', width=4, font=('arial', 14, 'bold'), borderwidth=5,
              command=lambda: entVar.set(entVar.get() + '9'), bg='sky blue')
btnStar = Button(btnFrame, text='*', width=4, font=('arial', 14, 'bold'), borderwidth=5,
                 command=lambda: entVar.set(entVar.get() + '*'), bg='sky blue')
btn4 = Button(btnFrame, text='4', width=4, font=('arial', 14, 'bold'), borderwidth=5,
              command=lambda: entVar.set(entVar.get() + '4'), bg='sky blue')
btn5 = Button(btnFrame, text='5', width=4, font=('arial', 14, 'bold'), borderwidth=5,
              command=lambda: entVar.set(entVar.get() + '5'), bg='sky blue')
btn6 = Button(btnFrame, text='6', width=4, font=('arial', 14, 'bold'), borderwidth=5,
              command=lambda: entVar.set(entVar.get() + '6'), bg='sky blue')
btnMinus = Button(btnFrame, text='-', width=4, font=('arial', 14, 'bold'), borderwidth=5,
                  command=lambda: entVar.set(entVar.get() + '-'), bg='sky blue')
btn1 = Button(btnFrame, text='1', width=4, font=('arial', 14, 'bold'), borderwidth=5,
              command=lambda: entVar.set(entVar.get() + '1'), bg='sky blue')
btn2 = Button(btnFrame, text='2', width=4, font=('arial', 14, 'bold'), borderwidth=5,
              command=lambda: entVar.set(entVar.get() + '2'), bg='sky blue')
btn3 = Button(btnFrame, text='3', width=4, font=('arial', 14, 'bold'), borderwidth=5,
              command=lambda: entVar.set(entVar.get() + '3'), bg='sky blue')
btnPlus = Button(btnFrame, text='+', width=4, font=('arial', 14, 'bold'), borderwidth=5,
                 command=lambda: entVar.set(entVar.get() + '+'), bg='sky blue')
btnSign = Button(btnFrame, image=plusMinus, width=52, height=33, borderwidth=5,
                 command=chgSign, bg='sky blue')
btn0 = Button(btnFrame, text='0', width=4, font=('arial', 14, 'bold'), borderwidth=5,
              command=zero, bg='sky blue')
btnPoint = Button(btnFrame, text='.', width=4, font=('arial', 14, 'bold'), borderwidth=5,
                  command=lambda: entVar.set(entVar.get() + '.'), bg='sky blue')
btnSub = Button(btnFrame, text='=', width=4, font=('arial', 14, 'bold'), borderwidth=5,
                command=thread_submit, bg='sky blue')

# Packing widgets
btnFrame.pack(expand='yes')
btnPercent.grid(row=0, column=0)
btnClear.grid(row=0, column=1)
btnBackspace.grid(row=0, column=2)
btnSlash.grid(row=0, column=3)
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btnStar.grid(row=1, column=3)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btnMinus.grid(row=2, column=3)
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btnPlus.grid(row=3, column=3)
btnSign.grid(row=4, column=0)
btn0.grid(row=4, column=1)
btnPoint.grid(row=4, column=2)
btnSub.grid(row=4, column=3)

# Key bindings
root.bind('<Return>', thread_submit)
root.bind('<Escape>', clear)

root.mainloop()
