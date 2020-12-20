"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    

class User(db.Model):
    """Instance of User"""
    
    __tablename__ = "users"
    
    def __repr__(self):
        u = self
        return f"<User id={u.id} first name={u.first_name} last name={u.last_name} url={u.img_url}>"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.String(30),
                           nullable=False,
                           unique=False)
    
    last_name = db.Column(db.String(30),
                          nullable=False,
                          unique=False)
    
    img_url = db.Column(db.String,
                          nullable=False,
                          default="https://www.idomains.uk/wp-content/uploads/2017/06/Profile_avatar_placeholder_large-250x250.png",
                          unique=False)
    
    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")
    
    @property
    def get_full_name(self):
        u = self
        return f"{u.first_name} {u.last_name}"
    
    
class Post(db.Model):
    """It's a post baby!
    Everyone's favorite thing.
    Users post posts.
    """
    __tablename__ = "posts"
    
    def __repr__(self):
        p = self
        return f"<Post {self.id} Title {self.title} Created At {self.created_at} User ID {self.user_id}>"
        
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    title = db.Column(db.String(60),
                      nullable=False,
                      unique=False)
    
    content = db.Column(db.String,
                        nullable=False,
                        unique=True)
    
    created_at = db.Column(db.DateTime,
                           nullable=False,
                           default=datetime.datetime.now)
    
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.id'),
                        nullable=False)
    
    