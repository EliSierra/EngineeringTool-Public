import sqlite3
import os
import pandas as pd
from pathlib import Path
from difflib import get_close_matches
from typing import List, Optional, Dict, Any

# Directory path of the database
db_path=Path(__file__).parent / "MaterialDatabase.db"

#db_path = Path(r"E:\Py Engineering Tool\Engineering-Tool\(1) Tool\Materials\MaterialDatabase.db")  #Old Path



### List of functions in MatMan.py: ###
# initialize_database(db_path: Path = db_path) # initializes the database (NOT FOR EXTERNAL USE)

# readmat        # Reads material properties from database based on material name input

# matexists      # checks to see if the material name exists in the database

# allmats        # Returns a list of all materials (NOT FOR EXTERNAL USE)
 
# matsearch      # Returns a list of close matches based on text input

# strstrip       # Simplifies strings (NOT FOR EXTERNAL USE)

# excelSearch    # Searches Excel file for properties and returns a dictionary (NOT FOR EXTERNAL USE)

# MatWrite       # Writes properties from Excel file to database

# ExcelFileName  # Opens file dialog to select Excel File


def initialize_database(db_path: Path = db_path): # Initializes the database and creates the materials table if it doesn't exist
    with sqlite3.connect(str(db_path)) as con:
        cur = con.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS materials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            density REAL,
            ultimate_strength REAL,
            yield_strength REAL,
            youngs_modulus REAL,
            poisson_ratio REAL,
            shear_modulus REAL,
            shear_strength REAL,
            electrical_resistivity REAL,
            CTE REAL,
            specific_heat REAL,
            thermal_conductivity REAL
        )
        """)


def readmat(name, db_path: Path = db_path): # Reads material properties from database and returns them as a list of tuples
    if not db_path.exists():
        initialize_database()

    with sqlite3.connect(str(db_path)) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM materials WHERE name = ?", (name,))
        return cur.fetchall()


def matexists(name, db_path: Path = db_path): # Checks to see if material exists in database
    if not db_path.exists():
        initialize_database()
    with sqlite3.connect(str(db_path)) as con:
        cur = con.cursor()
        cur.execute("SELECT 1 FROM materials WHERE name = ? LIMIT 1", (name,))
        return cur.fetchone() is not None # Returns True if material exists, False otherwise


def allmats(db_path: Path = db_path): # Returns a list of all materials in the database
    if not db_path.exists():
        initialize_database()    
    with sqlite3.connect(str(db_path)) as con:
        cur = con.cursor()
        cur.execute("SELECT name FROM materials")
        return [row[0] for row in cur.fetchall()]


def matsearch(Search, db_path: Path = db_path): # Searches for material in database and returns a list of close matches
    if not db_path.exists():
        initialize_database()    
    limit=10
    names=allmats(db_path)
    searchLower = Search.lower()

    #substring matches anywhere in the name
    substringMatches = [n for n in names if searchLower in n.lower()]

    #fuzzy matches (get_close_matches) if needed
    if len(substringMatches) < limit:
        fuzzy_matches = get_close_matches(Search, names, n=limit, cutoff=0.5)
        # merge lists without duplicates
        substringMatches.extend(m for m in fuzzy_matches if m not in substringMatches)




    return substringMatches[:limit]


def strstrip(s: str):
    return s.strip().lower()


def excelSearch(excel_path): # Searches an excel file for material properties and returns them as a dictionary
    data=pd.read_excel(excel_path, header=None)
    
    words = {
        'density': ['density'],
        'ultimate_strength': ['tensile strength, ultimate', 'ultimate tensile strength'],
        'yield_strength': ['tensile strength, yield', 'yield strength'],
        'youngs_modulus': ['modulus of elasticity', 'youngs modulus'],
        'poisson_ratio': ['poissons ratio', "poisson's ratio"],
        'shear_modulus': ['shear modulus'],
        'shear_strength': ['shear strength'],
        'electrical_resistivity': ['electrical resistivity'],
        'CTE': ['cte', 'coefficient of thermal expansion', 'cte, linear'],
        'specific_heat': ['specific heat capacity', 'specific heat'],
        'thermal_conductivity': ['thermal conductivity']
    }

    results: Dict[str, Any] = {}

    results.setdefault('name', data.iat[0,0])  # Assuming the title is in the first cell

    # the idea behind this for loop is to go through each row of excel and at each row go through each property in the words disctionary and see if any of the variants are in the first column of excel
    for _, row in data.iterrows(): # Iterate through each row in the DataFrame
        a=row[0] # First column of excel
        b=row[1] # Second column of excel

        # Check to see if first coumn contains labels and then match to words dictionary and write results to results
        if isinstance(a, str): # Ensure 'a' is a string to avoid errors
            a_stripped = strstrip(a) # get rid of spaces and cases
            for key, variants in words.items(): # Loop through each property and its variants, uses the keys in the word dictionary to cycle through material properties to return values
                if any(strstrip(variant) in a_stripped for variant in variants): # Check if any variant matches the stripped string
                    results.setdefault(key, b) # Store the value in results dictionary
                    
    return results


def MatWrite(excel_path, db_path: Path = db_path): # Writes material properties from excel file to database
        if not db_path.exists():
            initialize_database()        
        epath=Path(excel_path)
        if not epath.exists():
            raise FileNotFoundError(f"Excel file not found: {epath}")
        properties=excelSearch(epath)
        name=properties.get('name')
        SqlInsert=("INSERT INTO materials (name, density, ultimate_strength, yield_strength, youngs_modulus, poisson_ratio, shear_modulus, shear_strength, electrical_resistivity, CTE, specific_heat, thermal_conductivity) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
        values=(
            name,
            properties.get('density'),
            properties.get('ultimate_strength'),
            properties.get('yield_strength'),
            properties.get('youngs_modulus'),
            properties.get('poisson_ratio'),
            properties.get('shear_modulus'),
            properties.get('shear_strength'),
            properties.get('electrical_resistivity'),
            properties.get('CTE'),
            properties.get('specific_heat'),
            properties.get('thermal_conductivity')
        )
        if matexists(name, db_path):
            return None
        else:
            with sqlite3.connect(str(db_path)) as con:
                cur = con.cursor()
                cur.execute(SqlInsert, values)
                return cur.lastrowid



def ExcelFileName(parent=None):
    from PyQt6.QtWidgets import QFileDialog

    filename, _ = QFileDialog.getOpenFileName(
        parent,
        "Select Excel Material File",
        "",
        "Excel Files (*.xlsx *.xls);;All Files (*)"
    )
    return filename
