import sqlite3
import time
import datetime
import auslesen 


if __name__ == '__main__':
# setInputDatabase()
    reader = auslesen.ReadOut(1350)
    while reader.Run:
        try:
           reader.read(datetime.datetime.now())
           time.sleep(0.025)
        except KeyboardInterrupt:
           reader.close()

    
