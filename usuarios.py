#enxergar rotas que estão em outros arquivos
from flask import Blueprint, redirect, render_template, request

from database import db
from models import Usuario

bp_usuarios = Blueprint("usuarios", __name__, template_folder = "templates")

@bp_usuarios.route('/create', methods = ['GET', 'POST'])
def create():
  if request.method == 'GET':
    return render_template('usuarios_create.html')
  
  if request.method == 'POST' :
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    request.form.get('csenha')
    
    u = Usuario(nome, email, senha)
    #pesquisar sobre
    db.session.add(u)
    db.session.commit()
    return "opa, deu bom"

  else:
    return "opa, deu ruim"

@bp_usuarios.route('/recovery')
def recovery():
   #pesquisar
   usuarios = Usuario.query.all()
   return render_template('usuarios_recovery.html', usuarios = usuarios)

@bp_usuarios.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
  u = Usuario.query.get(id)
  if request.method == 'GET':
    return render_template('usuarios_update.html', u = u)
  if request.method == 'POST':
    u.nome =  request.form.get('nome')
    u.email = request.form.get('email')
    db.sesssion.add(u)
    db.session.commit()
    return redirect('/usuarios/recovery')
  else :
    return "deu errado!"


@bp_usuarios.route('/delete/<int:id>', methods = ['GET', 'POST'])
def delete(id):
    u = Usuario.query.get(id)
    if request.method == 'GET':
      return render_template('usuarios_delete.html', u = u)
    if request.method == 'POST':
      db.sesssion.delete(u)
      db.session.commit()
      return 'Dados excluidos'
    else:
      return "deu errado!"
  
    


