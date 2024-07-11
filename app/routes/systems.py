from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import text
from ..models.system import System
from ..forms import SystemForm
from ..extensions import db

systems_bp = Blueprint('systems', __name__, url_prefix='/systems')

@systems_bp.route('/')
def list_systems():
    sort_by = request.args.get('sort_by', 'name')
    search = request.args.get('search', '')

    if sort_by not in ['name', 'world_id']:
        sort_by = 'name'

    query = System.query
    if search:
        query = query.join(World, System.world_id == World.id).filter(
            System.name.ilike(f'%{search}%') |
            System.description.ilike(f'%{search}%') |
            System.rules.ilike(f'%{search}%') |
            World.name.ilike(f'%{search}%')
        )

    systems = query.order_by(text(sort_by)).all()
    return render_template('systems/list.html', systems=systems, sort_by=sort_by)



@systems_bp.route('/add', methods=['GET', 'POST'])
def add_system():
    form = SystemForm()
    if form.validate_on_submit():
        new_system = System(
            name=form.name.data,
            description=form.description.data,
            rules=form.rules.data,
            basis=form.basis.data
        )
        new_system.worlds = form.worlds.data
        db.session.add(new_system)
        db.session.commit()
        flash('System created successfully!', 'success')
        return redirect(url_for('systems.list_systems'))
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
    return render_template('systems/add.html', form=form)

@systems_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_system(id):
    system = System.query.get_or_404(id)
    form = SystemForm(obj=system)
    if form.validate_on_submit():
        form.populate_obj(system)
        db.session.commit()
        flash('System updated successfully!', 'success')
        return redirect(url_for('systems.list_systems'))
    return render_template('systems/edit.html', form=form, system=system)


@systems_bp.route('/<int:id>/delete', methods=['POST'])
def delete_system(id):
    system = System.query.get_or_404(id)
    db.session.delete(system)
    db.session.commit()
    return redirect(url_for('systems.list_systems'))
