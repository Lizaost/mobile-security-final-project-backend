from flask import Flask
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app,
     expose_headers=['Access-Control-Allow-Credentials'],
     supports_credentials=True,
     origins='https://127.0.0.1:3000')
app.config.from_object(Config)
db = SQLAlchemy(app)
# db.init_app(app)
from app.posts.model import Post
from app.users.model import User
from app.comments.model import Comment

print(db)
migrate = Migrate(app, db, ssl_context='adhoc')

from app import routes

if __name__ == "__main__":
    print('---')
    app.run(ssl_context='adhoc')