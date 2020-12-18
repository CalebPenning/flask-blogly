from models import User, db
from app import app

# Create all tables 
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users 
nick = User(first_name="Nick",
            last_name="Mullen",
            img_url="https://www.comedymoontower.com/wp-content/uploads/2016/03/9A123975-C92D-F98D-A75BDE23553BDFDC.jpg")

stavros = User(first_name="Stavros",
               last_name="Halkias",
               img_url="https://bestcomedytickets.com/wp-content/uploads/2019/10/Stavros-Halkias.jpg")

adam = User(first_name="Adam",
            last_name="Friedland",
            img_url="https://i.ytimg.com/vi/5I-6SHfYOw8/maxresdefault.jpg")

# Add new objects to session, so they'll persist
db.session.add(nick)
db.session.add(stavros)
db.session.add(adam)

# Commit, otherwise this never gets saved!
db.session.commit()