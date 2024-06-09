import flask_login
from website import create_app, db
from flask import render_template, request, redirect, session, send_from_directory, Response
from flask import Blueprint, render_template, request, flash, redirect, url_for,jsonify
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
@login_required
def timer():
    return render_template('timer.html')

@main.route('/sound')
@login_required
def sound():
    return render_template('sound.html')

@main.route('/alarm')
@login_required
def alarm():
    return render_template('alarm.html')

@main.route('/bgimage')
@login_required
def bgimage():
    return render_template('bgimage.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

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
@login_required
def serve_song(sound):
    return send_from_directory('static', sound)

@main.route('/store-session', methods=['POST'])
def store_session():
    if request.method == 'POST':
        data = request.get_json()
        session = UserSession.query.filter_by(user_id=data['user_id'], category=data['category']).first()
        if session:
            session.num_session = session.num_session + 1
            db.session.commit()
            return 'session added'
        else:
            new_session = UserSession(user_id=data['user_id'],category=data['category'], num_session=1)
            db.session.add(new_session)
            db.session.commit()
            return 'session created'
        
@main.route('/get-current-user-session', methods=['GET'])
def get_current_user_session():
    user_id = current_user.id
    session = UserSession.query.filter_by(user_id=user_id).order_by(UserSession.id.desc()).first()
    if session:
        return jsonify({'num_session': session.num_session})
    else:
        return jsonify({'num_session': 0})
        
@main.route('/tracker')
@login_required
def tracker():
    current_user = flask_login.current_user
    user_sessions = UserSession.query.filter_by(user_id=current_user.id).all()
    return render_template('track.html', user_sessions=user_sessions)


if __name__ == '__main__':
    main.run(debug=True)
