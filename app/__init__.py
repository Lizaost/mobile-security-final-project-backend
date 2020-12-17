from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# db.init_app(app)
from app.posts.model import Post
from app.users.model import User
from app.comments.model import Comment
print(db)
migrate = Migrate(app, db)

from app import routes
