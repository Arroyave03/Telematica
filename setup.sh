sudo apt update
sudo apt install docker-compose -y
#Se contruyen los contenedores
sudo docker build -t siataapi:1 -f DockerfileApi .
sudo docker build -t siatapass:1 -f DockerfilePass .
sudo docker build -t siataweb:1 -f DockerfileWeb .
#Se ejecutan los contenedores
sudo docker run -d -p 5000:5000 siataapi:1
sudo docker run -d -p 5001:5001 siatapass:1
sudo docker run -it -p 80:80 siataweb:1