from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.plot import Plot
from ..forms import PlotForm
from ..extensions import db

plots_bp = Blueprint('plots', __name__, url_prefix='/plots')

@plots_bp.route('/')
def list_plots():
    plots = Plot.query.all()
    return render_template('plots/list.html', plots=plots)

@plots_bp.route('/add', methods=['GET', 'POST'])
def add_plot():
    form = PlotForm()
    if form.validate_on_submit():
        new_plot = Plot(
            title=form.title.data,
            summary=form.summary.data,
            description=form.description.data,
            world_id=form.world.data.id if form.world.data else None,
            status=form.status.data,
            genre=form.genre.data,
            rating=form.rating.data,
            word_count=form.word_count.data,
            reading_time=form.reading_time.data,
            published_date=form.published_date.data
        )
        db.session.add(new_plot)
        db.session.commit()

        # Add multiple associations
        for location in form.locations.data:
            new_plot.locations.append(location)
        for event in form.events.data:
            new_plot.events.append(event)
        for character in form.characters.data:
            new_plot.characters.append(character)

        db.session.commit()
        flash('Plot created successfully!', 'success')
        return redirect(url_for('plots.list_plots'))
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
    return render_template('plots/add.html', form=form)


@plots_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_plot(id):
    plot = Plot.query.get_or_404(id)
    form = PlotForm(obj=plot)
    if form.validate_on_submit():
        form.populate_obj(plot)
        db.session.commit()
        flash('Plot updated successfully!', 'success')
        return redirect(url_for('plots.list_plots'))
    return render_template('plots/edit.html', form=form, plot=plot)

@plots_bp.route('/<int:id>/delete', methods=['POST'])
def delete_plot(id):
    plot = Plot.query.get_or_404(id)
    db.session.delete(plot)
    db.session.commit()
    return redirect(url_for('plots.list_plots'))
