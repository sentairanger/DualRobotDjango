# DualRobotDjango

## Introduction

Last time I used Flask to create a web server app to control two robots and can be expanded to control more if desired. However, I decided to take another challenge and try making a similar app using the Django web framework. It was a lot more challenging due to the fact that no one else has even attempted controlling a robot using Django so I decided to take the plunge. So I will show you how I did it and also how you can run it on your own. 

## Getting Started

To get started I will show you the hardware I used and give you some alternatives as well.
  
### Hardware

* My two Raspberry Pi Robots Linus and Torvalds
* My Ubuntu 20.04 desktop to run all the code and to test the app.
* Optional: Android Phone and Tablet to run the app remotely. 


### Software

* Raspberry Pi OS Lite On Linus
* Raspberry Pi OS on Torvalds
* The django framework and virtualenv. To install execute the following command: `pip3 install virtualenv`. To create a virtual environment run `python3 -m virtualenv venv`. To activate the environment run `source venv/bin/activate`. If using Windows, run the `activate.exe` executable in the venv directory.
* Make sure `gpiozero`, `django` and `pigpio` are installed in the new environment by running `pip install django gpiozero pigpio`. 


## Django File Structure Rundown

Before I explain the file structure it's necessary to explain how to create a Django project and app. First, create a project within the environment by running `django-admin startproject [projectname]`. Then go into the directory where you'll find the `manage.py` file and the new project directory. To test the project, run `python manage.py runserver` and it'll tell you to run the app at the localhost address. Point your browser to the link and you should be greeted with a message that django installed successfully. To create an app, stay in the same directory and run `python manage.py startapp [appname]`. Then a new app directory will be created. Within this directory these files will be automatically created:

* `manage.py`: created to manage the main application and project.
* `__init.__.py`: This is treated as a package and created by default
* `settings.py`: Where all the settings including the allowed hosts and applications allowed to run.
* `urls.py`: All links to the project are found here and the links are functions to call from the `views.py` file.
* `wsgi.py`: This is used if WSGI will be deployed.
* `admin.py`: Used to access the app as an admin. 
* `models.py`: Used to store all the models.
* `tests.py`: Where all the tests are stored
* `views.py`: Where all the app views are stored.


## Code Explanation

* In the `dualrobotapp` directory, the code controls both robots using the mouseup and mousedown functions. It can be accessed from another browser by altering the allowed hosts section in `settings.py` and making sure the firewall doesn't block port 8000. To run the code run `python manage.py runserver 0.0.0.0:8000`. 
* In `dualrobottouch` it's exactly the same thing except that it uses the touchstart and touchend commands to control the robots. This can be run on any phone or tablet. 



## Running Apps on Platforms

### Linux

Make sure to follow the steps I indicated above in the software section. 

### Windows

First make sure python is installed first and then create a virtual environment using the same steps in the software section.

### Mac OS

Follow the exact same steps as indicated on the software section.

### Android and iOS

The `dualrobottouch` file can be used to run the robots on either Android or iOS. However, Pythonista or Pydroid3 can be used to run the code on the phone or tablet directly. This prevents having to use another desktop to run the code. 

## Pictures

* App design on Ubuntu 
![Linux](https://github.com/sentairanger/DualRobotDjango/blob/main/linux.png)

* App design on Windows
![windows](https://github.com/sentairanger/DualRobotDjango/blob/main/Django.PNG)
