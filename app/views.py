from flask import render_template, url_for, request, redirect, flash
from flask_security import Security, login_required

from app import app
from .models import db, Content
from .forms import ContentForm
import random

@app.route('/')
@app.route('/index')
def index():
    description = "Toi, tu sais comment utiliser la console ! Jamais à court d'idées pour réaliser ton objectif, tu es déterminé-e et persévérant-e. Tes amis disent d'ailleurs volontiers que tu as du caractère et que tu ne te laisses pas marcher sur les pieds. Un peu hacker sur les bords, tu aimes trouver des solutions à tout problème. N'aurais-tu pas un petit problème d'autorité ? ;-)"
    return render_template('index.html', page_title='Le test ultime !', \
                                         user_image='static/img/profile.png', \
                                         user_name='Julio', \
                                         fb_app_id=app.config['FB_APP_ID'],\
                                         blur=True,
                                         description=description)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('admin/index.html')

@app.route('/dashboard/contents/new', methods=['GET', 'POST'])
@login_required
def new_content():
    form = ContentForm()
    content = Content('A description', 'Male')
    if form.validate_on_submit():
        c = Content(form.description.data, form.sex.data)
        db.session.add(c)
        db.session.commit()
        flash('Une nouvelle description a été ajoutée avec succès ! Description : {} Sexe : {}'.format(form.description.data, form.sex.data))
        return redirect(url_for('new_content', method='GET'))

    return render_template('contents/form.html', \
                           path=url_for('new_content'), \
                           title='Nouvelle description', \
                           method='POST',
                           form=form,
                           description=content.description,
                           sex=content.sex)

@app.route('/dashboard/contents')
@login_required
def contents():
    contents = Content.query.all()
    total = len(contents)
    return render_template('contents/index.html', contents=contents, total=total)

@app.route('/dashboard/contents/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def update_content(id):
    content = Content.query.get(id)
    form = ContentForm()
    if form.validate_on_submit():
        content.description = form.description.data
        content.sex = form.sex.data
        db.session.add(content)
        db.session.commit()
        flash('La description a bien été modifiée ! Description : {} Sexe : {}'.format(form.description.data, form.sex.data))
        return redirect(url_for('contents'))

    return render_template('contents/form.html',
                           path=url_for('update_content', id=id),
                           title='Mise à jour',
                           method='POST',
                           form=form,
                           description=content.description,
                           sex=content.sex)

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
    return redirect(url_for('contents'))

###############################
########## Test ###############
###############################

def find_content(sex):
    contents = Content.query.filter(Content.sex == sex).all()
    ids = [content.id for content in contents]
    the_one = Content.query.get(random.choice(ids))
    return the_one


@app.route('/result')
def result():
    content = find_content('female')
    description = content.description
    first_name = request.args['first_name']
    image = 'http://graph.facebook.com/' + request.args['id'] + '/picture?type=normal';
    # get  'http://graph.facebook.com/' + response.id + '/picture?type=normal';
    return render_template('result.html', page_title='Le test ultime !', \
                                   user_image=image, \
                                   user_name=first_name, \
                                   fb_app_id=app.config['FB_APP_ID'], \
                                   description=description)
