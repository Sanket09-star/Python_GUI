from tkinter import *

base = Tk()
base.geometry("380x380")
base.title("Calculator")


def addition():
    a = float(dis.get())
    b = float(dis1.get())
    c = a + b
    lb.config(text="Addition is : "+str(c))


def sub():
    a = float(dis.get())
    b = float(dis1.get())
    c = a - b
    lb.config(text="Subtraction is : "+str(c))


def mul():
    a = float(dis.get())
    b = float(dis1.get())
    c = a * b
    lb.config(text="Multiplication is : "+str(c))


def div():
    a = float(dis.get())
    b = float(dis1.get())
    c = a / b
    lb.config(text="Division is : "+str(c))


def mod():
    a = float(dis.get())
    b = float(dis1.get())
    c = a % b
    lb.config(text="Mod is : "+str(c))


def reset():
    dis.delete(0, END)
    dis1.delete(0, END)
    lb.configure(text="See Addition Here", font=15)
    dis.focus()


dis = Entry(base, width=30, font=15)
dis1 = Entry(base, width=30, font=15)
dis.place(x=20, y=30)
dis1.place(x=20, y=80)
ad = Button(base, text="+", width=5, height=3, command=addition)
sub = Button(base, text="-", width=5, height=3, command=sub)
mul = Button(base, text="X", width=5, height=3, command=mul)
div = Button(base, text="/", width=5, height=3, command=div)
mod = Button(base, text="%", width=5, height=3, command=mod)
rset = Button(base, text="Reset", width=8, height=2, command=reset)

lb = Label(base, text="See Addition Here", font=15)
lb.place(x=100, y=280)
ad.place(x=20, y=160)
sub.place(x=80, y=160)
mul.place(x=140, y=160)
div.place(x=200, y=160)
mod.place(x=260, y=160)
rset.place(x=140, y=330)
base.mainloop()
