from flask import Flask, render_template, request, redirect

app = Flask(__name__)

contatos = [
    {'name': 'João da Silva', 'email': 'joao@gmail.com', 'phone': '(16)99922-1122'},
    {'name': 'Maria Souza', 'email': 'maria1@gmail.om', 'phone': '(16)99922-3333'},
]

@app.route('/')
def index():
    return render_template(
        'index.html',
        contatos=contatos
    )

@app.route('/create', methods=['POST'])
def create():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    contatos.append({
      'name': name, 'email': email, 'phone': phone,
    })
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
    app.run(host='0.0.0.0', port=8080)