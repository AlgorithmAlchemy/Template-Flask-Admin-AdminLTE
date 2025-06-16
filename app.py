from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, expose, AdminIndexView
from flask_adminlte3 import AdminLTE3
from flask_admin.contrib.sqla import ModelView

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin_layout.html')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Выбери тему Bootswatch здесь:
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'  # например, cerulean, flatly, darkly и др.



# Подключаем расширения
db = SQLAlchemy(app)
AdminLTE3(app)  # ← Вот и вся магия

# Пример модели
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(120))

# Создаём таблицы
with app.app_context():
    db.create_all()

# Настройка Flask-Admin
admin = Admin(app, name='AdminLTE Panel', index_view=MyAdminIndexView())
admin.add_view(ModelView(User, db.session))

if __name__ == '__main__':
    app.run(debug=True)
