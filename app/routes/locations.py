from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.location import Location
from ..forms import LocationForm
from ..extensions import db

locations_bp = Blueprint('locations', __name__, url_prefix='/locations')

@locations_bp.route('/')
def list_locations():
    locations = Location.query.all()
    return render_template('locations/list.html', locations=locations)

@locations_bp.route('/add', methods=['GET', 'POST'])
def add_location():
    form = LocationForm()
    if form.validate_on_submit():
        new_location = Location(
            name=form.name.data,
            description=form.description.data,
            world_id=form.world_id.data,
            climate=form.climate.data,
            terrain=form.terrain.data
        )
        db.session.add(new_location)
        db.session.commit()
        flash('Location created successfully!', 'success')
        return redirect(url_for('locations_bp.list_locations'))
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
    return render_template('locations/add.html', form=form)

@locations_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_location(id):
    location = Location.query.get_or_404(id)
    form = LocationForm(obj=location)
    if form.validate_on_submit():
        form.populate_obj(location)
        db.session.commit()
        flash('Location updated successfully!', 'success')
        return redirect(url_for('locations_bp.list_locations'))
    return render_template('locations/edit.html', form=form)


@locations_bp.route('/<int:id>/delete', methods=['POST'])
def delete_location(id):
    location = Location.query.get_or_404(id)
    db.session.delete(location)
    db.session.commit()
    return redirect(url_for('locations.list_locations'))
