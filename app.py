"""Blogly application."""

from flask import Flask, render_template, request, flash, session, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "warriors"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
def render_homepage():
    return redirect('/users')

@app.route("/users")
def render_user_list():
    all_users = User.query.all()
    return render_template('base.html', users=all_users)

@app.route("/users/new", methods=["GET"])
def show_user_form():
    return render_template('new.html')

@app.route("/users/new", methods=["POST"])
def create_and_show_user():
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    img_url = request.form['img-url']
    
    new_user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(new_user)
    db.session.commit()
    
    return redirect('/users')

@app.route("/users/<int:user_id>")
def render_user_info(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('details.html', user=user)
    
@app.route("/users/<int:user_id>/edit")
def show_edit_page():
    pass

@app.route("/users/<int:user_id>/edit", methods=["POST"])
def edit_user_page():
    pass

@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user_instance():
    pass