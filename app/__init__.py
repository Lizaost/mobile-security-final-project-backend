from flask import Flask
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# CORS(app,
#      expose_headers=['Access-Control-Allow-Credentials', 'Access-Control-Allow-Origin'],
#      supports_credentials=True,
#      origins='https://127.0.0.1:3000')
app.config.from_object(Config)
db = SQLAlchemy(app)
# db.init_app(app)

# all db models, import after db creation, but before migrations
from app.posts.model import Post
from app.users.model import User
from app.comments.model import Comment
from app.auth.blacklist_token_model import BlacklistToken
from app.auth.refresh_token_model import RefreshToken

# db.create_all() after any changes in models

print(db)
migrate = Migrate(app, db, ssl_context='adhoc')

from app import routes
