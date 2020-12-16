import sqlite3
import time
import datetime
import auslesen 
# Verbindung, Cursor
#connection = sqlite3.connect("testdatenbank.db")
#cursor = connection.cursor()

# SQL-Abfrage
#sql = "SELECT * FROM data"

# Kontrollausgabe der SQL-Abfrage
# print(sql)

# Absenden der SQL-Abfrage
# Empfang des Ergebnisses
#cursor.execute(sql)
# Ausgabe des Ergebnisses
#for dsatz in cursor:
 #   print(dsatz[0], dsatz[1])

# Verbindung beenden
#connection.close()


reader = auslesen.ReadOut(3000)


while reader.Run:
    try:
        reader.read(datetime.datetime.now())
    except KeyboardInterrupt:
        reader.close()
