#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

# Install Nginx if it not already installed
if ! [ -x "$(command -v nginx)" ]; then
	sudo apt update
	sudo apt install -y nginx

fi

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

sudo echo "<html>
	<head></head>
	<body>
		<h1>Holberton School</h1>
	</body>
	</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link, remove it if it already exists
if [ -L /data/web_static/current ]; then
	rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Changing the ownership of /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
