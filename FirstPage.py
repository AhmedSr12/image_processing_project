from tkinter import *
from user_interface_gui import interface
root=Tk()
root.title("Blood Pressure  Report Generator")
f=Frame(root)
f.pack()
i=interface(f)
def reset():
    global f
    f.pack_forget()
    f.destroy()
    f = Frame(root)
    f.pack()
    i = interface(f)
reset_b = Button(root, text=" Reset ", command=reset,width=5 , height= 1,font="arial 12 italic")
reset_b.pack(side=BOTTOM)
root.mainloop()