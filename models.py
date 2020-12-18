"""Models for Blogly."""
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
    
    def get_full_name(self):
        u = self
        return f"{u.first_name} {u.last_name}"
    
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
                          default="",
                          unique=True)
    
    
    
    