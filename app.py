"""Blogly application."""

from flask import Flask, render_template, request, flash, session, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "warriors"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
def render_homepage():
    posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    return render_template("posts_homepage.html", posts=posts)

@app.errorhandler(404)
def page_not_found(err):
    """Show 404 Page"""
    
    return render_template('404.html'), 404

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
def show_edit_page(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)

@app.route("/users/<int:user_id>/edit", methods=["POST"])
def edit_user_page(user_id):
    user = User.query.get_or_404(user_id) 
    user.first_name = request.form['first-name']
    user.last_name = request.form['last-name']
    user.img_url = request.form['img-url']
    
    db.session.add(user)
    db.session.commit()
    
    return redirect(f'/users/{user.id}') 

@app.route("/users/<int:user_id>/delete")
def ask_permission(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('permissions.html', user=user)
    
@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user_instance(user_id):
    User.query.filter_by(id=user_id).delete()
    db.session.commit() 
    
    return redirect('/users')

@app.route("/users/<int:user_id>/posts/new")
def new_post_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('new_post.html', user=user)

@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def send_post_and_redirect(user_id):
    user = User.query.get_or_404(user_id)
    new_post = Post(title=request.form['title'],
                    content=request.form['content'],user=user)
    
    db.session.add(new_post)
    db.session.commit()
    flash(f"'{new_post.title}' was successfully added.")
    
    return redirect(f"/users/{user_id}")


@app.route('/posts/<int:post_id>')
def show_post_by_id(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('show_post_by_id.html', post=post)

@app.route('/posts/<int:post_id>/edit')
def show_edit_form(post_id):
    post = Post.query.get_or_404(post_id)
    
    return render_template('edit_post.html', post=post, user=post.user)


@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def edit_post(post_id):
    pass