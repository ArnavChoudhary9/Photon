@echo off

echo Initializing Setup . . .

echo 1. Setting up Virtual Environment . . .
python -m venv venv
call venv\Scripts\activate.bat
echo ---- Complete

echo 2. Installing Required Libraries . . .
pip install -r requirements.txt
echo ---- Complete

echo 3. Installing PyImGUI . . .
cd Libraries\PyImGUI
python setup.py install
echo ---- Complete

echo 4. Initialization Complete
pause
