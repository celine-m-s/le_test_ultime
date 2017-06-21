

## Run the program

Start by editing `config.py`.

Initialize database:

    FLASK_APP=run.py flask initdb

Re-running this method deletes all data. be careful!

Start a server in debug mode:

    python run.py

Start a server in production mode:

    FLASK_APP=run.py flask run

## TODO
- Problème de couche alpha qui m'empêche d'arrondir les angles de la photo de profil.
- FB share à tester en production
- tests
- production
