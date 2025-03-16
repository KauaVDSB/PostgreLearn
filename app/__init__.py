from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Instância do SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuração da URI do banco de dados
    DATABASE_URL = os.getenv(
        "DATABASE_URL"  # Busca a URI das variáveis de ambiente
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensões
    db.init_app(app)

    # Registrar rotas e criar tabelas
    with app.app_context():
        from .routes import main  # Importar o blueprint das rotas
        app.register_blueprint(main)

        # Criar as tabelas no banco de dados
        db.create_all()

    return app
