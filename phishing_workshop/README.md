directory for upcoming phishing workshop

Setting up WEBFMA

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

# Step 9: Run the Flask application
python manage.py run --host=0.0.0.0

