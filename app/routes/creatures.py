from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.creature import Creature
from ..forms import CreatureForm
from ..extensions import db

creatures_bp = Blueprint('creatures', __name__, url_prefix='/creatures')

@creatures_bp.route('/')
def list_creatures():
    creatures = Creature.query.all()
    return render_template('creatures/list.html', creatures=creatures)

@creatures_bp.route('/add', methods=['GET', 'POST'])
def add_creature():
    form = CreatureForm()
    if form.validate_on_submit():
        new_creature = Creature(
            name=form.name.data,
            description=form.description.data,
            world_id=form.world.data.id if form.world.data else None,
            species=form.species.data,
            size=form.size.data,
            age=form.age.data,
            role=form.role.data,
            align=form.align.data,
            abilities=form.abilities.data,
            weapons=form.weapons.data,
            armor=form.armor.data
        )
        db.session.add(new_creature)
        db.session.commit()

        # Add multiple associations
        for event in form.events.data:
            new_creature.events.append(event)
        for faction in form.factions.data:
            new_creature.factions.append(faction)
        for location in form.locations.data:
            new_creature.locations.append(location)
        
        db.session.commit()
        flash('Creature created successfully!', 'success')
        return redirect(url_for('creatures.list_creatures'))
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
    return render_template('creatures/add.html', form=form)


@creatures_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_creature(id):
    creature = Creature.query.get_or_404(id)
    form = CreatureForm(obj=creature)
    if form.validate_on_submit():
        form.populate_obj(creature)
        db.session.commit()
        flash('Creature updated successfully!', 'success')
        return redirect(url_for('creatures.list_creatures'))
    return render_template('creatures/edit.html', form=form, creature=creature)

@creatures_bp.route('/<int:id>/delete', methods=['POST'])
def delete_creature(id):
    creature = Creature.query.get_or_404(id)
    db.session.delete(creature)
    db.session.commit()
    return redirect(url_for('creatures.list_creatures'))
