from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "asset_management"

def create_app():
    app = Flask(__name__)

    if os.environ.get('FLASK_ENV') == 'production':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ayush:I9cCMFxrhSbPTH02LCEbrPGbkbRQmwxJ@dpg-cis94qdph6et1se9s7b0-a/asset_management'
        app.config['SECRET_KEY'] = 'secret_key'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://Ayush:hitkar123@localhost/{DB_NAME}'
        app.config['SECRET_KEY'] = 'secret_key'
        
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    from .report_views import report_view

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(report_view, url_prefix="/report")

    from .models import User

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # create_database(app)

    return app

