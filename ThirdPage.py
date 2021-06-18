from  Data import data
from tkinter import *
from tkinter import filedialog

class frame3 :
    def __init__(self, master, filePath,Date_entry, Name_entry, Age_entry):
        self.newmaster = master
        self.master = Frame(master)
        self.master.pack()
        self.filepath=filePath
        self.data1=data(self.newmaster)
        self.data1.setdata(Date_entry, Name_entry, Age_entry)
        self.data1.setpath(self.filepath)
        self.generate = Button(self.master, text=" Show Readings ", command=self.generate, font="bold 14 italic", width=16)
        self.generate.pack()
        self.save=Button(self.master, text=" Save Graph ", command=self.save, font="bold 14 italic", width=10)
        self.save.pack()

    def filedialog(self, type="xml"):
        filename = filedialog.asksaveasfilename(title="Save File", filetypes=(
            ("PNG", "*.png"),

        ))
        return filename

    def save(self):
        path = self.filedialog()
        self.data1.save_graph(path + '.png')