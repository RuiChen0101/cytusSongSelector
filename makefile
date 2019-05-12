.PHONY: directories clean

all:

ui: src/ui/mainui.ui src/ui/songScreen.ui
	pyuic5 ./src/ui/mainui.ui -o ./src/ui/controlPenalUI.py
	pyuic5 ./src/ui/songScreen.ui -o ./src/ui/songScreenUI.py

exe: ttesScoreBoard.py src/ui/mainwindow.py src/ui/songScreen.py
	pyinstaller -w ./ttesScoreBoard.py

clean:
	rm -rf dist build __pycache__
stat:
	wc src/*
