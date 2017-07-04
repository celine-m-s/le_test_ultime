## TODO

Another stupid Facebook app which will tell you who you are truly.

![This is how it looks like](https://raw.githubusercontent.com/celine-m-s/flask_test_app/master/animation.gif)

Written in French but feel free to make a pull request to translate it into another language. We all want to know who we are!

## Start the program

### Install dependencies & create a database

Run `pip install -r requirements.txt` to install all the dependencies.

Create a new database called `app.db` located at the root of your project.

:information_source: The project uses SQLite3 by default. You can change that in `config.py`.

### Sensitive data

Fork this project then open `config.py.sample`. Replace the data with your own. Rename it `config.py`.  

### Add data

Open `data/fbapp.yaml` and add as many descriptions as you'd like!

Then create the database running this command:

    FLASK_APP=run.py flask initdb

:warning: Re-running this method deletes all data. be careful!

### Run the server

Start a server in debug mode:

    python run.py

Start a server in production mode:

    FLASK_APP=run.py flask run

Start a Flask shell:

    FLASK_APP=run.py flask

## Contribute

This is a work in progress project!

Feel free to contribute making a pull request. I'll be very happy to read it!
