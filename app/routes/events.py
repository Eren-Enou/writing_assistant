from flask import Blueprint, render_template, request, redirect, url_for
from ..models.event import Event
from ..forms import EventForm
from ..extensions import db

events_bp = Blueprint('events', __name__, url_prefix='/events')

@events_bp.route('/')
def list_events():
    events = Event.query.all()
    return render_template('events/list.html', events=events)

@events_bp.route('/add', methods=['GET', 'POST'])
def add_event():
    form = EventForm()
    if form.validate_on_submit():
        new_event = Event(
            name=form.name.data,
            description=form.description.data,
            date=form.date.data,
            location_id=form.location_id.data,
            faction_id=form.faction_id.data,
            plot_id=form.plot_id.data,
            world_id=form.world_id.data
        )
        db.session.add(new_event)
        db.session.commit()
        flash('Event created successfully!', 'success')
        return redirect(url_for('events_bp.list_events'))
    return render_template('events/add.html', form=form)

@events_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_event(id):
    event = Event.query.get_or_404(id)
    form = EventForm(obj=event)
    if form.validate_on_submit():
        form.populate_obj(event)
        db.session.commit()
        flash('Event updated successfully!', 'success')
        return redirect(url_for('events_bp.list_events'))
    return render_template('events/edit.html', form=form)


@events_bp.route('/<int:id>/delete', methods=['POST'])
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('events.list_events'))
