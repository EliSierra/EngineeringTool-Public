
import os, sys
from pathlib import Path
os.add_dll_directory(str(Path(__file__).resolve().parents[1].parent / "Miniconda" / "Library" / "bin"))

import sys
import os
from pathlib import Path
import datetime as dt
import json

### Import PyQt Libraries ###
from PyQt6.QtWidgets import (
    QWidget, QMainWindow, QApplication, QPushButton, QLineEdit, QLabel,
    QCompleter, QToolBox, QVBoxLayout, QHBoxLayout, QPlainTextEdit,
    QTableWidget, QTableWidgetItem, QHeaderView, QStackedWidget,
    QFrame, QGridLayout, QSizePolicy, QMessageBox
)
from PyQt6 import QtWidgets, uic, QtGui
from PyQt6.uic.load_ui import loadUi
from PyQt6.QtCore import Qt, QStringListModel, QTimer

### Add the project root to Python path ###
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

### Import custom sub functions, classes and widgets ###
from CAMs.CAM_SubClass import CAMWidget
from Materials.MatRun import MaterialWidget
from ProjectManager.ProMan import CreateProjectFolder, LoadProjectFolder, SaveNotesAs, SaveNotes, LoadNotes, ClearNotes
from MetadataManager.MetaMan import LoadData, RunData, ClearData
import Globals as g

### Portable paths - resolved relative to this file's location ###
_gui_dir = Path(__file__).resolve().parent       # .../Main GUI/
_project_root = _gui_dir.parent                  # .../EngineeringTool-Public-main/

MainPath = _gui_dir / "Main.ui"
logo = _gui_dir / "Media" / "SierraTechOG.png"
stylePath = _gui_dir / "style.qss"

