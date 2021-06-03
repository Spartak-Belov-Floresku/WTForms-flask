from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Boolean

db = SQLAlchemy()

def connect_db(app):
    """connect to db"""

    db.app = app
    db.init_app(app)


class Pet(db.Model):

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    species = db.Column(db.String(25), nullable=False)
    photo_url = db.Column(db.Text, nullable= False, default='none')
    age = db.Column(db.Integer, default=1)
    notes = db.Column(db.Text, nullable=False, default='none')
    available = db.Column(Boolean, nullable=False, default=True)