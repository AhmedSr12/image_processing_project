class readings:
    def __init__(self):
        self.date=""
        self.year=00
        self.month = 00
        self.day = 00
        self.time="time"
        self.readings=[]
    def set_readings(self,date,time,r1,r2,r3,r4):
        if date[0] =="Z":
            temp="2"+date[1:4]
        else:
            temp =date[0:4]
        self.year = int(temp)
        self.month=int(date[5:7])
        self.day=int(date[8:])
        self.time = time
        self.readings = [r1,r2,r3,r4]
        self.date=date
    def get_date(self):
        return self.date
    def get_time(self):
        return self.time
    def get_sys(self):
        return self.readings[0]

    def get_dia(self):
        return self.readings[2]
    def get_bpm(self):
        return self.readings[3]
    def get_map(self):
        return self.readings[1]