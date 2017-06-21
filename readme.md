
Start by editing `config.py`.

Initialize database:

    FLASK_APP=run.py flask initdb

Re-running this method deletes all data. be careful!

Start a server in debug mode:

    python run.py

Start a server in production mode:

    FLASK_APP=run.py flask run

## Questions

- Comment protéger des informations essentielles ? => un fichier de configs qu'on peut après retrouver autrement sur le serveur.
- Est-ce vraiment intéressant d'utiliser Flask Security dans notre cas ?
- Pas de PATCH et PUT ??
- Problème de couche alpha qui m'empêche d'arrondir les angles de la photo de profil.
- FB share à tester en production

## Img

- http://pillow.readthedocs.io/en/4.1.x/handbook/tutorial.html#reading-and-writing-images
- http://pillow.readthedocs.io/en/4.1.x/handbook/concepts.html#concept-modes
- https://developers.facebook.com/docs/graph-api/reference/profile-picture-source/
- og:image https://developers.facebook.com/docs/sharing/webmasters#markup
- partage FB https://developers.facebook.com/docs/sharing/reference/share-dialog
- settings app: https://developers.facebook.com/apps/1967148823570310/settings/
- Flask wtf : https://flask-wtf.readthedocs.io/en/stable/api.html
- Flask quickstart : http://flask.pocoo.org/docs/0.12/quickstart/#accessing-request-data
- Jinja : http://jinja.pocoo.org/docs/2.9/templates/#if
- ORM : http://docs.sqlalchemy.org/en/rel_1_1/orm/tutorial.html
- watermark : http://www.thecodingcouple.com/watermark-images-python-pillow-pil/
- fBone : https://github.com/imwilsonxu/fbone/blob/master/fbone/user/models.py
- Flask Security : https://pythonhosted.org/Flask-Security/
- http://ondras.zarovi.cz/sql/demo/
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars
- http://www.science-emergence.com/Articles/S%C3%A9lectionner-une-partie-dune-image-avec-PIL-de-python/

## TODO

- Ajouter du contenu dans dashboard/admin
- $(...).jqBootstrapValidation is not a function ()

Un blueprint se comporte comme une app sans être une app. Centraliser alors dans __init__().

diff avec flask :
- pas de blueprint dans Flask.
- dans Flask, les vues et les URL sont au même endroit. Dans Django, on a un fichier url et pas un objet app.

Flask :
- pas qu'un serveur web ! un serveur web, c'est nginx et apache. nginx est très allégé (proxy). Y'a moyen de faire plein de choses côté serveur. Il peut faire des appels à une API. Récupérer des données depuis l'api pour répondre à une requête.
- Dans django, pas jinja. C'est un système spécifique à Django. Macco c'est la folie ! Tu peux faire tout et n'importe quoi avec (très dur à déguguer).
