cd src
sudo apt-get -y install python3-pip
sudo apt install python3-venv
python3 -m venv flask
source flask/bin/activate
pip install Flask
python3 flask_backend.py
