if [ "$USER" != "root" ]
	then echo "Please run as root"
	exit
else

  echo "Install Packages"
    sudo apt install xterm -y
    sudo apt install python3 -y
    sudo apt install python3-pip
    pip install guizero
    pip install glob

  echo "git stuff"
    git clone https://github.com/markondej/fm_transmitter
		cd /fm_transmitter
		make GPIO21=1
fi
