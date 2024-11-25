sh
# Download and Install chromedriver
wget -N https://storage.googleapis.com/chrome-for-testing-public/113.0.5672.0/linux64/chrome-linux64.zip -P ~/
unzip ~/chrome_linux64.zip -d ~/
rm ~/chrome_linux64.zip
sudo mv -f ~/chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod 0755 /usr/local/bin/chromedriver


# Install chrome broswer
curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
apt-get -y update
apt-get -y install google-chrome-stable