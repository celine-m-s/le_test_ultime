from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', page_title='Le test ultime !',
                                         user_image='static/img/profile.png',
                                         user_name='Julio',
                                         )
