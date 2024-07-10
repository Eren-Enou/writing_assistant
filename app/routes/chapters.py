from flask import Blueprint, render_template, request, redirect, url_for
from ..models.chapter import Chapter
from ..extensions import db

chapters_bp = Blueprint('chapters', __name__, url_prefix='/chapters')

@chapters_bp.route('/')
def list_chapters():
    chapters = Chapter.query.all()
    return render_template('chapters/list.html', chapters=chapters)

@chapters_bp.route('/add', methods=['GET', 'POST'])
def add_chapter():
    if request.method == 'POST':
        new_chapter = Chapter(
            title=request.form['title'],
            content=request.form['content'],
            plot_id=request.form['plot_id'],
            world_id=request.form['world_id'],
            location_id=request.form.get('location_id'),
            creature_id=request.form.get('creature_id'),
            event_id=request.form.get('event_id'),
            magic_system_id=request.form.get('magic_system_id'),
            faction_id=request.form.get('faction_id')
        )
        db.session.add(new_chapter)
        db.session.commit()
        return redirect(url_for('chapters.list_chapters'))
    return render_template('chapters/add.html')

@chapters_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_chapter(id):
    chapter = Chapter.query.get_or_404(id)
    if request.method == 'POST':
        chapter.title = request.form['title']
        chapter.content = request.form['content']
        chapter.plot_id = request.form['plot_id']
        chapter.world_id = request.form['world_id']
        chapter.location_id = request.form.get('location_id')
        chapter.creature_id = request.form.get('creature_id')
        chapter.event_id = request.form.get('event_id')
        chapter.magic_system_id = request.form.get('magic_system_id')
        chapter.faction_id = request.form.get('faction_id')
        db.session.commit()
        return redirect(url_for('chapters.list_chapters'))
    return render_template('chapters/edit.html', chapter=chapter)

@chapters_bp.route('/<int:id>/delete', methods=['POST'])
def delete_chapter(id):
    chapter = Chapter.query.get_or_404(id)
    db.session.delete(chapter)
    db.session.commit()
    return redirect(url_for('chapters.list_chapters'))
