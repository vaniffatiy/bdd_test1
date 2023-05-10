from models import User
from models import db

user = User(username='John', email='john@example.com')
user.save()
db.close()
