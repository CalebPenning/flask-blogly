from unittest import TestCase

from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test_db'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserViewsTestCase(TestCase):
    """Tests for view functions on Users."""
    
    def setUp(self):
        
        """Add sample user"""
        User.query.delete()
        
        user = User(first_name="Test", last_name="Johnny")
        db.session.add(user)
        db.session.commit()
        
        self.user_id = user.id
    
    def tearDown(self):
        db.session.rollback()
    
    def test_user_list(self):
        with app.test_client() as client:
            respt = client.get("/")
            html = resp.get_data(as_test=True)
            
            self.assertEqual(resp.status_code, 200)
            
    def test_add_user(self):
        with app.test_client() as client:
            d = {"first_name": "Test", "last_name": "test", "img_url": ""}
            resp = client.post("/users/new", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
    
            