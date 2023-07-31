from flask import Flask, session, g, render_template
from flask_caching import Cache
import redis
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
DB_NAME = "asset_management"
cache = Cache()
def create_app():
    app = Flask(__name__)

    if os.environ.get('FLASK_ENV') == 'production':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ayush:I9cCMFxrhSbPTH02LCEbrPGbkbRQmwxJ@dpg-cis94qdph6et1se9s7b0-a/asset_management'
        app.config['SECRET_KEY'] = 'secret_key'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://Ayush:hitkar123@localhost/{DB_NAME}'
        app.config['SECRET_KEY'] = 'secret_key'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CACHE_TYPE'] = 'redis'
    app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'

    

    db.init_app(app)
    migrate = Migrate(app, db)
    cache.init_app(app)
    from .views import views
    from .auth import auth
    from .report_views import report_view

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(report_view, url_prefix="/report")

    from .models import User, Organization

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    @app.context_processor
    def inject_organization_name():
        if 'organization_id' in session:
        # Fetch the organization details based on the organization ID from the database
            organization_id = session['organization_id']
            organization = Organization.query.get(organization_id)
            if organization:
                # Return the organization name as a context variable
                return {'organization_name': organization.name}
        return {'organization_name': None}

    # create_database(app)

    return app

