from datetime import timedelta, datetime

import flask_login
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask import session, send_from_directory
from flask_login import login_required, current_user
from sqlalchemy import func
from website import create_app, db
from website.templates.models import UserSession

main = create_app()

index = Blueprint('index', __name__)


@main.route('/index')
def index():
    return render_template('index.html')


@main.route('/timer')
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
        new_session = UserSession(user_id=current_user.id, category=data['category'])
        db.session.add(new_session)
        db.session.commit()
        return jsonify(success=True)


@main.route('/get-total-sessions', methods=['GET'])
def get_total_sessions():
    if current_user.is_authenticated:
        total_sessions = db.session.query(UserSession).filter_by(user_id=current_user.id).count()
        return jsonify(total_sessions=total_sessions)
    else:
        return jsonify(total_sessions=0), 401


@main.route('/tracker')
@login_required
def tracker():
    current_user = flask_login.current_user
    categories = ['gaming', 'study', 'work', 'hobby']
    session_data = {}

    for category in categories:
        session_count = UserSession.query.filter_by(
            user_id=current_user.id,
            category=category,
        ).count()
        session_data[category] = session_count

    return render_template('track.html', session_data=session_data)


@main.route('/tracker-week')
@login_required
def tracker_week():
    current_user = flask_login.current_user
    last_week_date = datetime.now() - timedelta(days=7)

    categories = ['gaming', 'study', 'work', 'hobby']
    session_data = {}

    for category in categories:
        session_count = UserSession.query.filter_by(
            user_id=current_user.id,
            category=category,
        ).filter(
            UserSession.created_at >= last_week_date
        ).count()
        session_data[category] = session_count

    current_date_str = datetime.now().date()
    last_week_date_str = last_week_date.date()
    return render_template(
        'track-period.html',
        session_data=session_data,
        to_date=current_date_str,
        from_date=last_week_date_str
    )


@main.route('/tracker-month')
@login_required
def tracker_month():
    current_user = flask_login.current_user
    last_month_date = datetime.now() - timedelta(days=30)
    categories = ['gaming', 'study', 'work', 'hobby']
    session_data = {}

    for category in categories:
        session_count = UserSession.query.filter_by(
            user_id=current_user.id,
            category=category,
        ).filter(
            UserSession.created_at >= last_month_date
        ).count()
        session_data[category] = session_count

    current_date_str = datetime.now().date()
    last_month_date_str = last_month_date.date()
    return render_template(
        'track-period.html',
        session_data=session_data,
        to_date=current_date_str,
        from_date=last_month_date_str
    )


@main.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    main.run(debug=True)
