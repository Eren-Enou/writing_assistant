from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.relationship import Relationship
from ..forms import RelationshipForm
from ..extensions import db

relationships_bp = Blueprint('relationships', __name__, url_prefix='/relationships')

@relationships_bp.route('/')
def list_relationships():
    relationships = Relationship.query.all()
    return render_template('relationships/list.html', relationships=relationships)

@relationships_bp.route('/add', methods=['GET', 'POST'])
def add_relationship():
    form = RelationshipForm()
    if form.validate_on_submit():
        new_relationship = Relationship(
            character1_id=form.character1.data.id,
            character2_id=form.character2.data.id,
            relationship_type=form.relationship_type.data,
            description=form.description.data,
            level=form.level.data,
            is_romantic=form.is_romantic.data,
            is_supportive=form.is_supportive.data,
            is_rival=form.is_rival.data,
            is_ally=form.is_ally.data,
            is_conflict=form.is_conflict.data
        )
        db.session.add(new_relationship)
        db.session.commit()
        flash('Relationship created successfully!', 'success')
        return redirect(url_for('relationships.list_relationships'))
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
    return render_template('relationships/add.html', form=form)

@relationships_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_relationship(id):
    relationship = Relationship.query.get_or_404(id)
    form = RelationshipForm(obj=relationship)
    if form.validate_on_submit():
        form.populate_obj(relationship)
        db.session.commit()
        flash('Relationship updated successfully!', 'success')
        return redirect(url_for('relationships.list_relationships'))
    return render_template('relationships/edit.html', form=form, relationship=relationship)


@relationships_bp.route('/<int:id>/delete', methods=['POST'])
def delete_relationship(id):
    relationship = Relationship.query.get_or_404(id)
    db.session.delete(relationship)
    db.session.commit()
    return redirect(url_for('relationships.list_relationships'))
