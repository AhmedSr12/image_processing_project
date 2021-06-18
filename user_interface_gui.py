import tkinter.messagebox
from  ThirdPage import  frame3
from  tkinter import  filedialog
from  Data import data
from  tkinter import  *
class interface :
    def __init__(self, master):
        self.newmaster = master
        self.master = Frame(master)
        self.master.pack()
        self.enter_Name = Label(self.master, text=" Enter Patient Name : ", font="arial 14 italic")
        #self.enter_Name.grid(row=5, column=0)
        self.Name_entry = Entry(self.master, font="arial 14 italic")
        #self.Name_entry.grid(row=5, column=1)

        self.enter_Date = Label(self.master, text=" Date :", font="arial 14 italic")
        #self.enter_Date.grid(row=7, column=0)
        self.Date_entry = Entry(self.master, font="arial 14 italic")
        #self.Date_entry.grid(row=7, column=1)

        self.enter_Age = Label(self.master, text=" Enter Patient Age :", font="arial 14 italic")
        #self.enter_Age.grid(row=6, column=0)
        self.Age_entry = Entry(self.master, font="arial 14 italic")
        #self.Age_entry.grid(row=6, column=1)

        self.enter_path = Label(self.master, text=" Please Enter or Browse Folder Path : ", font="arial 14 italic")
        self.enter_path.grid(row=8, column=0)
        self.path_entry = Entry(self.master, font="arial 14 italic")
        self.path_entry.grid(row=8, column=1)
        self.OK_Button = Button(self.master, text=" OK ", command=self.OK, font="arial 14 italic", width=10)
        self.OK_Button.grid(row=9, column=2)
        self.browse = Button(self.master, text=" Browse File ", command=self.browse, font="bold 14 italic", width=10)
        self.browse.grid(row=8, column=2)

    def filedialog(self):
        self.filename = filedialog.askdirectory(title="Select Image Folder")
        return self.filename

    def OK(self):
        self.File_Path = self.path_entry.get()
        A, B, C = self.Date_entry.get(), self.Name_entry.get(), self.Age_entry.get()
        self.master.pack_forget()
        self.master.destroy()
        self.f = frame3(self.newmaster,A, B, C )



    def browse(self):
        self.File_Path = self.filedialog()

        if self.File_Path != "":
            A,B,C=self.Date_entry.get(), self.Name_entry.get(), self.Age_entry.get()
            self.master.pack_forget()
            self.master.destroy()

            self.f = frame3(self.newmaster ,self.File_Path,A, B, C )
