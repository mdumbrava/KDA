from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import KEY, SQL

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = KEY

    app.config['SQLALCHEMY_DATABASE_URI'] = SQL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    db.init_app(app)

    # Authenticate Blueprint
    from KDA.Auth import bp as Auth
    app.register_blueprint(Auth)

    # KDA Blueprint
    from KDA.KDA import bp as KDA
    app.register_blueprint(KDA)

    # Ahri Blueprint
    from KDA.Ahri import bp as Ahri
    app.register_blueprint(Ahri)

    # # Akali Blueprint
    from KDA.Akali import bp as Akali
    app.register_blueprint(Akali)
    
    # # Evelyn Blueprint
    from KDA.Evelyn import bp as Evelyn
    app.register_blueprint(Evelyn)
 
    # # Kai'sa Blueprint
    from KDA.Kaisa import bp as Kaisa
    app.register_blueprint(Kaisa)
    
    # # Seraphine Blueprint
    from KDA.Seraphine import bp as Seraphine
    app.register_blueprint(Seraphine)

    return app