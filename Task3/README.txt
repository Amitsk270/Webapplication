Task3.
how to setup and deploy the whole application in K8s? please follow the below steps.
1).Once we setup minikube environment , please start the minikube with command = minikube start.
2).setup the docker environment in minikube , please enter the below command.
  command = eval $(minikube docker-env)         ##This command sets up your terminal to use the Docker daemon inside Minikube instead of the local Docker daemon.
3).please make sure that necessary files are present for building the docker image.(app.py, requirements.txt, Dockerfile,)
4).Need to build the docker image for the application in the minikube docker environment. please use the below command.
  command = docker build -t flask:test .
 -- once you build the docker image for the application please verify using the docker images command in the minikube environment.(docker images)- flask image should be present.
Make sure that mysql-deployment.yml , hpa.yml , application.yml are present.
5).deploy the MySQL pod.
   command = kubectl apply -f mysql-deployment.yml    # wait till the pod comes up and even the MySQL service should be created.
6).Deploy the application manifest.
   command = kubectl apply -f application.yml         # wait till the pod comes up and even the nodeport services will be created.
7).Enable the hpa in minikube setup.(to setup an hpa in minikube setup please run the below command.)
   command = kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml      # check the metric-server pod is up and running.
   Ensure Metrics Server Configuration is Correct:
        If you installed the metrics-server without any custom configurations, you might need to add flags to allow it to accept self-signed certificates.

Edit the metrics-server deployment:
command = kubectl edit deployment metrics-server -n kube-system

Find the container args section and add the following arguments.  
- --kubelet-insecure-tls
- --kubelet-preferred-address-types=InternalIP


8).once that setup of metric-server is done then please apply the HPA for pod autoscaling.
   command = kubectl apply -f hpa.yml                 #this will apply the hpa for that particular deployment.

Make sure that all pods are up and running , Once the pods are up and running please test the application features.

9).Make sure that you take the minikube ip and add that into sudo vi /etc/hosts to access the application.
Now I am accessing the application without the localhost as minikube will use his own network, so I have taken minikube ip and added in the sudo vi /etc/hosts  and then I am accessing the application.
command = minikube ip
adding in entry in the hosts file = minikubeip amitapplication

A).To do operation with the database please go to browser and type the below command.(POST API)
command = http://amitapplication:30622/add-item             #this will ask our input that needs to be added into database , please enter anything and submit it. once you submit it basically that input will be added to your backend database.(it uses the POST API)
B).Once you add some item into database even we can check what is there in that database using http://amitapplication:30622/xyz/items command , that basically uses the GET API which is written inside the application code.
command = http://amitapplication:30622/xyz/items            # this will display the items which are present in the database.
C).To access the application go browser and run the below command to access the application.
command = http://amitapplication:30622/xyz                  # with this you can access the application.

Even i have attached the screenshots of MySQL database from backend.(please refer the attached screenshots in the document of task3)

Please refer the document where have attached the screenshots with proper output for the above tasks and even i have mentioned how to access the application with localhost by port-forwarding method this is just a temporary solution.(please refer the attached screenshots in the document of task3)



1. How the Web Application Talks to the Database?
The Flask application connects to the MySQL database using an environment variable called DATABASE_URL. This variable has a connection string that includes the database driver and the login details, like username and password. It uses the service name mysql-service to find the MySQL database within the Kubernetes cluster, making it easy for the app to locate it without worrying about changing IP addresses. The connection uses port 3306, which is the standard port for MySQL, ensuring all data is sent and received correctly.

2. How the Web Application is Exposed to the Outside World?
The Flask application is made available to the outside world using a Kubernetes service called NodePort. This allows anyone to access the app by connecting to a specific port (in this case, 30622) on node.When users send traffic to minikubeip:30622, it gets directed to the app running inside Kubernetes.


3. How Auto-Scaling is Configured?
Auto-scaling in Kubernetes is done using a tool called the Horizontal Pod Autoscaler (HPA). This tool automatically adjusts the number of application pods based on how much CPU or memory they are using. For example, you can set it to keep CPU usage around 50% and allow the number of pods to go from 1 to 5 as needed. This means if there’s a lot of traffic, it will create more pods, and if traffic is low, it will reduce the number. The HPA checks usage regularly, helping keep the application responsive while also saving costs.

HPA
1.I have also tested the HPA for this application by adding load on the pod so that extra pods will be created if CPU crosses mentioned threshold.(please refer the attached screenshots in the document of task3.)
2.To create the load just login to pod and try to create some load.
  login command = kubectl exec -it podname -- bash
  command = for i in {1..1000000}; do touch "file_$i.txt"; done   #this command will create the load.
3.once the load is created the extra pods will be created.








