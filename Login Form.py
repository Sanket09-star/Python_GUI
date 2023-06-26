from tkinter import *
base = Tk()
base.title("Login Form")
base.geometry("600x800")
font = ("Bodoni Bk BT", 15)
font1 = ("Bodoni Bk BT", 20)

main_labal = Label(base, text="Login Form", font=font1, bg="lightBlue")

b1 = Button(base, text="Submit", font=font, bg="lightblue")
b2 = Button(base, text="Reset", font=font, bg="lightblue")
f = Label(base, text="Enter First Name : ", font=font, bg="lightgreen")
la = Label(base, text="Enter Last Name :  ", font=font, bg="lightgreen")

addr = Label(base, text="Enter Address : ", font=font, bg="lightgreen")
coun = Label(base, text="Select Country : ", font=font, bg="lightgreen")
gen = Label(base, text="Select Gender : ", font=font, bg="lightgreen")
user = Label(base, text="Select User Type : ", font=font, bg="lightgreen")

ad = Text(base, width=30, height=5)
ch1 = Checkbutton(base, text="Personal Use : ", font=font)
ch2 = Checkbutton(base, text="Company Use : ", font=font)

c = StringVar()
c.set("Select Country")
countries = ("Australia", "USA", "UAE", "Nepal", "India", "Ukraine")
op1 = OptionMenu(base, c, *countries)

a = IntVar()
rb1 = Radiobutton(base, text="Male", font=font, variable=a, value=1)
rb2 = Radiobutton(base, text="Female", font=font, variable=a, value=2)

f1 = Entry(base, font=font)
l1 = Entry(base, font=font)


f.place(x=50, y=80)
f1.place(x=200, y=80)
la.place(x=50, y=140)
l1.place(x=200, y=140)
coun.place(x=50, y=200)
op1.place(x=200, y=200)
gen.place(x=50, y=260)
rb1.place(x=200, y=260)
rb2.place(x=300, y=260)
user.place(x=50, y=320)
ch1.place(x=200, y=320)
ch2.place(x=200, y=360)
addr.place(x=50, y=420)
ad.place(x=200, y=420)
main_labal.place(x=10, y=10)
b1.place(x=50, y=540)
b2.place(x=340, y=540)
base.mainloop()
