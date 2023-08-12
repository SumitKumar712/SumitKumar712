# IMPORT THE TKINTER LIBRARY
import tkinter
from tkinter import *

# CREATE THE MAIN APPLICATION WINDOW
root=Tk()

# SET THE TITLE, SIZE, AND POSITION OF THE WINDOW
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)

# SET THE BACKGROUND COLOR TO THE WINDOW
root.configure(bg="#17161b")

# INITIALIZE THE EMPTY STRING TO STORE THE EQUATION
equation = ""

# FUNCTION TO UPDATE THE EQUATION DISPLAY
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

# FUNCTION TO CLEAR THE EQUATION DISPLAY
def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

# FUNCTION TO EVALUATE THE EQUATION AND DISPLAY THE RESULT
def calculate(value):
    global equation
    result = ""
    if equation !="":
       try:
        result = eval(equation)
       except:
          result ="error"
          equation= ""
    label_result.config(text=result)         

# CREATE A LABEL TO DISPLAY THE EQUATION AND RESULT
label_result = Label(root, width=35, height=2,text="", font=("arial",30))
label_result.pack()

# CREATE BUTTONS FOR DIGITS AND VARIOUS OPERATORS WITH THEIR RESPECTIVE FUNCTIONS
Button(root,text="C", width=5, height=2, font=("arial",30,"bold"),fg="#fff",bg="#3697f5", command=lambda: clear()).place(x=10,  y=100)
Button(root,text="/", width=5, height=2, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("/")).place(x=150, y=100)
Button(root,text="%", width=5, height=2, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("%")).place(x=290, y=100)
Button(root,text="*", width=5, height=2, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("*")).place(x=430, y=100)

Button(root,text="7", width=5, height=2, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("7")).place(x=10,  y=200)
Button(root,text="8", width=5, height=2, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("8")).place(x=150, y=200)
Button(root,text="9", width=5, height=2, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("9")).place(x=290, y=200)
Button(root,text="-", width=5, height=2, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("-")).place(x=430, y=200)

Button(root,text="4", width=5, height=2, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("4")).place(x=10,  y=300)
Button(root,text="5", width=5, height=2, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("5")).place(x=150, y=300)
Button(root,text="6", width=5, height=2, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("6")).place(x=290, y=300)
Button(root,text="+", width=5, height=2, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("+")).place(x=430, y=300)

Button(root,text="1", width=5, height=2, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("1")).place(x=10,  y=400)
Button(root,text="2", width=5, height=2, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("2")).place(x=150, y=400)
Button(root,text="3", width=5, height=2, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("3 ")).place(x=290, y=400)
Button(root,text="0", width=11, height=2, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("0")).place(x=10, y=500)

Button(root,text=".", width=5, height=2, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show(".")).place(x=290, y=500)
Button(root,text="=", width=5, height=5, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#fe9037", command=lambda: calculate("=")).place(x=430,  y=400)


# START THE MAIN EVENT LOOP
root.mainloop()