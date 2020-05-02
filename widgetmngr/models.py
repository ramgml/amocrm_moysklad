from flask_admin import Admin, AdminIndexView
from flask_login import UserMixin, current_user
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.schema import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password = db.Column(db.String(200))
    name = db.Column(db.String(200))
    role = db.Column(db.String(25), index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    @property
    def is_admin(self):
        return self.role == 'admin'

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    amo_login = db.Column(db.String(100), index=True, unique=True)
    amo_hash = db.Column(db.String(40))
    amo_url = db.Column(db.String(100), unique=True, nullable=False)
    ms_auth = db.Column(db.String(72))
    leads = db.relationship('LeadStatus', backref='account', lazy='dynamic')
    customs = db.relationship('CustomFields', backref='account', lazy='dynamic')
    
    def __repr__(self):
        return f'{self.amo_login}'

class LeadStatus(db.Model):
    __tablename__ = 'lead_status'
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    amo_status_id = db.Column(db.Integer)
    ms_status_id = db.Column(db.Integer)

class CustomFields(db.Model):
    __tablename__ = 'custom_fields'
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    amo_field_id = db.Column(db.Integer)
    ms_field_id = db.Column(db.Integer)
