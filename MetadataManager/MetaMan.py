from pathlib import Path
from PyQt6.QtWidgets import QLineEdit, QComboBox, QMessageBox
from PyQt6 import QtWidgets
import Globals as g
import json, datetime as dt


def ScanInputs(ui, ToolName=None):

    inputs={}
    for widget in ui.findChildren(QLineEdit):
        name=widget.objectName()
        value=widget.text().strip()
        if value:
            inputs[name] = value
    
    for widget in ui.findChildren(QComboBox):
        name=widget.objectName()
        value=widget.currentText().strip()
        if value:
            inputs[name] = value

    return {
        "Tool": ToolName or ui.objectName(),
        "WidgetObjectName": ui.objectName(),
        "Inputs": inputs
    }

def SaveData(ui, ToolName = None, outputs=None):

    if not g.ProjectDirectory:
        QtWidgets.QMessageBox.warning(ui, "No Project Selected", "Please select or create a project first.")
        return # If a project folder is not selected or created prevent user from useing this feature
    
    MetaFolder = Path(g.ProjectDirectory) / "Metadata"
    MetaFolder.mkdir(exist_ok=True)

    MetaPath=MetaFolder/f"{ToolName}_{dt.datetime.now().strftime('%m-%d-%Y_%H%M%S')}.json"

    if not ToolName:
        ToolName = ui.objectName()

    data={
        "Tool": ToolName,
        "WidgetObjectName": ui.objectName(),
        "Timestamp": dt.datetime.now().strftime("%m-%d-%Y %H:%M:%S"),
        "Inputs": g.Metadata.get("Inputs",{}),
        "Outputs": outputs or {}
    }

    with open(MetaPath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    msgBox = QMessageBox()
    msgBox.setText(f"Metadata saved to{MetaPath}") # want to put message box that says where the metadata was saved and that it was indeed saved
    msgBox.exec()


    return MetaPath

def LoadData(self):

    if not g.ProjectDirectory:
        QtWidgets.QMessageBox.warning(self, "No Project Selected", "Please select or create a project first.")
        return # If a project folder is not selected or created prevent user from useing this feature

    DataFolder = Path(str(g.ProjectDirectory)) / "Metadata"
    FilePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Data", str(DataFolder), "Json Files (*.json)")

    if not FilePath:
        return


    with open(FilePath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    self.Metadata.setWordWrap(True)
    self.Metadata.setText(json.dumps(data,indent=4))
    g.MetadataPath = FilePath


def RunData(mainui):
    
    FilePath = g.MetadataPath
    if not FilePath:
        return
    

    
    with open(FilePath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ToolName = data["Tool"]
    WidgetName = data["WidgetObjectName"]

    TargetWidget = mainui.findChild(QtWidgets.QWidget, WidgetName)

    if not TargetWidget:
        QtWidgets.QMessageBox.warning(mainui, "Metadata Load Error",
                                      f"Could not find widget '{WidgetName}' for tool '{ToolName}'.")
        return
    
    mainui.MainStack.setCurrentWidget(TargetWidget)

    for name, value in data["Inputs"].items():
        textbox = TargetWidget.findChild(QtWidgets.QLineEdit, name)
        if textbox:
            textbox.setText(value)
        combo = TargetWidget.findChild(QtWidgets.QComboBox, name)
        if combo:
            index = combo.findText(value)
            if index >= 0:
                combo.setCurrentIndex(index)
    
def ClearData(self):
    self.Metadata.clear()
    return