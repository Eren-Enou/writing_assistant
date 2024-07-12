from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

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

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('user/dashboard.html')