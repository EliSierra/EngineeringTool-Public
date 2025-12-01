
import sys
import os
from pathlib import Path
import datetime as dt

### Import PyQt Libraries ###
from PyQt6.QtWidgets import QWidget
from PyQt6 import QtWidgets, uic, QtGui
from PyQt6.uic.load_ui import loadUi
from PyQt6.QtWidgets import QPushButton, QLineEdit, QLabel, QCompleter
from PyQt6.QtCore import Qt, QStringListModel, QTimer

### Add the project root to Python path ###
project_root = Path(__file__).resolve().parents[1]  # this goes up one folder to 'Tool'
sys.path.append(str(project_root))

### Import custom sub functions, classes and widgets ###
from CAMs.CAM_SubClass import CAMWidget
from Materials.MatRun import MaterialWidget
from ProjectManager.ProMan import CreateProjectFolder, LoadProjectFolder, SaveNotesAs, SaveNotes, LoadNotes, ClearNotes
from MetadataManager.MetaMan import LoadData, RunData, ClearData
import Globals as g


MainPath=Path(r"E:\Py Engineering Tool\Engineering-Tool\Tool\Main GUI\Main.ui") # Path of the MAINGUI ui file

logo=Path(r"E:\Py Engineering Tool\Engineering-Tool\Tool\Main GUI\Media\SierraTechOG.png")

### Tool Links ###
BeamPath=Path(r"E:\Py Engineering Tool\Engineering-Tool\Tool\Beams\Beam Calculator .xlsx")

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(MainPath, self)

        ### Logo SetUp ###
        self.SierraTech: QLabel #label that displays Sierra Tech logo
        self.SierraTech.setPixmap(QtGui.QPixmap(str(logo)).scaled(225, 90, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

        ### Button Set Up ###
        self.BeamCall: QPushButton #button that opens Beam GUI
        self.CAMCall: QPushButton #button that opens CAM GUI
        self.MaterialCall: QPushButton #button that opens Material GUI
        self.OpenProjectBot: QPushButton #button that opens project folder
        self.NewProjectBot: QPushButton #button that creates new project folder
        self.SaveNotesAs: QPushButton #button that saves notes into a new directory
        self.LoadNotes: QPushButton #button that loads notes
        self.SaveNotes: QPushButton #button that saves notes into existing directory
        self.ClearNotes: QPushButton #button that clears the notes textbox
        self.ImportData: QPushButton #button that imports metadata
        self.ClearData: QPushButton #button that clears data from metadata textbox
        self.RunData: QPushButton #button that calls metadata and then opens correct tool and then inputs data



        ### Label Set Up ###
        self.ActiveFile: QLabel #Label that displays active project file directory
        self.ProjectTitle: QLabel #Label that displays the active project title
        self.Metadata: QLabel #Label that displays the Metadata

        ### Center Widget Setup ###
        self.MainStack: QtWidgets.QStackedWidget #stacked widget that holds different GUIs

        self.cam_widget=CAMWidget() #define CAM widget
        self.mat_widget=MaterialWidget() #define Material widget

        self.MainStack.addWidget(self.cam_widget) #add CAM widget to stack
        self.MainStack.addWidget(self.mat_widget) #add Material widget to stack

        ### Call Buttons ###

        self.CAMCall.clicked.connect(lambda: self.MainStack.setCurrentWidget(self.cam_widget))
        self.MaterialCall.clicked.connect(lambda: self.MainStack.setCurrentWidget(self.mat_widget))

        self.NewProjectBot.clicked.connect(lambda: CreateDisplay(self))
        self.OpenProjectBot.clicked.connect(lambda: LoadDisplay(self))

        self.SaveNotesAs.clicked.connect(lambda: SaveNotesAs(self))
        self.LoadNotes.clicked.connect(lambda: LoadNotes(self))
        self.SaveNotes.clicked.connect(lambda: SaveNotes(self))
        self.ClearNotes.clicked.connect(lambda: ClearNotes(self))

        self.ClearData.clicked.connect(lambda: ClearData(self))
        self.ImportData.clicked.connect(lambda: LoadData(self))
        self.RunData.clicked.connect(lambda: RunData(self))

        self.BeamCall.clicked.connect(OpenBeamCalculator)

        

### Functions ###

# Function to display active project directory on new project creation
def CreateDisplay(self):
    ProjectPath,g.ProjectName=CreateProjectFolder(self)

    if ProjectPath:
        self.ActiveFile.setText(f"Active Project Directory: {str(ProjectPath)} ")
        self.ProjectTitle.setText(f"Project: {g.ProjectName}")

# Function to display active project directory on project open
def LoadDisplay(self):
    result = LoadProjectFolder(self)
    if result:
        # LoadProjectFolder currently returns (path, msg)
        ProjectPath, msg = result
        if msg:
            QtWidgets.QMessageBox.warning(self, "Invalid Project", msg)
        else:
            self.ActiveFile.setText(f"Active Project Directory: {str(ProjectPath)} ")
            g.ProjectName = Path(ProjectPath).name 

            self.ProjectTitle.setText(f"Project: {g.ProjectName}")

# Function to Open Beam Calcualtor
def OpenBeamCalculator():
    path_str = str(BeamPath)
    if os.path.exists(path_str):
        os.startfile(path_str)
    else:
        QtWidgets.QMessageBox.warning(None, "File Not Found",f"Could not locate:\n{path_str}")

### Run and Show the GUI ###
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = MainWindow()
    Widget.show()
    sys.exit(app.exec())
