# @Savital 22.06.19
# views.py
from app import app
from flask import render_template

@app.route('/')
def render_main(name=None):
    return render_template('main.html', name=name)
