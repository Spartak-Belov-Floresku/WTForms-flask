  
from unittest import TestCase

from app import app
from models import db, Pet


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin_flask:password@localhost/test_flask_db'
app.config['SQLALCHEMY_ECHO'] = False


app.config['TESTING'] = True


app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
app.config['WTF_CSRF_ENABLED'] = False

db.drop_all()
db.create_all()

class PetViewsTestCase(TestCase):
    """Test for views Pet"""

    def setUp(self):

        """Add sample Pet"""
        
        Pet.query.delete()
        
        first_pet = Pet(name='Goofy', species='dog', photo_url='https://upload.wikimedia.org/wikipedia/en/5/50/Goofy_Duckipedia.png', age=89, notes='cartoon character')
        second_pet = Pet(name='Tom', species='cat', photo_url='https://upload.wikimedia.org/wikipedia/en/f/f6/Tom_Tom_and_Jerry.png', age=75, notes='cartoon character')

        db.session.add_all([first_pet, second_pet])
        db.session.commit()

        self.first_pet_id = first_pet.id
        self.second_pet_id = second_pet.id

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    """run test to get all pets"""
    def test_list_pets(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('is available', html)

    """run test show edit form"""
    def test_show_edit_form(self):
        with app.test_client() as client:
            resp = client.get(f'/{self.second_pet_id}')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('cat', html)

    """run test to change pets's data in database"""
    def test_edit_pet_data(self):
        with app.test_client() as client:
            pet = {'name': 'Roman', 'species': 'dog'}
            resp = client.post(f'/{self.second_pet_id}', data=pet, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Roman', html)