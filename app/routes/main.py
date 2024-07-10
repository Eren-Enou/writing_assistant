from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/create')
def create():
    return render_template('create.html')

@main_bp.route('/list')
def list_models():
    return render_template('list.html')