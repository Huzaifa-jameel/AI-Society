from flask import Blueprint, render_template, request, redirect, url_for
from flask_wtf.csrf import validate_csrf
from wtforms.validators import ValidationError

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/register', methods=['POST'])
def register():
    try:
        validate_csrf(request.form.get('csrf_token'))
        name = request.form.get('reg-name')
        email = request.form.get('reg-email')
        year = request.form.get('reg-year')
        print(f"Form received: {name}, {email}, {year}")
        return redirect(url_for('main.index'))
    except ValidationError:
        return "Invalid CSRF token", 400