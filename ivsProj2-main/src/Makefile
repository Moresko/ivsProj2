.PHONY: help all run test profile pack clean doc 

help:
	@echo "-------------HELP--------------"
	@echo "Type make all to run whole project"
	@echo "Type make run to run a Calculator"
	@echo "Type make tests to run mathLib tests"
	@echo "Type make profiling to run a profiling script"
	@echo "Type make clean to delete all wrong files"
	@echo "Type make pack to zip whole project"
	@echo "Type make doc to generate a documentation"

all:
	sudo apt-get update
	sudo apt-get install python3-pip
	pip3 install numpy
	sudo apt-get install python3-tk
	pip3 install pyinstaller

run:
	python3 calc.py

test:
	python3 mathLibTest.py

profile:
	pip3 install numpy
	python3 stddev.py

pack: doc clean
	mkdir -p ../xkasem02_xmores02_xbotlo01_xkozak20/install 
	cp ../Installer/installCalc.sh ../Installer/installStddev.sh ../xkasem02_xmores02_xbotlo01_xkozak20/install/
	mkdir -p ../xkasem02_xmores02_xbotlo01_xkozak20/doc 
	cp -r html ../xkasem02_xmores02_xbotlo01_xkozak20/doc/
	rm -r html
	mkdir -p ../xkasem02_xmores02_xbotlo01_xkozak20/repo
	rsync -av --exclude=xkasem02_xmores02_xbotlo01_xkozak20 ../ ../xkasem02_xmores02_xbotlo01_xkozak20/repo/
	cd .. && zip -r xkasem02_xmores02_xbotlo01_xkozak20.zip  xkasem02_xmores02_xbotlo01_xkozak20 ../xkasem02_xmores02_xbotlo01_xkozak20
	rm -rf ../xkasem02_xmores02_xbotlo01_xkozak20
clean:
	rm -rf __pycache__
doc:
	doxygen Doxyfile
