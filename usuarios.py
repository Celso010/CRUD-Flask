#enxergar rotas que estão em outros arquivos
from datetime import datetime

from flask import (
  Blueprint,
  flash,
  get_flashed_messages,
  render_template,
  request,
)
from validate_docbr import CPF

from database import db
from models import Usuario

bp_usuarios = Blueprint("usuarios", __name__, template_folder = "templates")

@bp_usuarios.route("/menu")
def menu():
  messages = get_flashed_messages()
  return render_template("usuarios_menu.html", messages = messages)
  
@bp_usuarios.route('/create', methods = ['GET', 'POST'])
def create():
  if request.method == 'GET':
    return render_template('usuarios_create.html')
  
  elif request.method == 'POST' :
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    sexo = request.form.get('sexo')
    data = request.form.get('data')

    if not nome.replace(" ","").isalpha():
      flash('Por favor, insira um nome válido.', 'error')
      return render_template('usuarios_create.html')

    cpf_validator = CPF()
    if not cpf_validator.validate(cpf):
     flash('CPF inválido, por favor insira um CPF válido', 'error')
     return render_template('usuarios_create.html')


    if sexo not in ('M','m','f','F'):
      flash('Por favor, insira um sexo válido (M ou F).', 'error')
      return render_template('usuarios_create.html')


    try:
      data_valida = datetime.strptime(data, '%d/%m/%Y')
    except ValueError:
      flash('Data inválida, por favor insira uma data no formato DD/MM/AAAA', 'error')
      return render_template('usuarios_create.html')



    
    u = Usuario(nome, cpf, sexo, data)
    try:
            db.session.add(u)
            db.session.commit()
            return  render_template('usuarios_menu.html')
    except Exception:
            db.session.rollback()
    return render_template('usuarios_menu.html')
   
  else:
    return "opa, deu ruim"

@bp_usuarios.route('/recovery')
def recovery():
   usuarios = Usuario.query.all()
   return render_template('usuarios_recovery.html', usuarios = usuarios)

@bp_usuarios.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
  u = Usuario.query.get(id)
  if u is None:
    return "O usuário não existe"
    
  if request.method == 'GET':
    return render_template('usuarios_update.html', u = u)
  elif request.method == 'POST':
    u.nome =  request.form.get('nome')
    u.cpf = request.form.get('cpf')
    u.sexo = request.form.get('sexo')
    u.data = request.form.get('data')
    db.session.add(u)
    db.session.commit()
    return   render_template('usuarios_menu.html')
  else :
    return "deu errado!"


@bp_usuarios.route('/delete/<int:id>', methods = ['GET', 'POST'])
def delete(id):
    u = Usuario.query.get(id)
    if u is None:
        return "O usuário não existe"
    if request.method == 'GET':
      return render_template('usuarios_delete.html', u = u)
    elif request.method == 'POST':
      db.session.delete(u)
      db.session.commit()
      flash(f'Usuário {u.nome} excluído com sucesso!', 'success')
      return   render_template('usuarios_menu.html')
    else:
      return "deu errado!"
  
    


