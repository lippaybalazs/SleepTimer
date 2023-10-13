RD /S /Q "__pycache__"
RD /S /Q "build"
RD /S /Q "dist"
del SleepTimer.spec

venv\Scripts\python.exe -m eel SleepTimer.py web --onefile --noconsole --icon=web\favicon.ico
