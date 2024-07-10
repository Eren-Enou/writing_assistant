from flask import Blueprint, render_template, request, redirect, url_for
from ..models.character import Character
from ..extensions import db

characters_bp = Blueprint('characters', __name__, url_prefix='/characters')

@characters_bp.route('/')
def list_characters():
    characters = Character.query.all()
    return render_template('characters/list.html', characters=characters)

@characters_bp.route('/add', methods=['GET', 'POST'])
def add_character():
    if request.method == 'POST':
        new_character = Character(
            name=request.form['name'],
            description=request.form['description'],
            race=request.form['race'],
            class_=request.form['class_'],
            deity=request.form.get('deity'),
            age=request.form['age'],
            alignment=request.form['alignment'],
            strength=request.form['strength'],
            dexterity=request.form['dexterity'],
            constitution=request.form['constitution'],
            intelligence=request.form['intelligence'],
            wisdom=request.form['wisdom'],
            charisma=request.form['charisma'],
            experience_points=request.form['experience_points'],
            background=request.form['background'],
            personality=request.form['personality'],
            ideal=request.form['ideal'],
            bonds=request.form['bonds'],
            flaws=request.form['flaws']
        )
        db.session.add(new_character)
        db.session.commit()
        return redirect(url_for('characters.list_characters'))
    return render_template('characters/add.html')

@characters_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_character(id):
    character = Character.query.get_or_404(id)
    if request.method == 'POST':
        character.name = request.form['name']
        character.description = request.form['description']
        character.race = request.form['race']
        character.class_ = request.form['class_']
        character.deity = request.form.get('deity')
        character.age = request.form['age']
        character.alignment = request.form['alignment']
        character.strength = request.form['strength']
        character.dexterity = request.form['dexterity']
        character.constitution = request.form['constitution']
        character.intelligence = request.form['intelligence']
        character.wisdom = request.form['wisdom']
        character.charisma = request.form['charisma']
        character.experience_points = request.form['experience_points']
        character.background = request.form['background']
        character.personality = request.form['personality']
        character.ideal = request.form['ideal']
        character.bonds = request.form['bonds']
        character.flaws = request.form['flaws']
        db.session.commit()
        return redirect(url_for('characters.list_characters'))
    return render_template('characters/edit.html', character=character)

@characters_bp.route('/<int:id>/delete', methods=['POST'])
def delete_character(id):
    character = Character.query.get_or_404(id)
    db.session.delete(character)
    db.session.commit()
    return redirect(url_for('characters.list_characters'))
