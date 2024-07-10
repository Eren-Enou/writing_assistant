from flask import Blueprint, render_template, request, redirect, url_for, flash
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
            plot_id=form.plot.data.id if form.plot.data else None,
            world_id=form.world.data.id if form.world.data else None,
        )
        db.session.add(new_chapter)
        db.session.commit()

        # Add multiple associations
        for location in form.locations.data:
            new_chapter.locations.append(location)
        for creature in form.creatures.data:
            new_chapter.creatures.append(creature)
        for event in form.events.data:
            new_chapter.events.append(event)
        for magic_system in form.magic_systems.data:
            new_chapter.magic_systems.append(magic_system)
        for faction in form.factions.data:
            new_chapter.factions.append(faction)
        
        db.session.commit()
        flash('Chapter created successfully!', 'success')
        return redirect(url_for('chapters.list_chapters'))
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
    return render_template('chapters/add.html', form=form)


@chapters_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_chapter(id):
    chapter = Chapter.query.get_or_404(id)
    form = ChapterForm(obj=chapter)
    if form.validate_on_submit():
        form.populate_obj(chapter)
        db.session.commit()
        flash('Chapter updated successfully!', 'success')
        return redirect(url_for('chapters.list_chapters'))
    return render_template('chapters/edit.html', form=form, chapter=chapter)

@chapters_bp.route('/<int:id>/delete', methods=['POST'])
def delete_chapter(id):
    chapter = Chapter.query.get_or_404(id)
    db.session.delete(chapter)
    db.session.commit()
    return redirect(url_for('chapters.list_chapters'))
