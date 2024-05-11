from flask import Flask, render_template, request, redirect, url_for
import time
import datetime

app = Flask(__name__)

# Initialize variables
work_session = 25  # 25 minutes
break_session = 5  # 5 minutes
session_count = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global session_count
    if request.method == 'POST':
        if request.form['submit'] == 'Start':
            session_count += 1
            return redirect(url_for('pomodoro'))
        elif request.form['submit'] == 'Reset':
            session_count = 0
            return redirect(url_for('index'))
    return render_template('timer.html')

@app.route('/pomodoro', methods=['GET', 'POST'])
def pomodoro():
    global session_count
    if request.method == 'POST':
        if request.form['submit'] == 'Take Break':
            return redirect(url_for('break_time'))
        elif request.form['submit'] == 'Skip Break':
            session_count += 1
            return redirect(url_for('pomodoro'))
    t_now = datetime.datetime.now()
    t_fut = t_now + datetime.timedelta(minutes=work_session)
    return render_template('timer.html', t_fut=t_fut, session_count=session_count)

@app.route('/break', methods=['GET', 'POST'])
def break_time():
    global session_count
    if request.method == 'POST':
        if request.form['submit'] == 'Back to Work':
            session_count += 1
            return redirect(url_for('pomodoro'))
    t_now = datetime.datetime.now()
    t_fut = t_now + datetime.timedelta(minutes=break_session)
    return render_template('timer.html', t_fut=t_fut, session_count=session_count)

if __name__ == '__main__':
    app.run(debug=True)