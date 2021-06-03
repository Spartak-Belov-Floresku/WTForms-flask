from models import Pet, db
from app import app

"""creat table"""
db.drop_all()
db.create_all()

"""if table is not empty"""
Pet.query.delete()


first_pet = Pet(name='Goofy', species='dog', photo_url='https://upload.wikimedia.org/wikipedia/en/5/50/Goofy_Duckipedia.png', age=89, notes='cartoon character')
second_pet = Pet(name='Tom', species='cat', photo_url='https://upload.wikimedia.org/wikipedia/en/f/f6/Tom_Tom_and_Jerry.png', age=75, notes='cartoon character')

db.session.add_all([first_pet, second_pet])
db.session.commit()