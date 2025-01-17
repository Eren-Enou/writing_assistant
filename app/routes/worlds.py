from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import text
from ..models.world import World
from ..forms import WorldForm
from ..extensions import db

worlds_bp = Blueprint('worlds', __name__, url_prefix='/worlds')

@worlds_bp.route('/')
def list_worlds():
    sort_by = request.args.get('sort_by', 'name')
    search = request.args.get('search', '')

    if sort_by not in ['name', 'temperature']:
        sort_by = 'name'

    query = World.query
    if search:
        query = query.filter(World.name.ilike(f'%{search}%'))

    worlds = query.order_by(text(sort_by)).all()
    return render_template('worlds/list.html', worlds=worlds, sort_by=sort_by)



@worlds_bp.route('/add', methods=['GET', 'POST'])
def add_world():
    form = WorldForm()
    if form.validate_on_submit():
        new_world = World(
            name=form.name.data,
            description=form.description.data,
            history=form.history.data,
            time_period=form.time_period.data,
            setting=form.setting.data,
            temperature=form.temperature.data,
            humidity=form.humidity.data,
            flora=form.flora.data,
            fauna=form.fauna.data,
            magical_system=form.magical_system.data
        )
        db.session.add(new_world)
        db.session.commit()
        flash('World created successfully!', 'success')
        return redirect(url_for('worlds.list_worlds'))
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
    return render_template('worlds/add.html', form=form)

@worlds_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_world(id):
    world = World.query.get_or_404(id)
    form = WorldForm(obj=world)
    if form.validate_on_submit():
        form.populate_obj(world)
        db.session.commit()
        flash('World updated successfully!', 'success')
        return redirect(url_for('worlds.list_worlds'))
    return render_template('worlds/edit.html', form=form, world=world)



@worlds_bp.route('/<int:id>/delete', methods=['POST'])
def delete_world(id):
    world = World.query.get_or_404(id)
    db.session.delete(world)
    db.session.commit()
    return redirect(url_for('worlds.list_worlds'))
