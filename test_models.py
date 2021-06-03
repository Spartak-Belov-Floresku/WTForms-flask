from unittest import TestCase

from app import app
from models import db, Pet

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin_flask:password@localhost/test_flask_db'
app.config['SQLALCHEMY_ECHO'] = False


db.drop_all()
db.create_all()


class PetModelTestCase(TestCase):
    """Tests for model for Pet"""

    def setUp(self):
        """Clean up any existing pets"""

        Pet.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    """run test to ctreate pet object"""
    def test_create_pet_obj(self):

        pet = Pet(name='Goofy', species='dog', photo_url='https://upload.wikimedia.org/wikipedia/en/5/50/Goofy_Duckipedia.png', age=89, notes='cartoon character')

        self.assertEqual(pet.name, "Goofy")

    """run test to insert pet data into database"""
    def test_insert_pet_to_db(self):
        
        pet = Pet(name='Goofy', species='dog', photo_url='https://upload.wikimedia.org/wikipedia/en/5/50/Goofy_Duckipedia.png', age=89, notes='cartoon character')
        
        db.session.add(pet)
        db.session.commit()

        self.assertEqual(pet.name, 'Goofy')