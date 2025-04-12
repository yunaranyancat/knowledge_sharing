directory for upcoming phishing workshop

Setting up WEBFMA in KALI VM - KALI 2024.3

# Step 1: Go to Desktop
cd ~/Desktop

# Step 2: Download the ZIP directly using wget
wget https://github.com/yunaranyancat/knowledge_sharing/raw/master/phishing_workshop/webmfa.zip

# Step 3: Unzip the project
unzip webmfa.zip
cd webmfa

# Step 4: Install virtualenv if not already installed
pip install virtualenv

# Step 5: Create a virtual environment
virtualenv venvmfa

# Step 6: Activate the virtual environment
source venvmfa/bin/activate

# Step 7: Install dependencies
pip install -r requirements.txt

# Step 8: Source the environment variables
source .env

## Adjust routing to port 5000
# Redirect HTTP (port 80) to port 5000
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 5000

# Redirect HTTPS (port 443) to port 5000
sudo iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-port 5000


# Step 9: Run the Flask application
python manage.py run --host=0.0.0.0 --cert=cert.pem --key=key.pem

