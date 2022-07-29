# Setup (Ubuntu 22LTS)
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9
sudo apt-get install python3.9-dev python3.9-venv
python3.9 -m venv sandbox
source sandbox/bin/activate
func host start