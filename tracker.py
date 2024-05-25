from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#init database
db = SQLAlchemy(app)

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')


cursor.execute('''
INSERT INTO users (name, age) VALUES (?, ?)
''', ('Alice', 30))

cursor.execute('''
INSERT INTO users (name, age) VALUES (?, ?)
''', ('Bob', 25))

cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Update data
cursor.execute('''
UPDATE users SET age = ? WHERE name = ?
''', (31, 'Alice'))

# Commit changes
conn.commit()

# Delete data
cursor.execute('''
DELETE FROM users WHERE name = ?
''', ('Bob',))

# Commit changes
conn.commit()

# Query data again
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()

#db model
class Timer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    time = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Timer {self.name}>'

@app.route('/timerdata', methods=['POST'])
def create_timer():
    data = request.get_json()
    new_timer = Timer(name=data['name'], time=data['time'], user_id=data['user_id'])
    db.session.add(new_timer)
    db.session.commit()
    return jsonify({'message': 'Timer created'}), 201

@app.route('/timerdata/<int:timer_id>', methods=['PUT'])
def update_timer(timer_id):
    data = request.get_json()
    timer = Timer.query.get_or_404(timer_id)
    timer.name = data['name']
    timer.time = data['time']
    timer.user_id = data['user_id']
    db.session.commit()
    return jsonify({'message': 'Timer updated'})

@app.route('/timerdata/<int:timer_id>', methods=['DELETE'])
def delete_timer(timer_id):
    timer = Timer.query.get_or_404(timer_id)
    db.session.delete(timer)
    db.session.commit()
    return jsonify({'message': 'Timer deleted'})

if __name__ == '__main__':
    app.run(debug=True)