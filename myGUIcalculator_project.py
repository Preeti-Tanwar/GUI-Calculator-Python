from tkinter import *
from math import sin,cos,tan
def click(event):
    global entry_variable
    text=event.widget.cget("text")
    if text == "=":
        if entry_variable.get().isdigit():
            value = int(entry_variable.get())
        else:
            try:
                value = eval(calculator_screen.get())
            except Exception as e:
                print(e)
                value = "Error"
        entry_variable.set(value)
        # if text=="^":
        #     text=
    elif text == "C":
        entry_variable.set("")
        calculator_screen.update()

    else:
        entry_variable.set(entry_variable.get() + text)
        calculator_screen.update()

root=Tk()
root.geometry("250x370")
root.title("Genius Calculator")
root.configure(background="pink")
# set icon in title
photo=PhotoImage(file="calculator_icon3.png")
root.iconphoto(False,photo)
# screen of calculator
entry_variable=StringVar()
entry_variable.set("")
calculator_screen=Entry(root,textvariable=entry_variable,borderwidth=6, relief=SUNKEN, font="lucida 20 bold")
calculator_screen.pack(fill="x", padx=8, pady=8)

# making frame for first row of buttons
f1=Frame(root, background="blue")
b=Button(f1, text="7", font="lucida 20 bold")
b.bind("<Button-1>", click)
b.grid(row=1, column=1)

b=Button(f1, text="8", font="lucida 20 bold")
b.bind("<Button-1>", click)
b.grid(row=1, column=2)

b=Button(f1, text="9", font="lucida 20 bold")
b.bind("<Button-1>", click)
b.grid(row=1, column=3)

b=Button(f1, text="/", font="lucida 20 bold",padx=3)
b.bind("<Button-1>", click)
b.grid(row=1, column=4)

b=Button(f1, text="sin", font="lucida 20 bold",padx=2)
b.bind("<Button-1>", click)
b.grid(row=1, column=5)
f1.pack(anchor="nw",padx=8)

f2=Frame(root, background="lightgrey")
b=Button(f2, text="4", font="lucida 20 bold")
b.bind("<Button-1>", click)
b.grid(row=2, column=1)

b=Button(f2, text="5", font="lucida 20 bold")
b.bind("<Button-1>", click)
b.grid(row=2, column=2)

b=Button(f2, text="6", font="lucida 20 bold")
b.bind("<Button-1>", click)
b.grid(row=2, column=3)

b=Button(f2, text="*", font="lucida 20 bold",padx=2)
b.bind("<Button-1>", click)
b.grid(row=2, column=4)

b=Button(f2, text="cos", font="lucida 20 bold", width=3, padx=4)
b.bind("<Button-1>", click)
b.grid(row=2, column=5)
f2.pack(anchor="nw", padx=8)

f3=Frame(root, background="lightgrey")
b=Button(f3, text="1", font="lucida 20 bold")
b.bind("<Button-1>", click)
b.grid(row=3, column=1)

b=Button(f3, text="2", font="lucida 20 bold")
b.bind("<Button-1>", click)
b.grid(row=3, column=2)

b=Button(f3, text="3", font="lucida 20 bold")
b.bind("<Button-1>", click)
b.grid(row=3, column=3)

b=Button(f3, text="-", font="lucida 20 bold", padx=4)
b.bind("<Button-1>", click)
b.grid(row=3, column=4)

b=Button(f3, text="tan", font="lucida 20 bold")
b.bind("<Button-1>", click)
b.grid(row=3, column=5)
f3.pack(anchor="nw", padx=8)

f4=Frame(root, background="lightgrey")
b=Button(f4, text=".", font="lucida 20 bold",padx=4)
b.bind("<Button-1>", click)
b.grid(row=4, column=1)

b=Button(f4, text="0", font="lucida 20 bold", padx=2)
b.bind("<Button-1>", click)
b.grid(row=4, column=2)

b=Button(f4, text="C", font="lucida 20 bold")
b.bind("<Button-1>", click)
b.grid(row=4, column=3)

b=Button(f4, text="+", font="lucida 20 bold")
b.bind("<Button-1>", click)
b.grid(row=4, column=4)

b=Button(f4, text="**", font="lucida 20 bold",width=3)
b.bind("<Button-1>", click)
b.grid(row=4, column=5)
f4.pack(anchor="nw", padx=8)

f5=Frame(root)
b=Button(f5,text="(", font="lucida 20 bold")
b.bind("<Button-1>", click)
b.grid(row=5, column=1)

b=Button(f5,text=")", font="lucida 20 bold")
b.bind("<Button-1>", click)
b.grid(row=5, column=2)

b=Button(f5,text="=", font="lucida 20 bold", width=9)
b.bind("<Button-1>", click)
b.grid(row=5,column=3)

f5.pack(anchor="nw", padx=8)
root.mainloop()