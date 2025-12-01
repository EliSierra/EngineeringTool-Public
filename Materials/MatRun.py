import sys
import os
from PyQt6.QtWidgets import QWidget
from PyQt6 import QtWidgets, uic
from PyQt6.uic.load_ui import loadUi
from pathlib import Path
from PyQt6.QtWidgets import QPushButton, QLineEdit, QLabel, QCompleter
from PyQt6.QtCore import Qt, QStringListModel, QTimer
from .MatMan import matsearch, MatWrite, ExcelFileName, readmat


MatPath = Path(__file__).parent / "MaterialWidget.ui"


#MatPath=Path(r"E:\Py Engineering Tool\Engineering-Tool\(1) Tool\Materials\MaterialWidget.ui")


class MaterialWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi(MatPath, self)

        self.Search: QPushButton #button that searches database for material based on search bar text

        self.MaterialAdd: QPushButton #button that adds material to database based on excel file path from filesearch button
        self.FileSearch: QPushButton #button that finds excel file
        
        self.SearchBar: QLineEdit #text input for material search
        self.FileBar: QLineEdit #line to display file path

        self.Results: QLabel #label that displays search results

        # Hook up buttons
        self.Search.clicked.connect(self.search_material)
        self.MaterialAdd.clicked.connect(self.add_material)
        self.FileSearch.clicked.connect(self.ExcelName)

        # Hook up completer for search bar
        self.model = QStringListModel()
        self.completer = QCompleter(self.model, self)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        self.completer.setFilterMode(Qt.MatchFlag.MatchContains)        
        self.SearchBar.setCompleter(self.completer)

        # Timer to delay search updates
        self._search_timer = QTimer()
        self._search_timer.setSingleShot(True)
        self._search_timer.timeout.connect(lambda: self.update_completer_matches(self.SearchBar.text()))

        self.SearchBar.textChanged.connect(lambda _: self._search_timer.start(200))

# When the user picks something from the completer
        self.completer.activated.connect(self.on_completion_selected)

        # text change triggers search update
        #self.SearchBar.textChanged.connect(self.update_completer_matches)

    def update_completer_matches(self, text):
        text=text.strip()
        if len(text) < 2:
            self.model.setStringList([])
            return

        matches = matsearch(text)

        # prevent recursive textChanged calls while updating
        self.SearchBar.blockSignals(True)
        self.model.setStringList(matches)
        self.SearchBar.blockSignals(False)

    def on_completion_selected(self, text):
        # Optional: do something when a completion is chosen
        # e.g. auto-run the search or just leave it
        self.SearchBar.setText(text)

    def GhostCompleter(self): # No Longer Used but was useful at some point is is kept around for reference
        text = self.SearchBar.text()
        if len(text)<2: #will not start looking for matches until 2 characters are typed
            return
        
        matches = matsearch(text)

        completer = QCompleter(matches)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.SearchBar.setCompleter(completer)
        


    def search_material(self): # Needs to search for material and display results in results label
        query = self.SearchBar.text().strip() # get text from search bar

        if not query:
            return

        results = readmat(query)
        self.Results.clear() # clear the Results label
        if not results:
            self.Results.setText(f"No results found for '{query}'.")
            return

        try:
            formatted = "\n".join([f"{col}: {val}" for col, val in zip(
                ["ID", "Name", "Density (kg/m³)", "Ultimate Strength (Pa)", "Yield Strength (Pa)", "Young's Modulus (Pa)", 
                 "Poisson's Ratio", "Shear Modulus (Pa)", "Shear Strength (Pa)", "Electrical Resistivity (Ohm·m)", 
                 "Coefficient of Thermal Expansion (1/K)", "Specific Heat (J/(kg·K))", "Thermal Conductivity (W/(m·K))"],
                results[0]
            )])
            self.Results.setText(formatted)


        except Exception as e:
            print("Error formatting results:", e)
            self.Results.setText(f"Error displaying results: {e}")

    def add_material(self):
        path = self.FileBar.text().strip()
        self.FileBar.setText("Successfully added material!")
        if not path:
            self.FileBar.setText("no file selected.")
            return
        MatWrite(path)

    def ExcelName(self):
        file=ExcelFileName(self)
        if file:
            self.FileBar.setText(file)
        else:
            self.FileBar.setText("no file selected.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = MaterialWidget()
    Widget.show()
    sys.exit(app.exec())


