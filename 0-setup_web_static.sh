#!/usr/bin/env bash
# setting up my web server for the deployment of web static

# if not installed, install nginx
sudo apt-get update
sudo apt-get install -y nginx

#create folder
sudo mkdir -p /data/web_static/shared /data/web_static/releases/test

#create fake html file
echo "<html>
  <head>
  </head>
  <body>
  Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html

# symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#ownership
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "26i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx start
