# !/usr/bin/python3
# //////////////////////////////////////
#    analogInContinuous.py
#     Read analog data via IIO continous mode and plots it.
# //////////////////////////////////////

# From: https://stackoverflow.com/questions/20295646/python-ascii-plots-in-terminal
# https://github.com/dkogan/gnuplotlib
# https://github.com/dkogan/gnuplotlib/blob/master/guide/guide.org
# sudo apt install gnuplot  (10 minute to install)
# pip3 install gnuplotlib
# This uses X11, so when connecting to the bone from the host use:  ssh -X bone

# See https://elinux.org/index.php?title=EBC_Exercise_10a_Analog_In#Analog_in_-_Continuous.2C_Change_the_sample_rate
# for instructions on changing the sampling rate.  Can go up to 200KHz.

import numpy as np
import datetime
import time
import sqlite3

CON = sqlite3.connect("Database.db")
CUR = CON.cursor()

class ReadOut(object):

    def __init__(self, MAX):
        self.IIOPATH = IIOPATH = '/sys/bus/iio/devices/iio:device0'
        self.IIODEV = '/dev/iio:device0'
        self.MAX = MAX #Obere Grenze
     #  self.SLEEPTIME = 1
        self.Len = 1
        self.AIN = '1'
        self.Run = True
        self.SetTimeDelta =1
        self.lastTime = datetime.datetime.now()
        
    # Setup IIO for Continous reading
    # Enable AIN
    def read(self,zeit):
        try:
            file1 = open(self.IIOPATH + '/scan_elements/in_voltage' + self.AIN + '_en', 'w')
            file1.write('1')
            file1.close()
        except:  # carry on if it's already enabled
            pass
        # Set buffer length
        file1 = open(self.IIOPATH + '/buffer/length', 'w')
        file1.write(str(2 * self.Len))  # I think LEN is in 16-bit values, but here we pass bytes
        file1.close()
        # Enable continous
        file1 = open(self.IIOPATH + '/buffer/enable', 'w')
        file1.write('1')
        file1.close()
        fd = open(self.IIODEV, "r")
#        print('Hit ^C to stop')
        y = np.fromfile(fd, dtype='uint16', count=self.Len)
        if y >= self.MAX and zeit-self.lastTime>datetime.timedelta(seconds=self.SetTimeDelta):
            print(time.ctime())
            print(y[0])
            self.setOutput
            self.lastTime= datetime.datetime.now()
    def close(self):
        print("Turning off input.")
        file1 = open(self.IIOPATH + '/buffer/enable', 'w')
        file1.write('0')
        file1.close()
        file1 = open(self.IIOPATH + '/scan_elements/in_voltage' + self.AIN + '_en', 'w')
        file1.write('0')
        file1.close()
        self.Run = False

    def setTimeDiff(diff):
        self.lastTime = diff

    def __del__(self):
        print("done")

    def setOutput(self):
        print("something")
        sql = "SELECT count(*) FROM VERBRAUCH WHERE DATE = %s" %datetime.date.today()
        CUR.execute(sql)
        for dsatz in CUR:
            if dsatz[0]==0:
                CUR.execute("INSERT INTO VERBRAUCH VALUES('%s',1)"%datetime.date.today()
                CON.commit()
        CON.close()
# // Bone  | Pocket | AIN
# // ----- | ------ | ---
# // P9_39 | P1_19  | 0
# // P9_40 | P1_21  | 1
# // P9_37 | P1_23  | 2
# // P9_38 | P1_25  | 3
# // P9_33 | P1_27  | 4
# // P9_36 | P2_35  | 5
# // P9_35 | P1_02  | 6
