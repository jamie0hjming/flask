
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def init_ext(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    Bootstrap(app=app)
