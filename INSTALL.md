## Install

### Prerequisites

Before you can install the Binary Clock you'll need the following: 

* Raspberry PI with [Raspberry PI OS](https://www.raspberrypi.org/downloads/raspberry-pi-os/) (formally Raspbian) installed. The lite version is just fine as a GUI is not needed for this project. 
* SSH or console access to the Rpi
* A Unicorn Hat


### Installation

These instructions assume you have your Raspberry Pi all ready to go. We are installing things as the default user ```pi```.

1. Install WebIOPi

```

#clone webiopi - this version supports 1,2,3 and Zero
git clone https://github.com/thortex/rpi3-webiopi.git
cd rpi3-webiopi

#install deps
cd dev
./01_setup-required-packages.sh

./03_install_python_dev.sh

./10_make_deb.sh

#install the dpkg files
sudo dpkg -i ~/build.webiopi/python2-webiopi*.deb
sudo dpkg -i ~/build.webiopi/python3-webiopi*.deb

#use python 2
sudo webiopi-select-python 3

#restart the services
sudo systemctl daemon-reload
sudo systemctl restart webiopi

```

2. Install Binary Clock

```

#clone repo
https://github.com/robweber/binary_clock.git
cd binary_clock

sudo apt-get install python3-pip -y

#install dependencies
sudo pip3 install -r requirements.txt

#copy config file
sudo cp webiopi.config /etc/webiopi/config

#generate a new password for web interface
sudo webiopi-passwd

#restart the services
sudo systemctl restart webiopi

```

3. WebIOPi should now be running on http://IP:8000


### Running the Program

When it boots the Binary Clock will start. __please note, you need a network connection as the Raspberry Pi will not remember the system time from one boot to the next__

Log in to the web interface on port 8000 using the username and password created in the installation step. Here you can adjust any settings or set the alarm as defined in the README document. 