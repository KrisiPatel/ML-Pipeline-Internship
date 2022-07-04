# ML-Pipeline-Internship

STEPS TO CREATING A FLASK WEB APPLICATION : https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=2474s

1.	Set up an environment
-	Install python and pip
-	Install virtualenv
-	Create a project directory
-	Create a virtual environment
-	Install required packages 
2.	Set up the application
-	From flask import Flask
-	App = Flask(__name__) is used to reference to the file
-	Then create an index root, so when we browse to the URL we don’t immediately just get a 404 error. You set up roots with the app route decorator.
-	Then we are going to have a function for debugging so if any errors occur they will pop up on the web page.
-	Then using the terminal connect to the local host to access this web application.
-	Create more folders : one called templates and one called static.
-	Create a html file to hold the code for the web application.
-	In templates you make another html file to inherit code so you don’t have to keep writing code again and again. E.g ) {% block head %}{% endblock %}
-	In the folder static create the css file.
-	Then we need to create the database and also initialise it in the main file e.g ) app.py.
-	Continue writing you code for the web application now.

STEPS TO DOCKERISATION OF THE FLASK APPLICATION :

1.	Create a directory with the name “Flask-Docker-App”  mkdir Flask-Docker-App 
2.	Navigate to the newly created directory  cd Flask-Docker-App
3.	Create a virtual environment py -3 -m venv venv
4.	Activate the environment  venv\Scripts\activate
5.	Install Flask  pip install Flask
6.	Create the required files touch app.py Dockerfile
7.	Modify the dockerfile
-	Tell the file what syntax to use
-	Tell the file what base image to use
-	Tell docker what directory to use
-	Tell docker to copy the contents of requirements.txt
-	Tell docker to run the flask app as a module
8.	Build the docker image docker build –-tag python-docker .
9.	Run the docker image as a container docker images
10.	Run an image docker run


Minikube Installation on Windows  https://www.youtube.com/watch?v=qQnYrPErXOE
Step 1: Check if virtualisation is supported in your machine
Step 2: Download/Install kubectl, minikube utility and add it to to the local ENV PATH
Step 3: Download/Install a Hypervisor | ORACLE VM BOX
Step 4: Start  Minikube 
Step 5: Create and Expose a container in the Minikube Cluster
Step 6: Test or Access the Container
Step 7: Lab Cleanup

Errors Faced :
-	Step 4: Start Minikube -> the laptop I had was windows 10, for minikube to work I needed hyper-v normally found on “windows turn on and off” but no such option was available there. Another solution was to use windows powershell to install hyper-v using a single line command but that command kept returning the same error of Microsoft-Hyper-V-Tools is unknown. Tried a few more solutions including restarting my laptop and going on BIOS settings however hyper-v was not found there either. Turns out hyper-v can only be installed on windows 10 Pro, Windows Enterprise or Windows Education which would cost a great deal of money.

Solution:
1.	Create a student account with Microsoft Azure
2.	 Select create a resource and go on Kubernetes service and press create
3.	Add any name for resource group of your choice and same name applied for Kubernetes cluster name, also select the region.
4.	Change the node count to anything more than 2. Preferably 3.
5.	After all options are chosen select review and create.
6.	Once deployment is complete select go to resource.
7.	Open up Powershell terminal In Microsoft Azure
8.	Copy the command to clipboard : az aks get-credentials—resource-group testakslab –name testaks
9.	To see how many nodes we have running : Kubectl get nodes 
10.	A container registry would allow you to store container images safely in the cloud for later deployment :
1.	Select create a resource
2.	Select container registry and create
3.	Write the resource group and a registry name that has to be unique.
4.	Review and create once all requirements are checked.
5.	Once deployment is complete select go to resource
6.	Open up PowerShell terminal in Microsoft Azure
7.	git clone https://github.com/KrisiPatel/ML-Pipeline-Internship.git
8.	cd ML-Pipeline-Internship.git
9.	az acr build –image latest –registry testkrisi –file Dockerfile .
10.	touch deployment.yaml -> will create a deployment file
11.	code . -> will open the integrated editor in the cloud shell it will open up the flask app
12.	kubectl apply -f ./deployment.yaml -> to create the file
13.	kubectl get deploy latest  -> to see if deployment is ready.
11.	 To enable the network access we need to add an ingress rule
1.	Open PowerShell on Microsoft Azure
2.	touch service.yaml
3.	code .
4.	kubectl apply -f  ./service.yaml
5.	touch ingress.yaml
6.	code .
