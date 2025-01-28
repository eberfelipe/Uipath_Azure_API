from flask import Flask
from app.routes import routes  # Importando o Blueprint corretamente

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)
    return app

# Criando a instância da aplicação
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
