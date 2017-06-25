## TODO

- [ ] Secure config.py
  - [ ] Secret key
  - [ ] admin email
  - [ ] admin password
- [ ] Description content x 20
- [ ] Fill database with content
- [ ] Image generation: round corners
- [ ] Tests:
  - [ ] Test image generation
  - [ ] Test FB share
  - [ ] Test FB metadata

## Run the program

Start by editing `config.py`.

Initialize database:

    FLASK_APP=run.py flask initdb

Re-running this method deletes all data. be careful!

Start a server in debug mode:

    python run.py

Start a server in production mode:

    FLASK_APP=run.py flask run
