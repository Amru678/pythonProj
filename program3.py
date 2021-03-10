# 3.  Write a GUI program to design a simple calculator (use the grid layout)
# importing all the required modules from tkinter
from tkinter import Tk, StringVar, Frame, Entry, Button, TOP, RIGHT

win = Tk()
win.geometry("312x324")
win.resizable(0, 0)
win.title("Calculator")

expression = ""


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear():
    global expression
    expression = ""
    input_text.set("")


def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


def createButton(val, r, c, ch):
    Button(btns_frame, text=val, fg="black", width=10, height=3, bd=0, bg="#fff",
           cursor="hand2", command=lambda: btn_click(ch)).grid(row=r, column=c, padx=1, pady=1)


input_text = StringVar()

input_frame = Frame(win, width=312, height=50, bd=0,
                    highlightbackground="black", highlightcolor="black", highlightthickness=2)

input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'),
                    textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)

btns_frame = Frame(win, width=312, height=272.5, bg="grey")

btns_frame.pack()

# first row

Button(btns_frame, text="C", width=43, height=3, fg="black", bd=0, bg="#fff", cursor="hand2",
       command=lambda: bt_clear()).grid(row=0, column=0, columnspan=4, padx=1, pady=1)

# second row
createButton("7", 1, 0, 7)
createButton("8", 1, 1, 8)
createButton("9", 1, 2, 9)
createButton("*", 1, 3, "*")
# third row
createButton("4", 2, 0, 4)
createButton("5", 2, 1, 5)
createButton("6", 2, 2, 6)
createButton("-", 2, 3, "-")
# fourth row
createButton("1", 3, 0, 1)
createButton("2", 3, 1, 2)
createButton("3", 3, 2, 3)
createButton("+", 3, 3, "+")
# fourth row
createButton("0", 4, 0, 0)
createButton(".", 4, 1, ".")
Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee",
       cursor="hand2", command=lambda: bt_equal()).grid(row=4, column=2, padx=1, pady=1)
createButton("/", 4, 3, "/")

win.mainloop()
