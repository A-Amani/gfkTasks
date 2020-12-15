
For the sake of automation, all the commands (including initialization of db and queries) are being run uppon "$ docker-compose up -d" for a new container. 
A more practical approach would be to only run the initialization commands in upping stage, and the quesries through the "$ docker exec ..." 
