#!/bin/bash

docker stop ProjectManager2
docker rm ProjectManager2
docker rmi project-manager:latest
docker build -t project-manager:latest .
docker run -d --name ProjectManager2 -p 8080:80 -p 2222:22 -v ./webAPP:/var/www/html project-manager:latest