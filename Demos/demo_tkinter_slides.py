import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

top = tk.Tk()

def hello():
     messagebox.showinfo("Say Hello", "Hello World")


filename = askopenfilename()
print(filename)


btn1 = tk.Button(top, text = "Say Hello", command = hello)
btn1.pack()

top.geometry("200x100")
top.mainloop()
