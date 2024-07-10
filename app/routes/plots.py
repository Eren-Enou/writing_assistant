from flask import Blueprint, render_template, request, redirect, url_for
from ..models.plot import Plot
from ..extensions import db

plots_bp = Blueprint('plots', __name__, url_prefix='/plots')

@plots_bp.route('/')
def list_plots():
    plots = Plot.query.all()
    return render_template('plots/list.html', plots=plots)

@plots_bp.route('/add', methods=['GET', 'POST'])
def add_plot():
    if request.method == 'POST':
        new_plot = Plot(
            title=request.form['title'],
            summary=request.form['summary'],
            description=request.form.get('description'),
            world_id=request.form['world_id'],
            status=request.form.get('status'),
            genre=request.form.get('genre'),
            rating=request.form.get('rating'),
            word_count=request.form.get('word_count'),
            reading_time=request.form.get('reading_time'),
            published_date=request.form.get('published_date')
        )
        db.session.add(new_plot)
        db.session.commit()
        return redirect(url_for('plots.list_plots'))
    return render_template('plots/add.html')

@plots_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_plot(id):
    plot = Plot.query.get_or_404(id)
    if request.method == 'POST':
        plot.title = request.form['title']
        plot.summary = request.form['summary']
        plot.description = request.form.get('description')
        plot.world_id = request.form['world_id']
        plot.status = request.form.get('status')
        plot.genre = request.form.get('genre')
        plot.rating = request.form.get('rating')
        plot.word_count = request.form.get('word_count')
        plot.reading_time = request.form.get('reading_time')
        plot.published_date = request.form.get('published_date')
        db.session.commit()
        return redirect(url_for('plots.list_plots'))
    return render_template('plots/edit.html', plot=plot)

@plots_bp.route('/<int:id>/delete', methods=['POST'])
def delete_plot(id):
    plot = Plot.query.get_or_404(id)
    db.session.delete(plot)
    db.session.commit()
    return redirect(url_for('plots.list_plots'))
