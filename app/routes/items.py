from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.item import Item
from ..forms import ItemForm
from ..extensions import db

items_bp = Blueprint('items', __name__, url_prefix='/items')

@items_bp.route('/')
def list_items():
    items = Item.query.all()
    return render_template('items/list.html', items=items)

@items_bp.route('/add', methods=['GET', 'POST'])
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        new_item = Item(
            name=form.name.data,
            description=form.description.data,
            type=form.type.data,
            weight=form.weight.data,
            value=form.value.data,
            enchantment=form.enchantment.data,
            owner_id=form.owner_id.data
        )
        db.session.add(new_item)
        db.session.commit()
        flash('Item created successfully!', 'success')
        return redirect(url_for('items_bp.list_items'))
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
    return render_template('items/add.html', form=form)

@items_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    item = Item.query.get_or_404(id)
    form = ItemForm(obj=item)
    if form.validate_on_submit():
        form.populate_obj(item)
        db.session.commit()
        flash('Item updated successfully!', 'success')
        return redirect(url_for('items_bp.list_items'))
    return render_template('items/edit.html', form=form)


@items_bp.route('/<int:id>/delete', methods=['POST'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('items.list_items'))
