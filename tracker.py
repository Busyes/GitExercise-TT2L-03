from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#init database
db = SQLAlchemy(app)

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