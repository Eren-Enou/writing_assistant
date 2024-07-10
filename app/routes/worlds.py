from flask import Blueprint, render_template, request, redirect, url_for
from ..models.world import World
from ..extensions import db

worlds_bp = Blueprint('worlds', __name__, url_prefix='/worlds')

@worlds_bp.route('/')
def list_worlds():
    worlds = World.query.all()
    return render_template('worlds/list.html', worlds=worlds)

@worlds_bp.route('/add', methods=['GET', 'POST'])
def add_world():
    if request.method == 'POST':
        new_world = World(
            name=request.form['name'],
            description=request.form['description'],
            history=request.form.get('history'),
            time_period=request.form.get('time_period'),
            setting=request.form.get('setting'),
            temperature=request.form.get('temperature'),
            humidity=request.form.get('humidity'),
            flora=request.form.get('flora'),
            fauna=request.form.get('fauna'),
            magical_system=request.form.get('magical_system')
        )
        db.session.add(new_world)
        db.session.commit()
        return redirect(url_for('worlds.list_worlds'))
    return render_template('worlds/add.html')

@worlds_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_world(id):
    world = World.query.get_or_404(id)
    if request.method == 'POST':
        world.name = request.form['name']
        world.description = request.form['description']
        world.history = request.form.get('history')
        world.time_period = request.form.get('time_period')
        world.setting = request.form.get('setting')
        world.temperature = request.form.get('temperature')
        world.humidity = request.form.get('humidity')
        world.flora = request.form.get('flora')
        world.fauna = request.form.get('fauna')
        world.magical_system = request.form.get('magical_system')
        db.session.commit()
        return redirect(url_for('worlds.list_worlds'))
    return render_template('worlds/edit.html', world=world)

@worlds_bp.route('/<int:id>/delete', methods=['POST'])
def delete_world(id):
    world = World.query.get_or_404(id)
    db.session.delete(world)
    db.session.commit()
    return redirect(url_for('worlds.list_worlds'))
