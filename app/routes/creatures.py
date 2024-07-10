from flask import Blueprint, render_template, request, redirect, url_for
from ..models.creature import Creature
from ..extensions import db

creatures_bp = Blueprint('creatures', __name__, url_prefix='/creatures')

@creatures_bp.route('/')
def list_creatures():
    creatures = Creature.query.all()
    return render_template('creatures/list.html', creatures=creatures)

@creatures_bp.route('/add', methods=['GET', 'POST'])
def add_creature():
    if request.method == 'POST':
        new_creature = Creature(
            name=request.form['name'],
            description=request.form['description'],
            world_id=request.form['world_id'],
            species=request.form['species'],
            size=request.form['size'],
            age=request.form.get('age'),
            role=request.form['role'],
            align=request.form['align'],
            abilities=request.form.get('abilities'),
            weapons=request.form.get('weapons'),
            armor=request.form.get('armor')
        )
        db.session.add(new_creature)
        db.session.commit()
        return redirect(url_for('creatures.list_creatures'))
    return render_template('creatures/add.html')

@creatures_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_creature(id):
    creature = Creature.query.get_or_404(id)
    if request.method == 'POST':
        creature.name = request.form['name']
        creature.description = request.form['description']
        creature.world_id = request.form['world_id']
        creature.species = request.form['species']
        creature.size = request.form['size']
        creature.age = request.form.get('age')
        creature.role = request.form['role']
        creature.align = request.form['align']
        creature.abilities = request.form.get('abilities')
        creature.weapons = request.form.get('weapons')
        creature.armor = request.form.get('armor')
        db.session.commit()
        return redirect(url_for('creatures.list_creatures'))
    return render_template('creatures/edit.html', creature=creature)

@creatures_bp.route('/<int:id>/delete', methods=['POST'])
def delete_creature(id):
    creature = Creature.query.get_or_404(id)
    db.session.delete(creature)
    db.session.commit()
    return redirect(url_for('creatures.list_creatures'))
