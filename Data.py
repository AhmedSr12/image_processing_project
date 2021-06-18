import easyocr
import cv2
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
from Readings import readings
import os
from ImageProcess import crop
import operator
from tkinter import *
import tkinter
import datetime
import random


class data:
    def __init__(self, master):
        self.master = master
        self.record_date = ""
        self.patient_name = ""
        self.patient_age = 23
        self.path = ""
        self.read = []
        self.number_images = 0
        self.string = ""

    def get_date(self):
        list_return = []
        for i in self.read:
            list_return.append(i.get_date())
        return list_return

    def get_time(self):
        list_return = []
        for i in self.read:
            list_return.append(i.get_time())
        return list_return

    def get_sys(self):
        list_return = []
        for i in self.read:
            list_return.append(i.get_sys())
        return list_return

    def get_dia(self):
        list_return = []
        for i in self.read:
            list_return.append(i.get_dia())
        return list_return

    def get_bpm(self):
        list_return = []
        for i in self.read:
            list_return.append(i.get_bpm())
        return list_return

    def get_map(self):
        list_return = []
        for i in self.read:
            list_return.append(i.get_map())
        return list_return

    def getNo_img(self):
        return self.number_images

    def get_data(self):
        return self.record_date

    def setdata(self, record_date, name, age):
        self.record_date = record_date
        self.patient_name = name
        self.patient_age = age

    def setpath(self, path):
        self.path = path
        DIR = self.path
        self.number_images = (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

    def Extract_data(self):

        for i in os.listdir(self.path):
            image_path = self.path + '/' + i

            img = cv2.imread(image_path)

            reader = easyocr.Reader(['en'], gpu=True)
            result = reader.readtext(crop(img))
            # print(len(result))
            # for i in range(len(result)):
            # print(result[2][1], end='\t')
            temp = readings()
            t = result[1][1]
            x = result[0][1]
            if len(t) == 4:
                t = t[0:2] + ":" + t[2:]
            else:
                if not t[3:].isnumeric():
                    t = t[0:2] + ":" + "00"
                t = t[0:2] + ":" + t[3:]

            temp.set_readings(result[0][1], t, result[5][1], result[6][1][0:3], result[10][1], result[11][1])
            self.read.append(temp)
            self.arrange()
            print(result[0][1], t, result[5][1], result[6][1][0:3], result[10][1], result[11][1], '\n')
        print("donne")

    def arrange(self):

        self.read.sort(key=operator.attrgetter('year'))
        self.read.sort(key=operator.attrgetter('month'))
        self.read.sort(key=operator.attrgetter('time'))
        self.read.sort(key=operator.attrgetter('day'))

    def graph(self):
        time = []
        SYS = []
        DIA = []
        Bpm = []
        for i in self.read:
            t = i.time
            # integer = int(t[0:2]) + int(t[4]) / 60
            time.append(t)
            SYS.append(int(i.readings[0]))
            DIA.append(int(i.readings[2]))
            Bpm.append(int(i.readings[3]))

        fig, A = plt.subplots(2)
        fig.suptitle("Bpm and Blood Pressure curves")
        A[0].plot(time, DIA)
        A[0].get_xaxis().set_visible(False)

        A[1].plot(time, SYS, DIA)

        ax = plt.gca()
        if self.number_images > 5:
            ax.axes.xaxis.set_ticks([])

        A[1].legend(["SYS", "DIA"], loc='upper right', shadow=True)
        A[0].legend(["Bpm"], loc='upper right', shadow=True)
        numb = float(self.number_images / 5)
        total = [0, int(numb * 2), int(numb * 3), int(numb * 4), -1]

        for i in total:
            temp = self.read[i].get_time()
            temp = temp[0:2]
            if int(temp) < 12:
                temp += " AM"

            else:
                if temp == "12":
                    temp += " PM"
                else:
                    temp = str(int(temp) - 12) + " PM"
            self.string += "  " + temp + "             "

        plt.xlabel(self.string)
        plt.ylabel("ABP [mmhg]")
        plt.savefig('plot.png')
        self.plot = cv2.imread('plot.png')

    def Show_Graph(self):

        canvas = Canvas(self.master, width=640, height=480)
        canvas.pack()
        img = PhotoImage(file="plot.png")
        canvas.create_image(2, 2, anchor=NW, image=img)
        os.remove("plot.png")
        mainloop()

    def save_graph(self, path):
        cv2.imwrite(path, self.plot)











