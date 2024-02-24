***************************************************************************************************************************




# djangocraft
## _A Powerfull project setup tool_


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

djangocraft is a very powerfull and easy way to set up your Django project

It is really helpful for developers when they are going to start a new project or when they are in hackathons. With a few simple inputs you can set up your whole project in less than 10 seconds and have a pre built authentication with it.

## Features

- With a one line command you can set up your whole project 
- You get a Pre-build Authentication system with just one command
- Authentication system personalized according to user input

Django is a python based web framework and is used by various big companies around the world.


## Tech

djangocraft uses python and a lot of packages like:

- Typer[all]
- Subprocess 
- Shutil 
- os








## Authors

- [@YashRaj](https://github.com/YashRaj1506)


## Documentation

[Documentation](https://linktodocumentation)

commands:

## djangostartauth:

        djangocraft djangostartauth {project_name} {authentication_app_name}

project_name: Enter the name of the project in django

authentication_app_name : Enter the name of the application which you want the authentication part to have

Hit Enter

You are asked for the number of inputs you want to take from user in the registration page 

Enter the number of fields and enter their names (Also ensure they are from below pool of options)

[
 username,
 first_name,
 last_name,
 email,
 age,
]

You get a pre-built authentication according to your field choices. 


## djangoforpro:

        djangocraft djangoforpro {project_name} 

project_name: Enter the name of the project in django

Hit Enter

You get a quick setup for the project.

## Github for project

Source code : https://github.com/YashRaj1506/djangocraft_cli