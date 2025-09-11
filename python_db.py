""" ************************************************
Ein einfaches Datenbankprogramm
************************************************""" 

# das Modul importieren
import sqlite3

# die Verbindung zur Datenbank herstellen
connection = sqlite3.connect("adressen.db")

# den Cursor beschaffen
cursor = connection.cursor()

# SQL-Kommandos über die Methode execute() ausführen
# die Datenbanktabelle erstellen
cursor.execute(
"""CREATE TABLE kunden(
	kNummer INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	vorname TEXT NOT NULL,
	nachname TEXT NOT NULL,
	strasse TEXT NOT NULL,
	plz TEXT NOT NULL,
	ort TEXT NOT NULL,
	telefon TEXT)"""
)

# Datensätze einfügen
cursor.execute("INSERT INTO kunden (vorname, nachname, strasse, plz, ort) VALUES ('Erwin', 'Müller', 'Hasenweg 16', '12345', 'Hasenhausen')")
cursor.execute("INSERT INTO kunden (vorname, nachname, strasse, plz, ort) VALUES ('Erna', 'Strobelt', 'Birnenplatz 1', '56789', 'Bullerbue')")
# Die Änderungen durchführen
connection.commit()

# die Daten beschaffen und anzeigen
ergebnis = cursor.execute("SELECT * FROM kunden")
for datensatz in ergebnis:
    print(datensatz)

# die Verbindung schließen
connection.close()