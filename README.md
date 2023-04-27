# Django Class Based View Todo App

## Setup
To get this repository, run the following command inside your git enabled terminal
```
git clone https://github.com/Armin-WebDev/TodoApp-ClassBased.git
```

## Getting ready
Create an enviroment in order to keep the repo dependencies seperated from your local machine.
```
python -m venv venv
```
Make sure to install the dependencies of the project through the requirements.txt file.
```
pip install -r requirements.txt
```
Once you have installed django and other packages, go to the cloned repo directory and run the following command
```
python manage.py makemigrations
```
This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```
python manage.py runserver
```


## options
And lastly let's make the App run. We just need to start the server now and then we can start using our simple todo App. Start the server by following command
```
python manage.py runserver
```
Once the server is up and running, head over to http://127.0.0.1:8000 for the App.

