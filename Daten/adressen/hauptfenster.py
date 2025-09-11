""" ************************************************
Adressverwaltung
************************************************""" 

# die Module importieren
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QTableView  # Aufgabe 2: Module importieren QInputDialog, QTableView

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel   # Aufgabe 2: Module importieren QSqlTableModel

# die Formulare importieren
from mainwindow import Ui_MainWindow
from kunden_formular import NeuerKunde
from kunden_liste import Kundenliste
from kunde_einzel_formular import KundeEinzel


# eine Klasse für das Hauptfenster
# sie erbt von QMainWindow und Ui_MainWindow
class Hauptfenster(QMainWindow, Ui_MainWindow):
    # die magische Methode __init__()
    def __init__(self):      
        # die magische Methode __init__() der übergeordneten Klasse aufrufen
        super().__init__()
        
        # die Methode setupUi() aufrufen
        self.setupUi(self)
        
        # die Verbindung zur Datenbank herstellen
        self.datenbank = QSqlDatabase.addDatabase("QSQLITE")
        # den Datenbanknamen setzen
        self.datenbank.setDatabaseName("adressen.db")
        # konnte die Datenbank geöffnet werden?
        # wenn nicht, geben wir eine Meldung aus und brechen ab
        if self.datenbank.open() == False:
            QMessageBox.error(self, "Fehler", "Die Datenbank konnte nicht geöffnet werden.")
            exit()

        
        # die Schaltflächen verbinden
        self.button_listenanzeige.clicked.connect(self.listenanzeige)
        self.button_einzelanzeige.clicked.connect(self.einzelanzeige)
        self.button_neuer_eintrag.clicked.connect(self.neuer_eintrag)
        
        # Aufgabe 2: Suchfunktion
        self.button_suche.clicked.connect(self.suche)
        
        # das Widget anzeigen
        self.show()
        
    # Aufgabe 2: Suchfunktion implementieren
    def suche(self):
        nachname, ok = QInputDialog.getText(self, "Suche", "Nachnamen eingeben:")
        if not ok or not nachname.strip():
            return

        modell = QSqlTableModel(self, self.datenbank)
        modell.setTable("kunden")
        modell.setFilter(f"nachname = '{nachname}'")
        modell.select()

        view = QTableView()
        view.setWindowTitle(f"Suchergebnis für '{nachname}'")
        view.setModel(modell)
        view.resizeColumnsToContents()
        view.show()

        # Referenz sichern, damit das Fenster offen bleibt
        self._search_view = view
        
    # die Slots
    def listenanzeige(self):
        self.kundenliste = Kundenliste()
        self.kundenliste.show()
    
    def einzelanzeige(self):
        self.kundeneinzel_formular = KundeEinzel()
        self.kundeneinzel_formular.show()
    
    def neuer_eintrag(self):
        self.neuer_kunde_formular = NeuerKunde()
        self.neuer_kunde_formular.show()
        
    # die überschriebene Methode für Schließen
    def closeEvent(self, event):
        # die Methode der übergeordneten Klasse aufrufen
        super().closeEvent(event)
        self.datenbank.close()
    
# eine Instanz der Klasse QApplication erzeugen
app = QApplication([])
# eine Instanz unseres Fensters erzeugen
fenster = Hauptfenster()

# die Anwendung ausführen
app.exec()