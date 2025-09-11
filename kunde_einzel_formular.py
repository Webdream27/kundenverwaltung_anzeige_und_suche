""" ************************************************
Das Formular für die Einzeldarstellung
************************************************""" 

# die Module importieren
from PyQt5.QtWidgets import QMainWindow, QDataWidgetMapper
from PyQt5.QtSql import QSqlTableModel

# das Formular importieren
from kunde_einzel import Ui_KundeEinzel

# eine Klasse für den Dialog
# sie erbt von QMainWindow und Ui_KundeEinzel
class KundeEinzel(QMainWindow, Ui_KundeEinzel):
    # die magische Methode __init__()
    def __init__(self):
        # die magische Methode __init__() der übergeordneten Klasse aufrufen
        super().__init__()
        
        # die Methode setupUi() aufrufen
        self.setupUi(self)
        
        # die Verbindung herstellen
        self.verbindung_herstellen()
        # die Daten mappen
        self.daten_mappen()
        
        # Aufgabe 1: Statusleiste initial anzeigen
        self.updateStatus()

    # Aufgabe 1: Methode zum Aktualisieren der Statusleiste
    def updateStatus(self):
        total = self.modell.rowCount()                      # Y = Gesamtzahl
        current = self.mapper.currentIndex() + 1            # X = aktueller Datensatz
        if total == 0:
            text = "Datensatz 0 von 0"
        else:
            text = f"Datensatz {current} von {total}"

        # Direkt die StatusBar-Instanz nutzen
        self.statusBar.showMessage(text)

    def verbindung_herstellen(self):
        # die Aktionen verbinden
        self.actionGanz_nach_vorne.triggered.connect(self.ganz_nach_vorne)
        self.actionEinen_nach_vorne.triggered.connect(self.einen_nach_vorne)
        self.actionEinen_nach_hinten.triggered.connect(self.einen_nach_hinten)
        self.actionGanz_nach_hinten.triggered.connect(self.ganz_nach_hinten)
        self.actionL_schen.triggered.connect(self.loeschen)

    def daten_mappen(self):
        # ein Modell erstellen
        self.modell = QSqlTableModel()
        # die Tabelle setzen
        self.modell.setTable("kunden")
        # die Daten beschaffen
        self.modell.select()
        
        # die Verbindungen zwischen den Widgets und den Daten herstellen
        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.modell)
        self.mapper.addMapping(self.lineEdit_ID, 0)
        self.mapper.addMapping(self.lineEdit_vorname, 1)
        self.mapper.addMapping(self.lineEdit_name, 2)
        self.mapper.addMapping(self.lineEdit_strasse, 3)
        self.mapper.addMapping(self.lineEdit_plz, 4)
        self.mapper.addMapping(self.lineEdit_ort, 5)
        self.mapper.addMapping(self.lineEdit_telefon, 6)      
      
        # die Änderungen sollen automatisch übernommen werden
        self.mapper.setSubmitPolicy(QDataWidgetMapper.AutoSubmit)
        
        # zum ersten Datensatz gehen
        self.mapper.toFirst()

    # Slots mit Status-Update
    def ganz_nach_vorne(self):
        self.mapper.toFirst()
        self.updateStatus()

    def einen_nach_vorne(self):
        self.mapper.toPrevious()
        self.updateStatus()

    def einen_nach_hinten(self):
        self.mapper.toNext()
        self.updateStatus()

    def ganz_nach_hinten(self):
        self.mapper.toLast()
        self.updateStatus()

    def loeschen(self):
        index = self.mapper.currentIndex()
        self.modell.removeRow(index)
        self.mapper.submit()
        self.modell.select()

        if index < self.modell.rowCount():
            self.mapper.setCurrentIndex(index)
        else:
            self.mapper.toLast()

        self.updateStatus()
