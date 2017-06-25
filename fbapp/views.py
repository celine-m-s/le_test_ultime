from flask import Flask, render_template, url_for, request, redirect, flash
from flask_security import login_required

from .models import db, Content
from .forms import ContentForm
from .utils import find_content, OpenGraphImage

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

@app.route('/')
@app.route('/index')
def index():
    if 'img' in request.args.keys():
        og_image = request.args['img']
        share_link = url_for('index', img=og_image, _external=True)
    else:
        og_image = url_for('static', filename='tmp/sample.jpg', _external=True)
        share_link = url_for('index', _external=True)

    description = "Toi, tu sais comment utiliser la console ! Jamais à court d'idées pour réaliser ton objectif, tu es déterminé-e et persévérant-e. Tes amis disent d'ailleurs volontiers que tu as du caractère et que tu ne te laisses pas marcher sur les pieds. Un peu hacker sur les bords, tu aimes trouver des solutions à tout problème. N'aurais-tu pas un petit problème d'autorité ? ;-)"
    og_description = 'Tu veux savoir qui tu es vraiment ? Fais le test ultime !'
    return render_template('index.html', page_title='Le test ultime !',
                                         user_image='static/img/profile.png',
                                         user_name='Julio',
                                         fb_app_id=app.config['FB_APP_ID'],
                                         blur=True,
                                         description=description,
                                         og_url=share_link,
                                         og_image=og_image,
                                         og_description=og_description)

@app.route('/dashboard')
@login_required
def dashboard():
    all_contents = Content.query.all()
    total = len(all_contents)
    return render_template('admin/index.html',
                            all_contents=all_contents,
                            total=total,
                            root_url=url_for('dashboard'))

@app.route('/dashboard/contents/new', methods=['GET', 'POST'])
@login_required
def new_content():
    form = ContentForm()
    content = Content('A description', 'Male')
    if form.validate_on_submit():
        c = Content(form.description.data, form.gender.data)
        db.session.add(c)
        db.session.commit()
        flash('Une nouvelle description a été ajoutée avec succès ! Description : {} Sexe : {}'.format(
            form.description.data, form.gender.data
        ))
        return redirect(url_for('new_content', method='GET'))

    return render_template('contents/form.html', \
                           path=url_for('new_content'), \
                           title='Nouvelle description', \
                           method='POST',
                           form=form,
                           description=content.description,
                           gender=content.gender,
                           root_url=url_for('dashboard'))

@app.route('/dashboard/contents/<int:uid>/edit', methods=['GET', 'POST'])
@login_required
def update_content(uid):
    content = Content.query.get(uid)
    form = ContentForm()
    if form.validate_on_submit():
        content.description = form.description.data
        content.gender = form.gender.data
        db.session.add(content)
        db.session.commit()
        flash('La description a bien été modifiée ! Description : {} Sexe : {}'.format(
            form.description.data, form.gender.data
        ))
        return redirect(url_for('dashboard'))

    return render_template('contents/form.html',
                           path=url_for('update_content', id=uid),
                           title='Mise à jour',
                           method='POST',
                           form=form,
                           description=content.description,
                           gender=content.gender,
                           root_url=url_for('dashboard'))

@app.route('/dashboard/contents/<int:id>/delete')
@login_required
def delete_content(id):
    content = Content.query.get(id)
    db.session.delete(content)
    db.session.commit()
    if Content.query.get(id) is None:
        flash('La description a bien été supprimée')
    else:
        flash("Une erreur s'est produite. Merci de recommencer.")
    return redirect(url_for('dashboard'))

###############################
########## Test ###############
###############################

@app.route('/result')
def result():
    gender = request.args['gender'] # returns male, female, other
    content = find_content(gender)
    description = content.description
    first_name = request.args['first_name']
    uid = request.args['id']
    profile_pic = 'http://graph.facebook.com/' + uid + '/picture?type=large'
    fb_img = OpenGraphImage(first_name, profile_pic, uid, description)
    og_image = fb_img.location
    share_link = url_for('index',
                        img=fb_img.location,
                        _external=True)

    return render_template('result.html', page_title='Voici qui je suis vraiment !', \
                                   user_image=fb_img.cover_location, \
                                   user_name=first_name, \
                                   fb_app_id=app.config['FB_APP_ID'], \
                                   description=description, \
                                   og_image=og_image, \
                                   og_url=share_link, \
                                   og_description='Toi aussi, fais le test !')
