""" ************************************************
Die Liste fuer die Kunden
************************************************""" 

from PyQt5.QtWidgets import QWidget, QTableView
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt


# eine Klasse fuer die Liste
# sie erbt von QWidget
class Kundenliste(QWidget):
    # die magische Methode __init__()
    def __init__(self):
        # __init__ der Uebergeordneten Klasse aufrufen
        super().__init__()

        # den Fenstertitel setzen
        self.setWindowTitle("Listenanzeige Kunden")
        
        # das Modell erstellen
        self.modell = QSqlTableModel()
        # die Tabelle setzen
        self.modell.setTable("kunden")
        
        # die Texte fuer die Spaltenkoepfe setzen
        self.modell.setHeaderData(0, Qt.Horizontal, "ID")
        self.modell.setHeaderData(1, Qt.Horizontal, "Vorname")
        self.modell.setHeaderData(2, Qt.Horizontal, "Name")
        self.modell.setHeaderData(3, Qt.Horizontal, "Strasse")
        self.modell.setHeaderData(4, Qt.Horizontal, "PLZ")
        self.modell.setHeaderData(5, Qt.Horizontal, "Ort")
        self.modell.setHeaderData(6, Qt.Horizontal, "Telefon")       
       
        # die Daten beschaffen
        self.modell.select()
        # mit dem Modell verbinden
        self.ansicht = QTableView(self)
        self.ansicht.setModel(self.modell)
        # die Breite der Spalten an den Inhalt anpassen
        self.ansicht.resizeColumnsToContents()
        # die Zeilennummern ausblenden
        self.ansicht.verticalHeader().setVisible(False)

        # die Groesse setzen
        self.ansicht.resize(500, 300)
