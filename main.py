from flask import Flask
from flask_migrate import Migrate

from database import db
from usuarios import bp_usuarios

#iniciação
app = Flask(__name__)

conexao = "sqlite:///meubanco.sqlite"

#configuracoes app
app.config['SECRET_KEY'] = 'minha-chave'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')
db.init_app(app)

migrate = Migrate(app,db)
@app.route('/')
def index():
    return 'Opa!'


app.run(host='0.0.0.0', port=81)
