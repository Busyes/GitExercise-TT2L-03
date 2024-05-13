from flask import Flask, render_template, request, redirect
from flask import session

app = Flask(__name__)
app.secret_key = 'my_hard_to_crack_secret_key'

@app.route('/set_alarm', methods=['POST'])
def set_alarm():
    alarm_sound = request.form.get('alarm_sound')
    # Set the alarm sound using the user's selection
    set_alarm_sound(alarm_sound)
    return redirect('/alarm')

@app.route('/alarm')
def alarm():
    # Retrieve the current alarm sound
    alarm_sound = get_alarm_sound()
    return render_template('alarm.html', alarm_sound=alarm_sound)

def set_alarm_sound(alarm_sound):
    # Set the alarm sound in the database or session
    session['alarm_sound'] = alarm_sound

def get_alarm_sound():
    # Retrieve the alarm sound from the database or session
    return session.get('alarm_sound', 'default_alarm.mp3')