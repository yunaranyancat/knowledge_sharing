Setting up WEBFMA in KALI VM - KALI 2025.1a

Step 1: Go to Desktop
```
cd ~/Desktop
```

Step 2: Download the ZIP directly using wget
```
wget https://github.com/yunaranyancat/knowledge_sharing/raw/master/phishing_workshop/webmfa.zip
```
Step 3: Unzip the project
```
unzip webmfa.zip
cd webmfa
```
Step 4 : Install Python 3.11
```
sudo apt-get update

sudo apt install -y wget build-essential libssl-dev zlib1g-dev \
libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev \
libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev \
tk-dev libffi-dev uuid-dev
```
```
cd /tmp                                                         
wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz  
tar -xf Python-3.11.0.tgz                                      
cd Python-3.11.0
```
```
./configure --enable-optimizations
```
```
make -j$(nproc)                                                 
sudo make altinstall
```
python3.11 --version # Check if Python3.11 has been successfully installed
```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.11 1
sudo update-alternatives --config python3
```
```
python3.11 -m ensurepip --upgrade
python3.11 -m pip --version
```
```
cd ~/Desktop
mkdir training
cd training
rm -rf venvmfa
```

Step 5: Create a virtual environment
```
python3.11 -m venv venvmfa
```
Step 6: Activate the virtual environment
```
source venvmfa/bin/activate
```
Step 7: Install dependencies
```
pip install -r requirements.txt
```
Step 8: Source the environment variables
```
source .env
```
Adjust routing to port 5000
Redirect HTTP (port 80) to port 5000
```
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 5000
```
Redirect HTTPS (port 443) to port 5000
```
sudo iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-port 5000
```
Step 9: Run the Flask application
```
python manage.py run --host=0.0.0.0 --cert=cert.pem --key=key.pem
```
