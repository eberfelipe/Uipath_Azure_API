from flask import Flask
from app.routes import routes  # 🔹 Importando corretamente o Blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)  # 🔹 Registrando as rotas no app
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
