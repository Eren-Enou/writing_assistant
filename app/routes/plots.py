from flask import Blueprint, render_template, request, redirect, url_for
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
            world_id=form.world_id.data,
            status=form.status.data,
            genre=form.genre.data,
            rating=form.rating.data,
            word_count=form.word_count.data,
            reading_time=form.reading_time.data,
            published_date=form.published_date.data
        )
        db.session.add(new_plot)
        db.session.commit()
        flash('Plot created successfully!', 'success')
        return redirect(url_for('plots_bp.list_plots'))
    return render_template('plots/add.html', form=form)

@plots_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_plot(id):
    plot = Plot.query.get_or_404(id)
    form = PlotForm(obj=plot)
    if form.validate_on_submit():
        form.populate_obj(plot)
        db.session.commit()
        flash('Plot updated successfully!', 'success')
        return redirect(url_for('plots_bp.list_plots'))
    return render_template('plots/edit.html', form=form)

@plots_bp.route('/<int:id>/delete', methods=['POST'])
def delete_plot(id):
    plot = Plot.query.get_or_404(id)
    db.session.delete(plot)
    db.session.commit()
    return redirect(url_for('plots.list_plots'))
