import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'widgetmngr/widgetmngr.db')
SECRET_KEY = 'FCy12e&@&AW*@J2109e22rjJF21-9723871'

SQLALCHEMY_TRACK_MODIFICATIONS = False