from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..forms import CharacterForm
from ..models import Character
from ..extensions import db

characters_bp = Blueprint('characters', __name__, url_prefix='/characters')

@characters_bp.route('/')
def list_characters():
    characters = Character.query.all()
    return render_template('characters/list.html', characters=characters)

@characters_bp.route('/add', methods=['GET', 'POST'])
def add_character():
    form = CharacterForm()
    if form.validate_on_submit():
        new_character = Character(
            name=form.name.data,
            description=form.description.data,
            race=form.race.data,
            class_=form.class_.data,
            deity=form.deity.data,
            age=form.age.data,
            alignment=form.alignment.data,
            strength=form.strength.data,
            dexterity=form.dexterity.data,
            constitution=form.constitution.data,
            intelligence=form.intelligence.data,
            wisdom=form.wisdom.data,
            charisma=form.charisma.data,
            experience_points=form.experience_points.data,
            background=form.background.data,
            personality=form.personality.data,
            ideal=form.ideal.data,
            bonds=form.bonds.data,
            flaws=form.flaws.data
        )
        db.session.add(new_character)
        db.session.commit()
        flash('Character created successfully!', 'success')
        return redirect(url_for('characters.list_characters'))
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
    return render_template('characters/add.html', form=form)

@characters_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_character(id):
    character = Character.query.get_or_404(id)
    form = CharacterForm(obj=character)
    if form.validate_on_submit():
        form.populate_obj(character)
        db.session.commit()
        flash('Character updated successfully!', 'success')
        return redirect(url_for('characters.list_characters'))
    return render_template('characters/edit.html', form=form, character=character)

@characters_bp.route('/delete/<int:id>', methods=['POST'])
def delete_character(id):
    character = Character.query.get_or_404(id)
    db.session.delete(character)
    db.session.commit()
    return redirect(url_for('characters.list_characters'))
