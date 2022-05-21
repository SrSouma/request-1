import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

contatos = [
    {'name': 'João da Silva', 'email': 'joao@gmail.com', 'phone': '(16)99922-1122'},
    {'name': 'Maria Souza', 'email': 'maria1@gmail.om', 'phone': '(16)99922-3333'},
]

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  email = db.Column(db.String())
  password = db.Column(db.String())
  created_at = db.Column(db.String())
  updated_at = db.Column(db.String())

class Contacts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  email = db.Column(db.String())
  phone = db.Column(db.String())
  image = db.Column(db.String())
  user_id = db.Column(db.Integer)
  created_at = db.Column(db.String())
  updated_at = db.Column(db.String())

@app.route('/')
def index():
    contacts = Contacts.query.all()
    return render_template(
        'index.html',
        contacts=contacts, contatos=contatos
    )

@app.route('/create', methods=['POST'])
def create():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    contatos.append({
      'name': name, 'email': email, 'phone': phone,
    })
  
    new_contact = Contacts(
      name=name,
      email=email,
      phone=phone
    )
    db.session.add(new_contact)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
  contatos.pop(id)
  return redirect('/')

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  contatos[index]['name'] = name
  contatos[index]['email'] = email
  contatos[index]['phone'] = phone
  return redirect('/')

if __name__ == '__main__':
    db.create_all()
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)