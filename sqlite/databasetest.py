from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, to suppress warning

# Initialize database
db = SQLAlchemy(app)

# Create db model
class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(8), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize the database and create tables
with app.app_context():
    db.create_all()

@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        user_email = request.form['email']
        first_name = request.form['firstName']
        password1 = request.form['password1']
        password2 = request.form['password2']

        if password1 != password2:
            return "Passwords do not match."
        
        new_info = Info(email=user_email, name=first_name, password=password1)
        
        # Push to database
        try:
            db.session.add(new_info)
            db.session.commit()
            return redirect('/sign_up')
        except Exception as e:
            return f"There was an error: {str(e)}"
    else:
        return render_template('sign_up.html')

if __name__ == "__main__":
    app.run(debug=True)