from flask import Blueprint, render_template, request, redirect, url_for, flash
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
            location_id=form.location.data.id if form.location.data else None,
            faction_id=form.faction.data.id if form.faction.data else None,
            plot_id=form.plot.data.id if form.plot.data else None,
            world_id=form.world.data.id if form.world.data else None,
        )
        db.session.add(new_event)
        db.session.commit()

        # Add multiple associations
        for character in form.characters.data:
            new_event.characters.append(character)
        for creature in form.creatures.data:
            new_event.creatures.append(creature)
        
        db.session.commit()
        flash('Event created successfully!', 'success')
        return redirect(url_for('events.list_events'))
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
    return render_template('events/add.html', form=form)


@events_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_event(id):
    event = Event.query.get_or_404(id)
    form = EventForm(obj=event)
    if form.validate_on_submit():
        form.populate_obj(event)
        db.session.commit()
        flash('Event updated successfully!', 'success')
        return redirect(url_for('events.list_events'))
    return render_template('events/edit.html', form=form, event=event)


@events_bp.route('/<int:id>/delete', methods=['POST'])
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('events.list_events'))
