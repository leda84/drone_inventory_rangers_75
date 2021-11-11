# will run first when app runs
from flask import Flask
from config import Config
from .site.routes import site
#after making blueprint, remember to import here to link
from .api.routes import api
from .authentication.routes import auth

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .models import db as root_db, login_manager, ma 
from flask_cors import CORS
from drone_inventory.helpers import JSONEncoder


app = Flask(__name__)

app.register_blueprint(site)
##then register blueprint here
app.register_blueprint(api)
app.register_blueprint(auth)

app.config.from_object(Config)

root_db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.signin'  # to specify which page to load for non-authenticated users
ma.init_app(app)


migrate = Migrate(app,root_db)


CORS(app)


app.json_encoder = JSONEncoder