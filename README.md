WEBSTACK PORTFOLIO PROJECT for ALX SE Africa
MINALEX Todo Flask Web Application


# Todo Flask App

![Todo App Logo](https://github.com/Obianuju23/MINALEX/blob/main/shots/homepage.PNG?raw=true)

## Overview

The Todo Flask App is a powerful task management tool designed to streamline your daily activities and enhance productivity. It provides a convenient, one-stop solution for users to organize tasks, discuss concerns, and find quick resolutions to their pending to-do items.

## Key Features

- **Efficient Task Management:** Seamlessly organize and prioritize your tasks for enhanced productivity.
- **Collaborative Environment:** Foster collaboration by discussing tasks and sharing updates with team members.
- **Swift Resolutions:** Quickly resolve pending issues and tasks to stay on top of your commitments.
- **User-Friendly Interface:** Intuitive design for a seamless and enjoyable task management experience.

## How It Works

1. **Task Creation:**
   Easily create and manage tasks with just a few clicks.

2. **Discussion Forum:**
   Engage in discussions with team members to get insights and updates on tasks.

3. **Prioritization:**
   Prioritize tasks based on urgency and importance.

4. **Task Completion:**
   Mark tasks as complete when they are done.

## Getting Started

1. **Installation:**
   Clone the repository and install dependencies.

   ```bash
   git clone https://github.com/your-username/todo-flask-app.git
   cd todo-flask-app
   pip install -r requirements.txt
# Todo Flask App

![Todo App Logo](logo.png)

## Overview

The Todo Flask App is a powerful task management tool designed to streamline your daily activities and enhance productivity. It provides a convenient, one-stop solution for users to organize tasks, discuss concerns, and find quick resolutions to their pending to-do items.

## Key Features

- **Efficient Task Management:** Seamlessly organize and prioritize your tasks for enhanced productivity.
- **Collaborative Environment:** Foster collaboration by discussing tasks and sharing updates with team members.
- **Swift Resolutions:** Quickly resolve pending issues and tasks to stay on top of your commitments.
- **User-Friendly Interface:** Intuitive design for a seamless and enjoyable task management experience.

## How It Works

1. **Task Creation:**
   Easily create and manage tasks with just a few clicks.

2. **Discussion Forum:**
   Engage in discussions with team members to get insights and updates on tasks.

3. **Prioritization:**
   Prioritize tasks based on urgency and importance.

4. **Task Completion:**
   Mark tasks as complete when they are done.

## Getting Started

1. **Installation:**
   Clone the repository and install dependencies.

   ```bash
   git clone https://github.com/your-username/todo-flask-app.git
   cd todo-flask-app
   pip install -r requirements.txt











 as envisaged is an online Veterinary System that will be designed for pet owners to have a one-time system to give swift attention to their pets, online assistance to discuss concerns and as well give quick resolutions to pets’ disturbing issues as reported by the pet owners.

From this project, users can get a feel of what the web application is all about by having a "Logged Out Experience" and the routes that can be assessed by the user or customer includes:

The landing page
The About page
The contact page
The services page
DEVELOPMENT TOOLS
To develop this application, we have to state some tools that will be used for the software development:

Flask
SQLAlchemy
MySQL DBMS
Bootstrap CSS library
JQuery JavaScript library
First we will create a virtual environment where flask will be installed.

But we need to have Python and Virtual Environment installed

Install virtual Environment
sudo apt update
sudo apt upgrade -y
sudo apt install virtualenv -y
Creating a Virtual Environment
python3 -m venv .ovetcare
Activating the virtual Environment
# on a unix based operating system
source .ovetcare/bin/activate
(.ovetcare) /home/nerd $

# on a windows based operating system
.ovetcare\Scripts\activate.bat
(.ovetcare) C:\Users\nerd>
Deactivating a Virtual Environment
(.ovetcare) /home/nerd $ deactivate
INSTALLING DEPENDENCIES
We have the following dependencies saved in a file called requirements.txt:

bcrypt==4.0.1
click==8.0.4
dataclasses==0.8
dnspython==2.2.1
email-validator==1.3.1
Flask==2.0.3
Flask-Bcrypt==1.0.1
Flask-Login==0.5.0
Flask-SQLAlchemy==2.5.1
Flask-WTF==1.0.1
greenlet==2.0.2
idna==3.4
importlib-metadata==4.8.3
itsdangerous==2.0.1
Jinja2==3.0.3
MarkupSafe==2.0.1
pkg_resources==0.0.0
SQLAlchemy==1.4.49
typing_extensions==4.1.1
Werkzeug==2.0.3
WTForms==3.0.0
zipp==3.6.0
this was achieved using

(.ovetcare) /home/nerd $ pip freeze > requirements.txt
To install all these requirements do the following:

Activate the virtual environment
/home/nerd $ source .ovetcare/bin/activate

(.ovetcare) /home/nerd $
Install the dependencies
(.ovetcare) /home/nerd $ pip install -r requirements.txt
RUNNING THE APPLICATION
To run the O-Vet Care application using command line, do the following:

Step One
(.ovetcare) /home/nerd $ python app.py
OR

Step Two
(.ovetcare) /home/nerd $ FLASK_APP=app.py
(.ovetcare) /home/nerd $ FLASK_DEBUG=1
(.ovetcare) /home/nerd $ flask run
Both will give you the output:

* Serving Flask app 'ovet_care' (lazy loading)
* Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: on
* Running on all addresses.
WARNING: This is a development server. Do not use it in a production deployment.
* Running on http://172.21.168.105:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 280-470-183
