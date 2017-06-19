from flask import render_template, url_for, request, redirect, flash
from flask_security import Security, login_required

from app import app
from .models import db, Content
from .forms import ContentForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', page_title='Le test ultime !', \
                                         user_image='static/img/profile.png', \
                                         user_name='Julio', \
                                         fb_app_id=app.config['FB_APP_ID'])

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/contents/new', methods=['GET', 'POST'])
@login_required
def new_content():
    content = Content('A description', 0)
    form = ContentForm()

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

@app.route('/contents')
@login_required
def contents():
    contents = Content.query.all()
    total = len(contents)
    return render_template('contents/index.html', contents=contents, total=total)


#
#
# @app.route('/contents/<id>/update')
# @login_required
# def update_content(id):
#     return render_template('contents/form.html')
#
# @app.route('/contents/<id>/delete')
# @login_required
# def delete_content(id):
#     return render_template('contents/form.html')
