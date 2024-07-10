from flask import Blueprint, render_template, request, redirect, url_for
from ..models.event import Event
from ..extensions import db

events_bp = Blueprint('events', __name__, url_prefix='/events')

@events_bp.route('/')
def list_events():
    events = Event.query.all()
    return render_template('events/list.html', events=events)

@events_bp.route('/add', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        new_event = Event(
            name=request.form['name'],
            description=request.form['description'],
            date=request.form['date'],
            location_id=request.form.get('location_id'),
            faction_id=request.form.get('faction_id'),
            plot_id=request.form.get('plot_id'),
            world_id=request.form['world_id']
        )
        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for('events.list_events'))
    return render_template('events/add.html')

@events_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_event(id):
    event = Event.query.get_or_404(id)
    if request.method == 'POST':
        event.name = request.form['name']
        event.description = request.form['description']
        event.date = request.form['date']
        event.location_id = request.form.get('location_id')
        event.faction_id = request.form.get('faction_id')
        event.plot_id = request.form.get('plot_id')
        event.world_id = request.form['world_id']
        db.session.commit()
        return redirect(url_for('events.list_events'))
    return render_template('events/edit.html', event=event)

@events_bp.route('/<int:id>/delete', methods=['POST'])
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('events.list_events'))
