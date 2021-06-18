import easyocr
import cv2
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
from Readings import readings
import os
from ImgProcess import crop
import operator
from tkinter import *
import tkinter
import datetime
import random
class data:
    def __init__(self,master):
        self.master=master
        self.record_date=""
        self.patient_name=""
        self.patient_age = 23
        self.path=""
        self.read=[]
        self.number_images=0
        self.string=""
    def get_date(self):
        list_return=[]
        for i in self.read:
            list_return.append(i.get_date())
        return list_return
    def get_time(self):
        list_return=[]
        for i in self.read:
            list_return.append(i.get_time())
        return list_return
    def get_sys(self):
        list_return=[]
        for i in self.read:
            list_return.append(i.get_sys())
        return list_return
    def get_dia(self):
        list_return=[]
        for i in self.read:
            list_return.append(i.get_dia())
        return list_return
    def get_bpm(self):
        list_return=[]
        for i in self.read:
            list_return.append(i.get_bpm())
        return list_return
    def get_map(self):
        list_return=[]
        for i in self.read:
            list_return.append(i.get_map())
        return list_return