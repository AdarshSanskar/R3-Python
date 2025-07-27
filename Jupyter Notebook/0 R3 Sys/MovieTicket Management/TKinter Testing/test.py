from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

# root = Tk() ---> Old
root = tb.Window(themename="superhero")
root.title("Demo of TTK Bootstrap")
root.iconbitmap('Logo1.ico')
root.geometry('500x500')

label = tb.Label(text="Hello World", font=(28),bootstyle = "default")
label.pack(pady=50)



root.mainloop()