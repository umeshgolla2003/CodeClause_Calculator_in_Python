from tkinter import *

def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if  scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)

root = Tk()
root.geometry("415x525")
root.title("Calculator By Umesh")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font = "lucida 40 bold")
screen.pack(fill = X, ipadx=8, pady = 10, padx=10)

f = Frame(root, bg="grey")
b = Button(f, text = "9", font ="lucida 35 bold")
b.pack(side = LEFT, padx =12.5, pady =5)
b.bind("<Button-1>", click)

b = Button(f, text = "8", font ="lucida 35 bold")
b.pack(side = LEFT, padx =12.5, pady =5)
b.bind("<Button-1>", click)

b = Button(f, text = "7", font ="lucida 35 bold")
b.pack(side = LEFT, padx =12.5, pady =5)
b.bind("<Button-1>", click)

b = Button(f, text = "/", font ="lucida 35 bold")
b.pack(side = LEFT, padx =12.5, pady =5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text = "6", font ="lucida 35 bold")
b.pack(side = LEFT, padx =12, pady =5)
b.bind("<Button-1>", click)

b = Button(f, text = "5", font ="lucida 35 bold")
b.pack(side = LEFT, padx =12, pady =5)
b.bind("<Button-1>", click)

b = Button(f, text = "4", font ="lucida 35 bold")
b.pack(side = LEFT, padx =12, pady =5)
b.bind("<Button-1>", click)

b = Button(f, text = "*", font ="lucida 35 bold")
b.pack(side = LEFT, padx =12, pady =5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text = "3", font ="lucida 35 bold")
b.pack(side = LEFT, padx =13, pady =5)
b.bind("<Button-1>", click)

b = Button(f, text = "2", font ="lucida 35 bold")
b.pack(side = LEFT, padx =13, pady =5)
b.bind("<Button-1>", click)

b = Button(f, text = "1", font ="lucida 35 bold")
b.pack(side = LEFT, padx =13, pady =5)
b.bind("<Button-1>", click)

b = Button(f, text = "-", font ="lucida 35 bold")
b.pack(side = LEFT, padx =13, pady =5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text = "C", font ="lucida 35 bold")
b.pack(side = LEFT, padx =10, pady =8)
b.bind("<Button-1>", click)

b = Button(f, text = "0", font ="lucida 35 bold")
b.pack(side = LEFT, padx =10, pady =8)
b.bind("<Button-1>", click)

b = Button(f, text = "=", font ="lucida 35 bold")
b.pack(side = LEFT, padx =10, pady =8)
b.bind("<Button-1>", click)

b = Button(f, text = "+", font ="lucida 35 bold")
b.pack(side = LEFT, padx =10, pady =8)
b.bind("<Button-1>", click)

f.pack()


root.mainloop()
