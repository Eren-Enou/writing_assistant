from flask import Blueprint, render_template, request, redirect, url_for
from ..models.item import Item
from ..extensions import db

items_bp = Blueprint('items', __name__, url_prefix='/items')

@items_bp.route('/')
def list_items():
    items = Item.query.all()
    return render_template('items/list.html', items=items)

@items_bp.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        new_item = Item(
            name=request.form['name'],
            description=request.form['description'],
            type=request.form['type'],
            weight=request.form.get('weight'),
            value=request.form.get('value'),
            enchantment=request.form.get('enchantment'),
            owner_id=request.form.get('owner_id')
        )
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('items.list_items'))
    return render_template('items/add.html')

@items_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_item(id):
    item = Item.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.description = request.form['description']
        item.type = request.form['type']
        item.weight = request.form.get('weight')
        item.value = request.form.get('value')
        item.enchantment = request.form.get('enchantment')
        item.owner_id = request.form.get('owner_id')
        db.session.commit()
        return redirect(url_for('items.list_items'))
    return render_template('items/edit.html', item=item)

@items_bp.route('/<int:id>/delete', methods=['POST'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('items.list_items'))
