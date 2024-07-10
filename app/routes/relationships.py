from flask import Blueprint, render_template, request, redirect, url_for
from ..models.relationship import Relationship
from ..extensions import db

relationships_bp = Blueprint('relationships', __name__, url_prefix='/relationships')

@relationships_bp.route('/')
def list_relationships():
    relationships = Relationship.query.all()
    return render_template('relationships/list.html', relationships=relationships)

@relationships_bp.route('/add', methods=['GET', 'POST'])
def add_relationship():
    if request.method == 'POST':
        new_relationship = Relationship(
            character1_id=request.form['character1_id'],
            character2_id=request.form['character2_id'],
            relationship_type=request.form['relationship_type'],
            description=request.form.get('description'),
            level=request.form.get('level'),
            is_romantic=request.form.get('is_romantic') == 'on',
            is_supportive=request.form.get('is_supportive') == 'on',
            is_rival=request.form.get('is_rival') == 'on',
            is_ally=request.form.get('is_ally') == 'on',
            is_conflict=request.form.get('is_conflict') == 'on'
        )
        db.session.add(new_relationship)
        db.session.commit()
        return redirect(url_for('relationships.list_relationships'))
    return render_template('relationships/add.html')

@relationships_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_relationship(id):
    relationship = Relationship.query.get_or_404(id)
    if request.method == 'POST':
        relationship.character1_id = request.form['character1_id']
        relationship.character2_id = request.form['character2_id']
        relationship.relationship_type = request.form['relationship_type']
        relationship.description = request.form.get('description')
        relationship.level = request.form.get('level')
        relationship.is_romantic = request.form.get('is_romantic') == 'on'
        relationship.is_supportive = request.form.get('is_supportive') == 'on'
        relationship.is_rival = request.form.get('is_rival') == 'on'
        relationship.is_ally = request.form.get('is_ally') == 'on'
        relationship.is_conflict = request.form.get('is_conflict') == 'on'
        db.session.commit()
        return redirect(url_for('relationships.list_relationships'))
    return render_template('relationships/edit.html', relationship=relationship)

@relationships_bp.route('/<int:id>/delete', methods=['POST'])
def delete_relationship(id):
    relationship = Relationship.query.get_or_404(id)
    db.session.delete(relationship)
    db.session.commit()
    return redirect(url_for('relationships.list_relationships'))
