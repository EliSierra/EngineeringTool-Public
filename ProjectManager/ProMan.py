from pathlib import Path
from PyQt6.QtWidgets import QFileDialog, QInputDialog
from PyQt6 import QtWidgets
import os
import datetime as dt

import sys

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

import Globals as g


def ChooseFolder(parent=None, title="Select Project Folder"):
    
    folder = QFileDialog.getExistingDirectory(parent, title)

    return folder



def CreateProjectFolder(parent=None):
    folder = ChooseFolder(parent, "Select Location for New Project")
    if not folder:
        return None, None

    ### Create the Standard Folder Layout ###
    
    ProjectName, ok = QtWidgets.QInputDialog.getText(parent, "Project Name", "Enter Project Name:")
    if not ok or not ProjectName.strip():
        return None, None
    
    ProjectPath = Path(folder) / ProjectName.strip()
    ProjectPath.mkdir(parents=True, exist_ok=True)

    g.ProjectDirectory=str(ProjectPath) # update project directory file global variable

    folders= ["Presentations",
        "Order Forms",
        "Documentation/Templates",
        "Calculations",
        "CAD/Layouts",
        "CAD/Assemblies",
        "CAD/Parts",
        "CAD/Final Design",
        "CAD/Drawings",
        "Media",
        "Tests",
        "Electrical + DAQ",
        "Notes",
        "Metadata",
        "Archive",
        "Analysis/Scripts",
        "Analysis/Figures",
        "Software"
    ]
    for f in folders:
        (ProjectPath / f).mkdir(parents=True, exist_ok=True)

    ### Create the ProjectConfig File ###
    configfile = ProjectPath / "ProjectConfig.txt"  
    with open(configfile, "w") as f:
        f.write(f"Project Name = {ProjectName}\n")
        f.write(f"Created = {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    return ProjectPath, ProjectName




def LoadProjectFolder(parent=None):
    folder = ChooseFolder(parent, "Select Project Folder to Load")
    if not folder:
        return None
    
    ProjectPath=Path(folder)
    configfile = ProjectPath/ "ProjectConfig.txt"

    g.ProjectDirectory=str(ProjectPath) # update project directory file global variable
    
    msg=None
    if not configfile.exists():
        msg="This is not a valid project folder"

    return ProjectPath, msg



### Note Creation and Management ###

def SaveNotesAs(self,parent=None):
    
    if not g.ProjectDirectory:
        QtWidgets.QMessageBox.warning(self, "No Project Selected", "Please select or create a project first.")
        return # If a project folder is not selected or created prevent user from useing this feature
    

    NotesName, ok = QtWidgets.QInputDialog.getText(parent, "Notes File Name", "Enter Notes File Name:")
    if not ok or not NotesName.strip():
        return  # user cancelled or gave empty name

    NotesPath=Path(str(g.ProjectDirectory)) / "Notes"
    NotesPath.mkdir(exist_ok=True)
    NotesFile = NotesPath / f"{NotesName}.txt"

    if NotesFile.exists(): # Check to see if the file name already exists 
        reply = QtWidgets.QMessageBox.question(
            parent,
            "Overwrite File?",
            f"A note named '{NotesName}.txt' already exists.\nDo you want to overwrite it?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        if reply == QtWidgets.QMessageBox.StandardButton.No:
            return  


    text= self.Notes.toPlainText()

    with open(NotesFile, "w", encoding="utf-8") as f:
        f.write(f"Project Name = {g.ProjectName}\n")
        f.write(f"Notes Created = {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("\n")
        f.write(text)


    g.CurrentNotePath=str(NotesFile)
    QtWidgets.QMessageBox.information(self, "Notes Saved", f"Notes saved to:\n{NotesFile}")

def SaveNotes(self,parent=None):
    if not g.ProjectDirectory:
        QtWidgets.QMessageBox.warning(self, "No Project Selected", "Please select or create a project first.")
        return

    if not g.CurrentNotePath:
        QtWidgets.QMessageBox.warning(self, "No Active Note", "Please use 'Save Notes As' to create or open a note first.")
        return
    

    text = self.Notes.toPlainText()
    with open(g.CurrentNotePath, "w", encoding="utf-8") as f:
        #f.write(f"Project Name = {g.ProjectName}\n")
        #f.write(f"Modified = {dt.datetime.now().strftime('%m-%d-%Y %H:%M:%S')}\n\n")
        f.write(text)

    QtWidgets.QMessageBox.information(self, "Notes Saved", f"Changes saved to:\n{g.CurrentNotePath}")
    

def ClearNotes(self):
    self.Notes.clear()
    return

def LoadNotes(self):

    if not g.ProjectDirectory:
        QtWidgets.QMessageBox.warning(self, "No Project Selected", "Please select or create a project first.")
        return # If a project folder is not selected or created prevent user from useing this feature
    
    NotesFolder = Path(str(g.ProjectDirectory)) / "Notes"
    FilePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Notes", str(NotesFolder), "Text Files (*.txt)")
    
    if FilePath:
        with open(FilePath, "r", encoding="utf-8") as f:
            content = f.read()
        self.Notes.setPlainText(content)

    g.CurrentNotePath = FilePath


    