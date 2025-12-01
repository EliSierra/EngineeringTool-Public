import sys
import os
from PyQt6 import QtWidgets, uic
from PyQt6.uic.load_ui import loadUi
from pathlib import Path
from PyQt6.QtWidgets import QPushButton
import Globals as g



#print("Current working directory:", os.getcwd())
CamPath=Path(r"E:\Py Engineering Tool\Engineering-Tool\Tool\CAMs\QT\CAM_Desinger_Widget.ui")


class CAMWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        #CamPath2=Path(__file__).parent/"CAM_Designer_GUI.ui"
        loadUi(CamPath, self)

        self.GraphBot: QPushButton
        self.STEPBot: QPushButton 
        self.CADBot: QPushButton

        ### Action Items ###

        # Graphing button
        from .CAM_Func import CAMPlot
        self.GraphBot.clicked.connect(lambda: CAMPlot(self)) # graph button must be called GraphBot
        self.CADBot.clicked.connect(self.STLSave) # STL button must be called STLBot
        #self.STEPBot.clicked.connect(self.STPSave) # STEP Button must be called STEPBot
        
    def STLSave(self):
        from .CAM_Func import STLFileName, CADFileName

        if not g.ProjectDirectory:
            QtWidgets.QMessageBox.warning(self, "No Project Selected", "Please select or create a project first.")
            return # If a project folder is not selected or created prevent user from useing this feature
        
        filename = CADFileName(self)
        if filename:
            print("Save to:", filename)
            from .CAM_Func import STLGen, CAMPlot, STPGen
            angle,Y,Thickness=CAMPlot(self)
            STPGen(angle, Y, Thickness,filename)

        # Do something with filename, like saving a file
        else:
            print("No file selected.")
        
    def STPSave(self):
        from .CAM_Func import STPFileName

        filename = STPFileName(self)
        if filename:
            print("Save to:", filename)
            from .CAM_Func import STPGen, CAMPlot
            angle,Y,Thickness=CAMPlot(self)
            STPGen(angle, Y, Thickness,filename)

        # Do something with filename, like saving a file
        else:
            print("No file selected.")

        


    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = CAMWidget()
    Widget.show()
    sys.exit(app.exec())

    