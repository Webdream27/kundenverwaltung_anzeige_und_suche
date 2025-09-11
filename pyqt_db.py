""" ************************************************
Ein einfaches Datenbankprogramm mit PyQt
************************************************""" 

# die Klassen importieren
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# Schritt 1: Die Verbindung zur Datenbank adressen.db herstellen 
# die Verbindung zur Datenbank herstellen
datenbank = QSqlDatabase.addDatabase("QSQLITE")
# den Datenbanknamen setzen
datenbank.setDatabaseName("adressen.db")

# konnte die Datenbank geöffnet werden?
# wenn nicht, geben wir eine Meldung aus und brechen ab
if datenbank.open() == False:
    print("Die Datenbank konnte nicht göffnet werden!")
    exit()
 
# Schritt 2: Die Daten beschaffen 
# hier nehmen wir alle Datensätze der Tabelle kunden
abfrage = QSqlQuery()
abfrage.exec("SELECT * FROM kunden")
 
# Schritt 3: Die Daten verarbeiten 
# gibt es noch Einträge?
while abfrage.next() == True:
		# einlesen
		nummer = abfrage.value(0)
		# dann ausgeben
		print("Nummer: ", nummer)
		vorname = abfrage.value(1)
		# dann ausgeben
		print("Vorname: ", vorname)
		name = abfrage.value(2)
		print("Name: ", name)
		strasse = abfrage.value(3)
		print("Straße: ", strasse)
		plz = abfrage.value(4)
		print("PLZ: ", plz)
		ort = abfrage.value(5)
		print("Ort: ", ort)
		telefon = abfrage.value(6)
		print("Telefon: ", telefon)

# Schritt 4: Die Verbindung wieder schließen 
datenbank.close()

