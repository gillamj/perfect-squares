from math import sqrt as sr
from time import sleep as sl
import tkinter as tk

root = tk.Tk()
root.title("Enter your number here!")
a = 280
b = 85

root.geometry(str(a) + "x" + str(b))
root.configure(bg='black')
name_var = tk.StringVar()


def clear_screen():

    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):
            widget.grid_forget()


def get_squares():
    x = name_var.get()
    z = 0
    r = 4
    c = 1
    a = 280
    b = 85
    d = 1
    e = 0
    if x == "end":
        exit()
    try:
        clear_screen()
        y = float(x)
        while z <= y:
            if float(sr(z)) - int(sr(z)) == 0:
                u = str(int(sr(z))) + " is the perfect square root of " + str(z) + "!"
                tk.Label(root, text=u, font=('Georgia', 9, 'bold'), fg="RoyalBlue1", bg="black").grid(row=r, column=c)
                root.geometry(str(a) + "x" + str(b))
                z += 1
                r += 1
                if len(str(z)) > len(str(d)):
                    d = d * 10
                    e += 10
                    a += e

                if b <= 900:
                    b += 22

                if r == 44:
                    r = 4
                    c += 1
                    a += 250

            else:
                z += 1
    except ValueError:
        clear_screen()
        root.geometry("420x100")
        tk.Label(root, text="Not a valid number. Please try entering your number again.\n\
        If you do not wish to continue, please enter \"end\":",
        font=('Cascadia Code', 9, 'bold'), fg="red", bg="black").grid(row=4, column=1)


def clear_squares():

    clear_screen()
    name_entry.delete(0, 'end')
    root.geometry("550x100")
    tk.Label(root, text="Enter another number. If you do not wish to continue, please enter \"end\" in the \n\
    text box and click Submit.", font=('Arial Baltic', 9, 'bold'), fg="orange",
    bg="black").grid(row=4, column=1)


name_label = tk.Label(root, text='Number: ', font=('calibre', 10, 'bold'), fg="green2", bg="black")
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'), fg="green2", bg="black")
sub_btn = tk.Button(root, text='Submit', command=get_squares, font=('ariel', 15, 'italic'))
clr_btn = tk.Button(root, bg='grey', text='Clear', command=clear_squares, font=('ariel', 15, 'bold'), relief="groove")

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

sub_btn.grid(row=2, column=1)
clr_btn.grid(row=2, column=0)

root.geometry("450x150")
tk.Label(root, text="Please enter your number in the textbox and click Submit. \n\
If you do not wish to continue, please enter \"end\" in the \n\
text box and click Submit.", font=('Tunga', 9, 'bold'), fg="ivory4",
bg="black").grid(row=4, column=1)

root.mainloop()




