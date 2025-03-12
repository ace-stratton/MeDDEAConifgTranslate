@echo off
REM Change directory to where this .bat file is located.
cd /d "%~dp0"

REM Now run your Python script from here:
python TranslateFiles.py

REM Pause so you can see any console output before the window closes
pause