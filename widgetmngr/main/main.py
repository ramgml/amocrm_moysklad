from flask import Blueprint, render_template
from flask_login import login_required, current_user
import sqlite3
from widgetmngr.models import db, User, Account, LeadStatus, CustomFields

blueprint = Blueprint('main', __name__)

@blueprint.route('/')
def index():
    return render_template('index.html')
