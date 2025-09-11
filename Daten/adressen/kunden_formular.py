""" ************************************************
Das Formular fuer einen neuen Eintrag
************************************************""" 

# die Module importieren
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtSql import QSqlTableModel

# das Formular importieren
from neuer_kunde import Ui_NeuerKunde

# eine Klasse für den Dialog
# sie erbt von QWidget und Ui_NeuerKunde
class NeuerKunde(QWidget, Ui_NeuerKunde):
    # die magische Methode __init__()
    def __init__(self):
        # die magische Methode __init__() der übergeordneten Klasse aufrufen
        super().__init__()
        
        # die Methode setupUi() aufrufen
        self.setupUi(self)
        
        # ein Modell erstellen
        self.modell = QSqlTableModel()
        # die Tabelle setzen
        self.modell.setTable("kunden")
        
        # die Schaltflächen verbinden
        self.button_ok.clicked.connect(self.anlegen)
        self.button_beenden.clicked.connect(self.beenden)
        
    # die Slots
    def anlegen(self):
        # eine leere Zeile ergänzen
        zeile = self.modell.rowCount()
        self.modell.insertRows(zeile, 1)
        
        # die Daten aus dem Formular übernehmen
        self.modell.setData(self.modell.index(zeile,1),self.lineEdit_vorname.text())
        self.modell.setData(self.modell.index(zeile,2),self.lineEdit_name.text())
        self.modell.setData(self.modell.index(zeile,3),self.lineEdit_strasse.text())
        self.modell.setData(self.modell.index(zeile,4),self.lineEdit_plz.text())
        self.modell.setData(self.modell.index(zeile,5),self.lineEdit_ort.text())
        self.modell.setData(self.modell.index(zeile,6),self.lineEdit_telefon.text())
        
        # die Änderungen übernehmen
        self.modell.submitAll()
        
        # eine Meldung ausgeben
        QMessageBox.information(self, "Info", "Die Daten wurden übernommen.")
        
        # alle Felder wieder leeren
        self.lineEdit_vorname.clear()
        self.lineEdit_name.clear()
        self.lineEdit_strasse.clear()
        self.lineEdit_plz.clear()
        self.lineEdit_ort.clear()
        self.lineEdit_telefon.clear()      
    
    def beenden(self):
        # das Formular schließen
        self.close()