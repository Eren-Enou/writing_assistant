from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.faction import Faction
from ..forms import FactionForm
from ..extensions import db

factions_bp = Blueprint('factions', __name__, url_prefix='/factions')

@factions_bp.route('/')
def list_factions():
    factions = Faction.query.all()
    return render_template('factions/list.html', factions=factions)

@factions_bp.route('/add', methods=['GET', 'POST'])
def add_faction():
    form = FactionForm()
    if form.validate_on_submit():
        new_faction = Faction(
            name=form.name.data,
            description=form.description.data,
            world_id=form.world_id.data,
            is_neutral=form.is_neutral.data,
            is_good=form.is_good.data,
            is_evil=form.is_evil.data,
            is_chaotic=form.is_chaotic.data,
            is_lawful=form.is_lawful.data,
            alignment=form.alignment.data
        )
        db.session.add(new_faction)
        db.session.commit()
        flash('Faction created successfully!', 'success')
        return redirect(url_for('factions_bp.list_factions'))
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
    return render_template('factions/add.html', form=form)

@factions_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_faction(id):
    faction = Faction.query.get_or_404(id)
    form = FactionForm(obj=faction)
    if form.validate_on_submit():
        form.populate_obj(faction)
        db.session.commit()
        flash('Faction updated successfully!', 'success')
        return redirect(url_for('factions_bp.list_factions'))
    return render_template('factions/edit.html', form=form)


@factions_bp.route('/<int:id>/delete', methods=['POST'])
def delete_faction(id):
    faction = Faction.query.get_or_404(id)
    db.session.delete(faction)
    db.session.commit()
    return redirect(url_for('factions.list_factions'))
