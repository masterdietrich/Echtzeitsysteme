import sqlite3
import time
import datetime
import auslesen 


if __name__ == '__main__':
# setInputDatabase()
    reader = auslesen.ReadOut(3000)
    while reader.Run:
        try:
           reader.read(datetime.datetime.now())
           time.sleep(20)
        except KeyboardInterrupt:
           reader.close()

    
