from tkinter import *
base = Tk()


def eq():
    a = dis.get()
    a = eval(str(a))
    dis.delete(0, END)
    dis.insert(0, a)


def on_click(value):
    dis.insert(0, value)


base.geometry("400x400")
base.title("Calculator")
disconfig = ("15")
dis = Entry(base, width=40, font=disconfig, justify="right")
dis.place(x=20, y=30)
b1 = Button(base, text=1, width=5, height=3, command=lambda: on_click("1"))
b2 = Button(base, text=2, width=5, height=3, command=lambda: on_click("2"))
b3 = Button(base, text=3, width=5, height=3, command=lambda: on_click("3"))
b4 = Button(base, text=4, width=5, height=3, command=lambda: on_click("4"))
b5 = Button(base, text=5, width=5, height=3, command=lambda: on_click("5"))
b6 = Button(base, text=6, width=5, height=3, command=lambda: on_click("6"))
b7 = Button(base, text=7, width=5, height=3, command=lambda: on_click("7"))
b8 = Button(base, text=8, width=5, height=3, command=lambda: on_click("8"))
b9 = Button(base, text=9, width=5, height=3, command=lambda: on_click("9"))
b0 = Button(base, text=0, width=5, height=3, command=lambda: on_click("0"))
ad = Button(base, text="+", width=5, height=3, command=lambda:on_click("+"))
sub = Button(base, text="-", width=5, height=3, command=lambda: on_click("-"))
mul = Button(base, text="x", width=5, height=3, command=lambda: on_click("X"))
div = Button(base, text="/", width=5, height=3, command=lambda: on_click("/"))
mod = Button(base, text="%", width=5, height=3, command=lambda: on_click("%"))
eq = Button(base, text="=", width=5, height=3, command= eq)

b1.place(x=30, y=80)
b2.place(x=80, y=80)
b3.place(x=130, y=80)
b4.place(x=180, y=80)
b5.place(x=30, y=180)
b6.place(x=80, y=180)
b7.place(x=130, y=180)
b8.place(x=180, y=180)
b9.place(x=30, y=270)
b0.place(x=80, y=270)
ad.place(x=270, y=80)
sub.place(x=270, y=180)
mul.place(x=270, y=270)
div.place(x=330, y=80)
mod.place(x=330, y=180)
eq.place(x=330, y=270)


base.mainloop()