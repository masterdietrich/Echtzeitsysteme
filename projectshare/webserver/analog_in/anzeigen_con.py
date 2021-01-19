import sqlite3
import time
import datetime
import auslesen_con 


if __name__ == '__main__':
# setInputDatabase()
    reader = auslesen_con.ReadOut(3)
    while reader.Run:
        try:
           reader.read(datetime.datetime.now())
           time.sleep(0.025)
        except KeyboardInterrupt:
           reader.close()

    
