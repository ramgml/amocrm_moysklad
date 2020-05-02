from flask import Flask
from flask_admin import Admin

from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import os

from widgetmngr.auth.auth import blueprint as auth_blueprint
from widgetmngr.main.main import blueprint as main_blueprint

from widgetmngr.auth.auth import AccountView, HomeAdminView, AdminView

from widgetmngr.models import db, User, Account, CustomFields, LeadStatus

def create_app():
    app = Flask(__name__)
       
    app.config.from_pyfile('config.py')
    app.config["SECRET_KEY"]
    app.config["SQLALCHEMY_DATABASE_URI"]
    
    db.init_app(app)
    MIGRATION_DIR = os.path.join('widgetmngr', 'migrations')
    migrate = Migrate(app, db, directory=MIGRATION_DIR)


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' 
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
        
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    admin = Admin(app, 'Widget Manager', url='/',  index_view=HomeAdminView(name='Home'),template_mode='bootstrap3')

    admin.add_view(AccountView(Account, db.session))
    admin.add_view(AdminView(CustomFields, db.session))
    admin.add_view(AdminView(LeadStatus, db.session))

    return app
