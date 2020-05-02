from getpass import getpass
import sys
import re

from widgetmngr import create_app
from widgetmngr.models import db, User

app = create_app()

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

with app.app_context():
    email = input('Введите email: ')
    
    if User.query.filter(User.email == email).count():
        print(f'Пользователь с таким email: {email}, уже существует в БД.')
        sys.exit(0)

    username = input('Введите имя: ')
    password1 = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')

    if not password1 == password2:
        print('Введенные пароли не совпадают.')
        sys.exit(0)

    new_user = User(email=email, name = username, role = 'admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()

    print(f'Создан пользователь с id = {new_user.id}')
