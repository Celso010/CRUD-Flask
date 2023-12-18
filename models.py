from database import db


#tabela para definir e armazenar os usuarios
class Usuario(db.Model):
    
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(100))
    sexo = db.Column(db.String(1))
    data = db.Column(db.String(100))
    
    def __init__(self, nome, cpf, sexo, data):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.data = data

    def __repr__(self):
        return "Usuario: {}".format(self.nome)