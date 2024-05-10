from website import create_app
from flask import render_template, request, redirect, session, send_from_directory, Response
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import bcrypt

main = create_app()

index = Blueprint('index', __name__)

@main.route('/index')
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

@main.route('/logo')
def logo():
    return render_template('logo.png')

@main.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@main.route('/static/<path:logo>')
def send_static(logo):
    return send_from_directory('static/images', logo)

@main.route('/audio/<path:audio>')
def send_audio(audio):
    return send_from_directory('static/audio', audio)

if __name__ == '__main__':
    main.run(debug=True)