### Tool Links ###
BeamPath = _project_root / "Beams" / "Beam Calculator .xlsx"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(MainPath, self)

        ### Load external stylesheet (Task 7) ###
        if stylePath.exists():
            with open(stylePath, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())

        ### Logo SetUp ###
        self.SierraTech: QLabel
        self.SierraTech.setPixmap(
            QtGui.QPixmap(str(logo)).scaled(
                225, 90,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

        ### ---- Task 4: Sidebar QToolBox ---- ###
        self._build_sidebar_toolbox()

        ### ---- Task 5: Metadata QTableWidget ---- ###
        self._build_metadata_table()

        ### ---- Task 6: Notes QPlainTextEdit ---- ###
        self._build_notes_panel()

        ### Center Widget Setup ###
        self.MainStack: QStackedWidget
        self.cam_widget = CAMWidget()
        self.mat_widget = MaterialWidget()
        self.MainStack.addWidget(self.cam_widget)
        self.MainStack.addWidget(self.mat_widget)

        ### Connect sidebar buttons ###
        self.CAMCall.clicked.connect(lambda: self.MainStack.setCurrentWidget(self.cam_widget))
        self.MaterialCall.clicked.connect(lambda: self.MainStack.setCurrentWidget(self.mat_widget))

        self.NewProjectBot.clicked.connect(lambda: CreateDisplay(self))
        self.OpenProjectBot.clicked.connect(lambda: LoadDisplay(self))

        self.SaveNotesAs.clicked.connect(lambda: SaveNotesAs(self))
        self.LoadNotes.clicked.connect(lambda: LoadNotes(self))
        self.SaveNotes.clicked.connect(lambda: SaveNotes(self))
        self.ClearNotes.clicked.connect(lambda: ClearNotes(self))

        self.ClearData.clicked.connect(lambda: ClearData(self))
        self.ImportData.clicked.connect(lambda: self._load_metadata())
        self.RunData.clicked.connect(lambda: RunData(self))

        self.BeamCall.clicked.connect(OpenBeamCalculator)

        ### Task 5: Disable metadata action buttons initially ###
        self._set_metadata_buttons_enabled(False)

    # ---- Task 4: Build collapsible sidebar with QToolBox ---- #
    def _build_sidebar_toolbox(self):
        """Replace flat button list with a QToolBox grouped by category."""
        # Find the sidebar column (column 0-1 in the grid)
        # We'll create a QToolBox and insert it, hiding the original section labels/frames
        self.sidebarToolBox = QToolBox()
        self.sidebarToolBox.setObjectName("sidebarToolBox")
        self.sidebarToolBox.setMaximumWidth(230)

        # --- Project section ---
        project_widget = QWidget()
        project_layout = QVBoxLayout(project_widget)
        # Reparent existing buttons into the toolbox sections
        self.OpenProjectBot.setParent(project_widget)
        self.NewProjectBot.setParent(project_widget)
        proj_row = QHBoxLayout()
        proj_row.addWidget(self.OpenProjectBot)
        proj_row.addWidget(self.NewProjectBot)
        project_layout.addLayout(proj_row)
        project_layout.addStretch()
        self.sidebarToolBox.addItem(project_widget, "Project")

        # --- Useful Tools section ---
        tools_widget = QWidget()
        tools_layout = QVBoxLayout(tools_widget)
        for btn in [self.ODRIVECall, self.pushButton_2, self.pushButton_3, self.pushButton_4]:
            btn.setParent(tools_widget)
            btn.setMaximumWidth(16777215)  # Remove max width constraint
            tools_layout.addWidget(btn)
        tools_layout.addStretch()
        self.sidebarToolBox.addItem(tools_widget, "Useful Tools")

        # --- Calculators section ---
        calc_widget = QWidget()
        calc_layout = QVBoxLayout(calc_widget)
        for btn in [self.BeamCall, self.CAMCall]:
            btn.setParent(calc_widget)
            btn.setMaximumWidth(16777215)
            calc_layout.addWidget(btn)
        calc_layout.addStretch()
        self.sidebarToolBox.addItem(calc_widget, "Calculators")

        # --- Databases section ---
        db_widget = QWidget()
        db_layout = QVBoxLayout(db_widget)
        for btn in [self.MaterialCall, self.KBECall]:
            btn.setParent(db_widget)
            btn.setMaximumWidth(16777215)
            db_layout.addWidget(btn)
        db_layout.addStretch()
        self.sidebarToolBox.addItem(db_widget, "Databases")

        # Hide old section labels and separator frames
        for widget_name in ['Calculatorslbl', 'DataBaseLbl', 'UsefulToolslbl',
                           'frame', 'frame_3', 'frame_4', 'frame_8']:
            w = self.findChild(QWidget, widget_name)
            if w:
                w.hide()

        # Insert toolbox into grid at the sidebar position (rows 3-22, cols 0-1)
        self.gridLayout.addWidget(self.sidebarToolBox, 3, 0, 20, 2)

    # ---- Task 5: Build metadata table ---- #
    def _build_metadata_table(self):
        """Replace QLabel Metadata display with QTableWidget for structured viewing."""
        self.MetadataTable = QTableWidget()
        self.MetadataTable.setObjectName("MetadataTable")
        self.MetadataTable.setColumnCount(2)
        self.MetadataTable.setHorizontalHeaderLabels(["Field", "Value"])
        self.MetadataTable.horizontalHeader().setStretchLastSection(True)
        self.MetadataTable.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeMode.ResizeToContents
        )
        self.MetadataTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.MetadataTable.setAlternatingRowColors(True)

        # Replace the old Metadata QLabel in the grid
        old_meta = self.findChild(QLabel, "Metadata")
        if old_meta:
            old_meta.hide()
        # Insert table where the old label was (row 2, col 5, span 12 rows x 2 cols)
        self.gridLayout.addWidget(self.MetadataTable, 2, 5, 12, 2)

        # Keep self.Metadata pointing to something for backward compat with MetaMan
        self.Metadata = self.MetadataTable

    def _set_metadata_buttons_enabled(self, enabled):
        """Enable/disable Import, Clear, Run buttons based on data state."""
        self.ClearData.setEnabled(enabled)
        self.RunData.setEnabled(enabled)

    def _load_metadata(self):
        """Wrapper around LoadData that also updates the table display."""
        LoadData(self)
        # After loading, check if metadata was populated
        if g.MetadataPath:
            self._populate_metadata_table(g.MetadataPath)
            self._set_metadata_buttons_enabled(True)

    def _populate_metadata_table(self, filepath):
        """Populate the QTableWidget with JSON metadata."""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Flatten the JSON for table display
            rows = []
            for key, value in data.items():
                if isinstance(value, dict):
                    for sub_key, sub_val in value.items():
                        rows.append((f"{key}.{sub_key}", str(sub_val)))
                else:
                    rows.append((str(key), str(value)))

            self.MetadataTable.setRowCount(len(rows))
            for i, (field, val) in enumerate(rows):
                self.MetadataTable.setItem(i, 0, QTableWidgetItem(field))
                self.MetadataTable.setItem(i, 1, QTableWidgetItem(val))

        except Exception as e:
            print(f"Error populating metadata table: {e}")

    # ---- Task 6: Notes panel improvements ---- #
    def _build_notes_panel(self):
        """Replace QTextEdit with QPlainTextEdit for better performance."""
        old_notes = self.findChild(QtWidgets.QTextEdit, "Notes")
        if old_notes:
            # Create QPlainTextEdit replacement
            self.NotesEdit = QPlainTextEdit()
            self.NotesEdit.setObjectName("Notes")

            # Copy content if any
            if old_notes.toPlainText():
                self.NotesEdit.setPlainText(old_notes.toPlainText())

            # Replace in the grid (row 18, col 5, span 7 rows x 2 cols)
            old_notes.hide()
            self.gridLayout.addWidget(self.NotesEdit, 18, 5, 7, 2)

            # Point self.Notes to the new widget for backward compat
            self.Notes = self.NotesEdit

    def _auto_save_notes(self):
        """Auto-save notes if a note file is active (called on project switch)."""
        if g.CurrentNotePath and hasattr(self, 'Notes'):
            try:
                text = self.Notes.toPlainText()
                with open(g.CurrentNotePath, "w", encoding="utf-8") as f:
                    f.write(text)
            except Exception as e:
                print(f"Auto-save notes failed: {e}")


### Functions ###

def CreateDisplay(self):
    """Display active project directory on new project creation, with auto-save."""
    # Auto-save current notes before switching (Task 6)
    self._auto_save_notes()

    ProjectPath, g.ProjectName = CreateProjectFolder(self)

    if ProjectPath:
        self.ActiveFile.setText(f"Active Project Directory: {str(ProjectPath)} ")
        self.ProjectTitle.setText(f"Project: {g.ProjectName}")
        # Reset metadata state for new project
        self._set_metadata_buttons_enabled(False)
        self.MetadataTable.setRowCount(0)


def LoadDisplay(self):
    """Display active project directory on project open, with auto-save."""
    # Auto-save current notes before switching (Task 6)
    self._auto_save_notes()

    result = LoadProjectFolder(self)
    if result:
        ProjectPath, msg = result
        if msg:
            QMessageBox.warning(self, "Invalid Project", msg)
        else:
            self.ActiveFile.setText(f"Active Project Directory: {str(ProjectPath)} ")
            g.ProjectName = Path(ProjectPath).name
            self.ProjectTitle.setText(f"Project: {g.ProjectName}")
            # Reset metadata state for loaded project
            self._set_metadata_buttons_enabled(False)
            self.MetadataTable.setRowCount(0)


def OpenBeamCalculator():
    """Open Beam Calculator spreadsheet."""
    path_str = str(BeamPath)
    if os.path.exists(path_str):
        os.startfile(path_str)
    else:
        QMessageBox.warning(None, "File Not Found", f"Could not locate:\n{path_str}")


### Run and Show the GUI ###
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Widget = MainWindow()
    Widget.show()
    sys.exit(app.exec())
