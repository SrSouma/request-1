from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

contatos = [
    {'name': 'João da Silva', 'email': 'joao@gmail.com', 'phone': '(16)99922-1122'},
    {'name': 'Maria Souza', 'email': 'maria1@gmail.com', 'phone': '(16)99922-3333'},
]

class User(db.Model):
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
  contacts.pop(id)
  return redirect('/')

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  contacts[index]['name'] = name
  contacts[index]['email'] = email
  contacts[index]['phone'] = phone
  return redirect('/')

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=8080)