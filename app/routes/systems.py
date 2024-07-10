from flask import Blueprint, render_template, request, redirect, url_for
from ..models.system import System
from ..extensions import db

systems_bp = Blueprint('systems', __name__, url_prefix='/systems')

@systems_bp.route('/')
def list_systems():
    systems = System.query.all()
    return render_template('systems/list.html', systems=systems)

@systems_bp.route('/add', methods=['GET', 'POST'])
def add_system():
    if request.method == 'POST':
        new_system = System(
            name=request.form['name'],
            description=request.form['description'],
            rules=request.form.get('rules'),
            basis=request.form.get('basis'),
            world_id=request.form['world_id']
        )
        db.session.add(new_system)
        db.session.commit()
        return redirect(url_for('systems.list_systems'))
    return render_template('systems/add.html')

@systems_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_system(id):
    system = System.query.get_or_404(id)
    if request.method == 'POST':
        system.name = request.form['name']
        system.description = request.form['description']
        system.rules = request.form.get('rules')
        system.basis = request.form.get('basis')
        system.world_id = request.form['world_id']
        db.session.commit()
        return redirect(url_for('systems.list_systems'))
    return render_template('systems/edit.html', system=system)

@systems_bp.route('/<int:id>/delete', methods=['POST'])
def delete_system(id):
    system = System.query.get_or_404(id)
    db.session.delete(system)
    db.session.commit()
    return redirect(url_for('systems.list_systems'))
