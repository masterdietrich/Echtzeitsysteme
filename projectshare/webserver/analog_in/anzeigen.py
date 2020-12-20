import sqlite3
import time
import datetime
import auslesen 


def setInputDatabase():
    connection = sqlite3.connect("Database3.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM VERBRAUCH WHERE DATE ='%s' " %datetime.date.today()
    sql2 = "INSERT INTO VERBRAUCH VALUES('%s',1)" %datetime.date.today()
    sql3 = "SELECT COUNT(*) FROM VERBRAUCH WHERE DATE = '%s'" %datetime.date.today()
# Absenden der SQL-Abfrage
# Empfang des Ergebnisses
    cursor.execute(sql3)
    connection.commit()
# Ausgabe des Ergebnisses
    for dsatz in cursor:
        if dsatz[0]>0:
            cursor.execute(sql)
            connection.commit()
            for daniel in cursor: 
                counter = daniel[1]+1
                sql4 = "UPDATE VERBRAUCH SET COUNTER =%s WHERE DATE ='%s'" %(counter,datetime.date.today())
                print(counter)
                cursor.execute(sql4)
                connection.commit()
        else:
            cursor.execute(sql2)
            connection.commit()
# Verbindung beenden
    connection.close()





if __name__ == '__main__':
# setInputDatabase()

    reader = auslesen.ReadOut(3000)


    while reader.Run:
        try:
            if reader.read(datetime.datetime.now()) >0:
                setInputDatabase()
        except KeyboardInterrupt:
                reader.close()

