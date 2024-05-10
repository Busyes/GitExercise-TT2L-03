from website import create_app
from flask import render_template, request, redirect, session
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import bcrypt

main = create_app()

index = Blueprint('index', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/sound')
def sound():
    return render_template('sound.html')

@main.route('/alarm')
def alarm():
    return render_template('alarm.html')

@main.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    main.run(debug=True)

