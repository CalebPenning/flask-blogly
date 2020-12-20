from app import app
from models import User, db, Post

# Create all tables 
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Post.query.delete()
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

# Add new posts 
p1 = Post(title="I'm so happy!", content="The title says it all. I couldn't be happier!", user_id=1)
p2 = Post(title="I'm sad.", content="Just kidding, I'm good. lol", user_id=2)
p3 = Post(title="Lol", content="I'm hanging out with my girlfriend.", user_id=3)

db.session.add_all([nick, stavros, adam])
db.session.commit()

db.session.add_all([p1, p2, p3])
db.session.commit()