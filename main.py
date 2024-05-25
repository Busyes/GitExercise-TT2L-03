from website import create_app, db
from flask import render_template, request, redirect, session, send_from_directory, Response
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import bcrypt
from website.templates.models import User, UserSession

main = create_app()

index = Blueprint('index', __name__)

@main.route('/index')
def index():
    return render_template('index.html')

@main.route ('/timer')
def timer():
    return render_template('timer.html')

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

@main.route('/sound/<path:sound>')
def serve_song(sound):
    return send_from_directory('static', sound)

@main.route('/store-session', methods=['POST'])
def store_session():
    if request.method == 'POST':
        data = request.get_json()
        session = UserSession.query.filter_by(user_id=data['user_id']).first()
        if session:
            session.num_session = session.num_session + 1
            db.session.commit()
            return 'session added'
        else:
            new_session = UserSession(user_id=data['user_id'], num_session=1)
            db.session.add(new_session)
            db.session.commit()
            return 'session created'

if __name__ == '__main__':
    main.run(debug=True)
