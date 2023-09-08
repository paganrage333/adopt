from flask import Flask, redirect, render_template, flash, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from forms import AddPetForm, EditPetForm
from models import db, connect_db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG'] = True
app.app_context().push()

connect_db(app)
db.create_all()

@app.route("/")
def show_home():
    return render_template("home.html")

@app.route("/add", methods=["GET", "POST"])
def add_pet():

    form = AddPetForm

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        flash(f"Added {name}")
        return redirect("/add")
    else: 
        return render_template("add_pet_form.html", form=form)

@app.route('/pet/<int:pet_id>', methods=['GET', 'POST'])
def pet_details(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if request.method == 'POST' and form.validate_on_submit():
        form.popualte_obj(pet)
        db.session.commit()
        return redirect(url_for('pet_display', pet_id=pet_id))
    
    return render_template('pet_display.html', pet=pet, form=form)




