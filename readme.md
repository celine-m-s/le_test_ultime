## TODO

- [x] Secure config.py
  - [x] Secret key
  - [x] admin email
  - [x] admin password
  - [x] sample config.py.sample then update readme
- [x] Descriptions from a YAML file
- [ ] Description content x 20
- [ ] Fill database with content
- [ ] Image generation: round corners
- [ ] Tests:
  - [ ] Test image generation
  - [ ] Test FB share
  - [ ] Test FB metadata

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

## Bug
Hmmmm je crois comprendre qu'une appli ne peut pas écrire sur le filesystem local dans heroku : https://stackoverflow.com/questions/18552937/store-file-in-directory-tmp-on-heroku-rails
Au fond c'est logique puisque si ton application est distribuée sur plusieurs serveurs, les différents serveurs ne pourront pas accéder au même système de fichiers.
Pour résoudre ce problème je te suggère de stocker les images dans la base de données sous la forme de blobs binaires. Du coup faudra ajouter une route "/image/<id>" qui va renvoyer le contenu de l'image.

[Basic writing in markdown](https://help.github.com/articles/basic-writing-and-formatting-syntax/)
[Emoji Cheat sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet/)
