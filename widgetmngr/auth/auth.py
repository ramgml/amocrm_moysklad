from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from widgetmngr.models import db, User


blueprint = Blueprint('auth', __name__)

@blueprint.route('/login')
def login():
    return render_template('login.html')

@blueprint.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Пожалуйста проверьте данные для авторизации, которые вводите и попробуйте еще раз.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember) 

    return redirect('/admin')


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

class AdminMixin:
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))

class AccountView(AdminMixin, ModelView):
     form_columns = ['amo_login','amo_hash', 'amo_url', 'ms_auth']

class AdminView(AdminMixin, ModelView):
    pass

class HomeAdminView(AdminMixin, AdminIndexView):
    def is_visible(self):
        return False
    pass

