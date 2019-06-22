# @Savital 22.06.19
# views.py
from app import app
from flask import render_template

@app.route('/')
def render_index(name=None):
    return render_template('index.html', name=name)


@app.route('/about')
def render_about(name=None):
    return render_template('about.html', name=name)
