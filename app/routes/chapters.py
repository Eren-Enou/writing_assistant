from flask import Blueprint, render_template, request, redirect, url_for
from ..models.chapter import Chapter
from ..forms.chapter import ChapterForm
from ..extensions import db

chapters_bp = Blueprint('chapters', __name__, url_prefix='/chapters')

@chapters_bp.route('/')
def list_chapters():
    chapters = Chapter.query.all()
    return render_template('chapters/list.html', chapters=chapters)

@chapters_bp.route('/add', methods=['GET', 'POST'])
def add_chapter():
    form = ChapterForm()
    if form.validate_on_submit():
        new_chapter = Chapter(
            title=form.title.data,
            content=form.content.data,
            plot_id=form.plot_id.data,
            world_id=form.world_id.data,
            location_id=form.location_id.data,
            creature_id=form.creature_id.data,
            event_id=form.event_id.data,
            magic_system_id=form.magic_system_id.data,
            faction_id=form.faction_id.data
        )
        db.session.add(new_chapter)
        db.session.commit()
        flash('Chapter created successfully!', 'success')
        return redirect(url_for('chapters_bp.list_chapters'))
    return render_template('chapters/add.html', form=form)

@chapters_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_chapter(id):
    chapter = Chapter.query.get_or_404(id)
    form = ChapterForm(obj=chapter)
    if form.validate_on_submit():
        form.populate_obj(chapter)
        db.session.commit()
        flash('Chapter updated successfully!', 'success')
        return redirect(url_for('chapters_bp.list_chapters'))
    return render_template('chapters/edit.html', form=form)

@chapters_bp.route('/<int:id>/delete', methods=['POST'])
def delete_chapter(id):
    chapter = Chapter.query.get_or_404(id)
    db.session.delete(chapter)
    db.session.commit()
    return redirect(url_for('chapters.list_chapters'))
