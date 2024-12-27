from tkinter import *
from tkinter import messagebox
root = Tk()

clicked = True
count = 0

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b7.config(state=DISABLED)
    b9.config(state=DISABLED)

def checkwinner():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","congradulation X wins")
        disable_all_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
         b4.config(bg="red")
         b5.config(bg="red")
         b6.config(bg="red")
         winner = True
         messagebox.showinfo("tic tac toe","congradulation X wins")
         disable_all_buttons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
         b7.config(bg="red")
         b8.config(bg="red")
         b9.config(bg="red")
         winner = True
         messagebox.showinfo("tic tac toe","congradulation X wins")
         disable_all_buttons()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
         b1.config(bg="red")
         b4.config(bg="red")
         b7.config(bg="red")
         winner = True
         messagebox.showinfo("tic tac toe","congradulation X wins")
         disable_all_buttons()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
         b2.config(bg="red")
         b5.config(bg="red")
         b8.config(bg="red")
         winner = True
         messagebox.showinfo("tic tac toe","congradulation X wins")
         disable_all_buttons()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
         b3.config(bg="red")
         b6.config(bg="red")
         b9.config(bg="red")
         winner = True
         messagebox.showinfo("tic tac toe","congradulation X wins")
         disable_all_buttons()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
         b1.config(bg="red")
         b5.config(bg="red")
         b9.config(bg="red")
         winner = True
         messagebox.showinfo("tic tac toe","congradulation X wins")
         disable_all_buttons()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
         b3.config(bg="red")
         b5.config(bg="red")
         b7.config(bg="red")
         winner = True
         messagebox.showinfo("tic tac toe","congradulation X wins")
         disable_all_buttons()

    #check o
    if b1["text"] == "O" and b2["text"] == "X" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","congradulation O wins")
        disable_all_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
         b4.config(bg="red")
         b5.config(bg="red")
         b6.config(bg="red")
         winner = True
         messagebox.showinfo("tic tac toe","congradulation X wins")
         disable_all_buttons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
         b7.config(bg="red")
         b8.config(bg="red")
         b9.config(bg="red")
         winner = True
         messagebox.showinfo("tic tac toe","congradulation X wins")
         disable_all_buttons()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
         b1.config(bg="red")
         b4.config(bg="red")
         b7.config(bg="red")
         winner = True
         messagebox.showinfo("tic tac toe","congradulation O wins")
         disable_all_buttons()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
         b2.config(bg="red")
         b5.config(bg="red")
         b8.config(bg="red")
         winner = True
         messagebox.showinfo("tic tac toe","congradulation O wins")
         disable_all_buttons()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
         b3.config(bg="red")
         b6.config(bg="red")
         b9.config(bg="red")
         winner = True
         messagebox.showinfo("tic tac toe","congradulation O wins")
         disable_all_buttons()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
         b1.config(bg="red")
         b5.config(bg="red")
         b9.config(bg="red")
         winner = True
         messagebox.showinfo("tic tac toe","congradulation O wins")
         disable_all_buttons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
         b3.config(bg="red")
         b5.config(bg="red")
         b7.config(bg="red")
         winner = True
         messagebox.showinfo("tic tac toe","congradulation O wins")
         disable_all_buttons()


def b_click(b):
    global clicked, count

    if b["tex"] == "" and clicked == True:
        b["tex"] = "X"
        clicked = False
        count +=1
    elif b["tex"] == "" and clicked == False:
        b["tex"] = "O"
        clicked = True
        count +=1
    else:
        messagebox.showerror("Tic tac toe", "sorry that box has been selected")


b1 = Button(root, text=" ", font=("HELVETICA, 20"),height=3,width=6,bg="white",command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("HELVETICA, 20"),height=3,width=6,bg="white",command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("HELVETICA, 20"),height=3,width=6,bg="white",command=lambda: b_click(b3))
b4 = Button(root, text=" ", font=("HELVETICA, 20"),height=3,width=6,bg="white",command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("HELVETICA, 20"),height=3,width=6,bg="white",command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("HELVETICA, 20"),height=3,width=6,bg="white",command=lambda: b_click(b6))
b7 = Button(root, text=" ", font=("HELVETICA, 20"),height=3,width=6,bg="white",command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("HELVETICA, 20"),height=3,width=6,bg="white",command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("HELVETICA, 20"),height=3,width=6,bg="white",command=lambda: b_click(b9))

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)

b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)
