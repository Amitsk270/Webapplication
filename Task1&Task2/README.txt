Task1 and Task2
How to setup and deploy the applications using docker-compose? please follow the steps below.
1).First we need install the docker for deploying an web and database containers.
2).Please follow the below steps for installing the docker.
A).Set up Docker's apt repository.
  command - # Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

B).Install the Docker packages.
  command- sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin

C).Install the docker compose
  command- sudo apt install docker-compose

D).Verify the docker compose with the below command.
   command - docker-compose --version     ## if you face any issue related python dependencies , please install the dependencies which i have mentioned below.

3).Once we install the docker packages and docker compose package , now we need to install the python dependencies which are required for the docker-compose.
when i was installing the docker-compose 1.29.2 it was asking some missing python dependencies , to avoid that issue we need to install the python dependencies.
4).Below are the commands which used to install the python dependencies.
sudo apt-get install --reinstall python3.12               ##(First, try reinstalling Python to ensure all components are included)
sudo apt-get install python3-pip
sudo apt-get install python3-venv                         ##(Ensure you have the venv package for creating virtual environments).

5).If you face any user permission denied issue when you are trying the deploy the compose file. just you can try removing and re-adding your user to the docker group , please find the below command.
sudo gpasswd -d $USER docker
sudo usermod -aG docker $USER

if python error and user error does not occurs then we can skip that 4 and 5th point.

6).After making changes to group memberships, log out and then log back in to apply the changes. You can also run the below command.

command - newgrp docker

7)please verify docker socket and that should look like this.(srw-rw---- 1 root docker 0 date /var/run/docker.sock).

8).Make sure that all necessary files are present.(app.py , Dockerfile , requirements.txt , docker-compose.yml). once these files are present we can run the below command to deploy the application and the database.
command = docker-compose up --build -d                  ##this will make the two containers up , one is for web and other is for MySQL database.
Make sure that containers are up and running , Once the containers are up and running please test the application features.

A).To add anything into the database please go to browser and type the below command.(TASK1)
command = http://localhost:35622/add-item             #this will asks our input what needs to be added into database , please enter anything and submit it. once you submit it basically that input will be added to your backend database.(it uses the POST API)--(TASK1)
B).Once you add some item into database even we can check what is there in that database using http://localhost:35622/xyz/items command , that basically uses the GET API which is written inside the application code.
command = http://localhost:35622/xyz/items            # this will display the items which are present in the database.
C).To access the application go browser and run the below command to access the application.(TASK2)
command = http://localhost:35622/xyz                  # with this you can access the application.

Please refer the document where have attached the screenshots with proper output for the above tasks.



1.A short description on what the app does and how it works?
The application is a web service created with Flask that works with a MySQL database to manage a list of items. It has a RESTful API, which provides specific URLs for adding new items and retrieving existing ones. The app uses SQLAlchemy to simplify database interactions, and it connects to the database using a special environment variable. Additionally, there’s a simple HTML form that lets users add items easily through a web page.

2.Setting Up and Deploying the Application with Docker Compose?
To set up and run the application using Docker Compose, start by making sure you have Docker and Docker Compose installed on your system. Then, create a file named docker-compose.yml that includes the settings for both the Flask app and the MySQL database. The Flask app (referred to as "web") will be built using a Dockerfile, while the MySQL service (called "db") will run in a container with specific settings for the database and a health check to confirm it's ready.
Once you have your docker-compose.yml file ready, go to the folder where this file is located and run the command docker-compose up --build -d. This will build and start both the Flask app and the MySQL database. They will be able to communicate with each other easily since they are on the same network defined in the configuration.





