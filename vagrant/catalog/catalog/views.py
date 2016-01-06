from catalog import app, db
from catalog.models import User, Catagory, CatagoryItem
from flask import (
    Flask,
    url_for,
    render_template,
    redirect,
    request,
    flash,
    jsonify
)


@app.route('/')
def dashboard():
    catagories = Catagory.query.all()
    print catagories
    return render_template(
        'index.html',
        catagories=catagories
    )