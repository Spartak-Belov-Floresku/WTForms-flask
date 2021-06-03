from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://admin_flask:password@localhost/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = 'helloworld'
app.debug = True
DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """lists all pets in db"""

    pets = db.session.query(Pet.id, Pet.name, Pet.photo_url, Pet.available).all()

    return render_template('index.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def show_add_form():
    """create a new pet"""

    form = PetForm()

    if form.validate_on_submit():

        """get data from form fields"""
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')
    else:
        form_name = "Add pet"
        return render_template('add_form.html', form = form, form_name = form_name)


@app.route("/<int:id>", methods=['GET', 'POST'])
def show_edit_form(id):
    """edit pet data"""

    pet = Pet.query.get_or_404(id)
    
    """here convert True or False to a string for form layout"""
    if pet.available:
        pet.available = 'true'
    else:
        pet.available = 'false'

    """sends pet data into form's field"""
    form = PetForm(obj=pet)

    if form.validate_on_submit():

        """get data from form fields and apply them to the pet"""
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        available = form.available.data

        """here convert  a string to True or False for db"""
        if available == "true":
            pet.available = True
        else:
            pet.available = False

        db.session.commit()

        flash(f'Pet {pet.name} updated', 'text-success font-weight-bold')

        return redirect(f'/{id}')
    else:
        form_name = "Edit Pet"
        return render_template('add_form.html', form = form, form_name = form_name)




if __name__ == "__main__":
    app.run(debug=True)