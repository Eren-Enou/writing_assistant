from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import text
from ..models.item import Item
from ..forms import ItemForm
from ..extensions import db

items_bp = Blueprint('items', __name__, url_prefix='/items')

@items_bp.route('/')
def list_items():
    sort_by = request.args.get('sort_by', 'name')
    search = request.args.get('search', '')

    if sort_by not in ['name', 'type', 'value']:
        sort_by = 'name'

    query = Item.query
    if search:
        query = query.filter(
            Item.name.ilike(f'%{search}%') |
            Item.description.ilike(f'%{search}%') |
            Item.type.ilike(f'%{search}%')
        )

    items = query.order_by(text(sort_by)).all()
    return render_template('items/list.html', items=items, sort_by=sort_by)



@items_bp.route('/add', methods=['GET', 'POST'])
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        new_item = Item(
            name=form.name.data,
            description=form.description.data,
            item_type=form.item_type.data,
            weight=form.weight.data,
            value=form.value.data,
            enchantment=form.enchantment.data,
            owner_id=form.owner.data.id if form.owner.data else None
        )
        db.session.add(new_item)
        db.session.commit()

        # Add multiple associations
        for location in form.locations.data:
            new_item.locations.append(location)
        for event in form.events.data:
            new_item.events.append(event)

        db.session.commit()
        flash('Item created successfully!', 'success')
        return redirect(url_for('items.list_items'))
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
        return redirect(url_for('items.list_items'))
    return render_template('items/edit.html', form=form, item=item)


@items_bp.route('/<int:id>/delete', methods=['POST'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('items.list_items'))
