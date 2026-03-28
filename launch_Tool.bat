@echo off
REM ============================================================
REM Portable Engineering Tool Launcher
REM Auto-detects drive letter, activates Miniconda, runs tool
REM ============================================================

REM Get the directory containing this batch file
set "TOOL_DIR=%~dp0"
set "DEV_ROOT=%TOOL_DIR%.."

REM Activate Miniconda via condabin (most reliable for portable conda)
if exist "%DEV_ROOT%\Miniconda\condabin\conda.bat" (
    call "%DEV_ROOT%\Miniconda\condabin\conda.bat" activate
) else if exist "%DEV_ROOT%\Miniconda\Scripts\activate.bat" (
    call "%DEV_ROOT%\Miniconda\Scripts\activate.bat"
) else if exist "%DEV_ROOT%\miniconda3\condabin\conda.bat" (
    call "%DEV_ROOT%\miniconda3\condabin\conda.bat" activate
) else if exist "%TOOL_DIR%.venv\Scripts\activate.bat" (
    call "%TOOL_DIR%.venv\Scripts\activate.bat"
) else (
    echo ERROR: No Python environment found.
    echo Looked in: %DEV_ROOT%\Miniconda\
    pause
    exit /b 1
)

REM Check if PyQt6 is installed, install deps if missing
python -c "import PyQt6" 2>nul
if errorlevel 1 (
    echo First run detected - installing dependencies...
    pip install -r "%TOOL_DIR%requirements.txt"
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies.
        pause
        exit /b 1
    )
    echo Dependencies installed successfully.
)

REM Run the tool
python "%TOOL_DIR%Main GUI\MainRun.py"

REM Keep window open on error
if errorlevel 1 pause
