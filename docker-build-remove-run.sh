sudo docker build -t flaskyieldapi:1.0 .
sudo docker rm flask-yield-api
sudo docker run -p 5000:5000 --name flask-yield-api flaskyieldapi:1.0
