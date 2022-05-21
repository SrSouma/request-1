import os
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

contatos = [
    {'name': 'João da Silva', 'email': 'joao@gmail.com', 'phone': '(16)99922-1122'},
    {'name': 'Maria Souza', 'email': 'maria1@gmail.com', 'phone': '(16)99922-3333'},
]

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  password = db.Column(db.String(30))
  created_at = db.Column(db.String(100))
  updated_at = db.Column(db.String(100))

class Contacts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  phone = db.Column(db.String(100))
  image = db.Column(db.String(100)) 
  user_id = db.Column(db.Integer)
  created_at = db.Column(db.String(100))
  updated_at = db.Column(db.String(100))



@app.route('/')
def index():
    if 'user_id' not in session: 
      return redirect('/login')
      
    contacts = Contacts.query.all()
    return render_template(
        'index.html',
        contatos=contatos, contacts=contacts
    
      
    )

@app.route('/create', methods=['POST'])
def create():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    newcontacts = Contacts(
      name = name, email = email, phone = phone
    )
    db.session.add(newcontacts)
    db.session.commit()    
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
  newcontacts = Contacts.query.filter_by(id=id).first()
  db.session.delete(newcontacts)
  db.session.commit()
  return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  newcontacts = Contacts.query.filter_by(id=id).first()
  newcontacts.name = name
  newcontacts.email = email
  newcontacts.phone = phone
  db.session.commit()
  return redirect('/')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/register')
def register():
  return render_template('register.html')

@app.route('/signin', methods=['POST'])
def signin():
  email = request.form.get('email')
  password = request.form.get('password')
  user = Users.query.filter_by(email=email).first()
  if not user:
    return redirect('/login')
  if not check_password_hash(user.password, password):
    return redirect('/login')
  else:
    session['user_id'] = user.id
    return redirect('/')

@app.route('/signup', methods=['POST'])
def signup():
  name = request.form.get('name')
  email = request.form.get('email')
  password = request.form.get('password')
  user = Users.query.filter_by(email=email).first()
  if user:
    return redirect('/register')
  else:
    new_user = Users(email=email, name=name, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')

@app.route('/logout')
def logout():
  if 'user_id' in session:
      session.pop('user_id', None)
  return redirect('/')

if __name__ == '__main__':
    db.create_all()
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)