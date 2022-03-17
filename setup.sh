if [ "$USER" != "root" ]
	then echo "Please run as root"
	exit
else

  echo "Install Packages"
    sudo apt install xterm
    sudo apt install python3
    pip install guizero
    pip install glob

  echo "git stuff"
    git clone https://github.com/markondej/fm_transmitter
		cd /fm_transmitter
		make GPIO21=1
fi
