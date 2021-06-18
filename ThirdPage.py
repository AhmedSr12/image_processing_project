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
        self.data1.Extract_data()
        self.date = self.data1.get_date()
        self.time = self.data1.get_time()
        self.sys = self.data1.get_sys()
        self.dia = self.data1.get_dia()
        self.bpm = self.data1.get_bpm()
        self.map = self.data1.get_map()
        self.data1.graph()
        self.data1.Show_Graph()

    def filedialog(self, type="xml"):
        filename = filedialog.asksaveasfilename(title="Save File", filetypes=(
            ("PNG", "*.png"),

        ))
        return filename

    def save(self):
        path = self.filedialog()
        self.data1.save_graph(path + '.png')

    def generate(self):
        Master = Tk()

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=10000, height=5000)

        canvas = Canvas(Master)
        self.scroll = Frame(Master)
        self.scroll.pack(side=BOTTOM, fill="x")
        self.frame = Frame(canvas)
        myscrollbar = Scrollbar(Master, command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)
        canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.frame.bind("<Configure>", myfunction)
        myscrollbar.pack(side=RIGHT, fill="y")
        canvas.pack(side=RIGHT)

        myscrollbar1 = Scrollbar(self.scroll, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=myscrollbar1.set)
        canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.frame.bind("<Configure>", myfunction)
        myscrollbar1.pack(side="bottom", fill="x")
        canvas.pack(side="top")

        self.draw(self.frame, 0, 0, text="Date")
        self.draw(self.frame, 0, 1, text="Time")
        self.draw(self.frame, 0, 2, text="SYS/DIA")
        self.draw(self.frame, 0, 3, text="HR[Bpm]")
        self.draw(self.frame, 0, 4, text="MAP")
        no = self.data1.getNo_img() + 1
        for i in range(no)[1:]:
            self.draw(self.frame, i, 0, text=self.date[i - 1])
            self.draw(self.frame, i, 1, text=self.time[i - 1])
            self.draw(self.frame, i, 2, text=self.sys[i - 1] + "/" + self.dia[i - 1])
            self.draw(self.frame, i, 3, text=self.bpm[i - 1])
            self.draw(self.frame, i, 4, text=self.map[i - 1])

    def draw(self, master, row, column, text="", width=12):
        s = text
        e = Label(master, text=s, borderwidth=1, relief="solid", width=width, height=2,
                  font="arial 16 italic")
        e.grid(row=row, column=column)