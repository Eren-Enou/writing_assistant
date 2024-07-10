from flask import Blueprint, render_template, request, redirect, url_for
from ..models.faction import Faction
from ..extensions import db

factions_bp = Blueprint('factions', __name__, url_prefix='/factions')

@factions_bp.route('/')
def list_factions():
    factions = Faction.query.all()
    return render_template('factions/list.html', factions=factions)

@factions_bp.route('/add', methods=['GET', 'POST'])
def add_faction():
    if request.method == 'POST':
        new_faction = Faction(
            name=request.form['name'],
            description=request.form['description'],
            world_id=request.form['world_id'],
            is_neutral=request.form.get('is_neutral') == 'on',
            is_good=request.form.get('is_good') == 'on',
            is_evil=request.form.get('is_evil') == 'on',
            is_chaotic=request.form.get('is_chaotic') == 'on',
            is_lawful=request.form.get('is_lawful') == 'on',
            alignment=request.form.get('alignment')
        )
        db.session.add(new_faction)
        db.session.commit()
        return redirect(url_for('factions.list_factions'))
    return render_template('factions/add.html')

@factions_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_faction(id):
    faction = Faction.query.get_or_404(id)
    if request.method == 'POST':
        faction.name = request.form['name']
        faction.description = request.form['description']
        faction.world_id = request.form['world_id']
        faction.is_neutral = request.form.get('is_neutral') == 'on'
        faction.is_good = request.form.get('is_good') == 'on'
        faction.is_evil = request.form.get('is_evil') == 'on'
        faction.is_chaotic = request.form.get('is_chaotic') == 'on'
        faction.is_lawful = request.form.get('is_lawful') == 'on'
        faction.alignment = request.form.get('alignment')
        db.session.commit()
        return redirect(url_for('factions.list_factions'))
    return render_template('factions/edit.html', faction=faction)

@factions_bp.route('/<int:id>/delete', methods=['POST'])
def delete_faction(id):
    faction = Faction.query.get_or_404(id)
    db.session.delete(faction)
    db.session.commit()
    return redirect(url_for('factions.list_factions'))
