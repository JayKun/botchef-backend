# BotChef
This app uses machine learning to suggest recipes to a user based on the ingredients, preferences, and dietary restrictions that the user has

## The Plan:

### Basic Use Case:
##### 1) Type in the ingredients you have
	- The app is in Android and on the web
	
##### 2) The app sends the list of ingredients to the BotChef server, where they are stored along with the user preferences.
	- The app sends an HTTP GET request to the web server along with a serialized list of ingredients. 
	- The web server returns a JSON response containing a list of recipes ranked. 
	
##### 3) Server finds a list of recipes that can be made with those ingredients
	- Uses database in Django to look up recipes based on ingredients
	- We used the recipe data at this link: https://eightportions.com/datasets/Recipes/
	- We used a naive bayesian classifier to read the ingredients and simplify them into a shopping list
	
##### 4) Server sorts recipes based on the user's preferences, and what most popular.
	- We used a combination of popularity and number of matching ingredients to choose the best recipe
	- We will use originally planned to use the Baidu API to perform suggestions, but then decided to use our own formula
	
##### 5) Server sends top 5 recipes to the app
	- Server sends data over HTTP GET request
	- Recipes sent to app in a JSON file
	
##### 6) User chooses a recipe in the app. The chosen recipe is sent to the server.
	- Chosen recipe data is sent via HTTP GET request
	
##### 7) Server receives the user's chosen recipe, and stores this data for later in the database, and updates the recipe popularity data, and thus the machine learning model.
	- The Django API is used for updating data
	
##### 8) Server can send better recipe suggestions to be displayed next time, using popularity data
	- Server sends suggestion data in an HTTP GET request
	- Suggestion data sent in JSON file





     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Welcome to your Django project on Cloud9 IDE!

Your Django project is already fully setup. Just click the "Run" button to start
the application. On first run you will be asked to create an admin user. You can
access your application from 'https://recipe-recommend-jaykun.c9users.io/' and the admin page from 
'https://recipe-recommend-jaykun.c9users.io/admin'.

## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
## Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

## Support & Documentation

Django docs can be found at https://www.djangoproject.com/

You may also want to follow the Django tutorial to create your first application:
https://docs.djangoproject.com/en/1.9/intro/tutorial01/

Visit http://docs.c9.io for support, or to learn more about using Cloud9 IDE.
To watch some training videos, visit http://www.youtube.com/user/c9ide