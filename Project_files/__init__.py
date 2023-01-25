from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Project_files.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8c5cb42ba703d467c8beecc8'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.app_context().push()
login_manager = LoginManager(app)

from Project_files import routes
