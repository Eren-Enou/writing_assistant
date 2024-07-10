from flask import Blueprint, render_template, request, redirect, url_for
from ..models.location import Location
from ..extensions import db

locations_bp = Blueprint('locations', __name__, url_prefix='/locations')

@locations_bp.route('/')
def list_locations():
    locations = Location.query.all()
    return render_template('locations/list.html', locations=locations)

@locations_bp.route('/add', methods=['GET', 'POST'])
def add_location():
    if request.method == 'POST':
        new_location = Location(
            name=request.form['name'],
            description=request.form['description'],
            world_id=request.form['world_id'],
            climate=request.form['climate'],
            terrain=request.form['terrain']
        )
        db.session.add(new_location)
        db.session.commit()
        return redirect(url_for('locations.list_locations'))
    return render_template('locations/add.html')

@locations_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_location(id):
    location = Location.query.get_or_404(id)
    if request.method == 'POST':
        location.name = request.form['name']
        location.description = request.form['description']
        location.world_id = request.form['world_id']
        location.climate = request.form['climate']
        location.terrain = request.form['terrain']
        db.session.commit()
        return redirect(url_for('locations.list_locations'))
    return render_template('locations/edit.html', location=location)

@locations_bp.route('/<int:id>/delete', methods=['POST'])
def delete_location(id):
    location = Location.query.get_or_404(id)
    db.session.delete(location)
    db.session.commit()
    return redirect(url_for('locations.list_locations'))
