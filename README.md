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
