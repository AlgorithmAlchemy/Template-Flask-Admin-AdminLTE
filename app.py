from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, expose, AdminIndexView, BaseView
from flask_adminlte3 import AdminLTE3
from flask_admin.contrib.sqla import ModelView


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin_layout.html')


class DashboardView(BaseView):
    @expose('/')
    def index(self):
        return self.render('dashboard.html')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

db = SQLAlchemy(app)
AdminLTE3(app)


# Model example
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(120))


# Create table
with app.app_context():
    db.create_all()

# Settings Flask-Admin
admin = Admin(app, name='AdminLTE Panel', index_view=MyAdminIndexView())
admin.add_view(DashboardView(name='Dashboard', endpoint='dashboard'))
admin.add_view(ModelView(User, db.session))

if __name__ == '__main__':
    app.run(debug=True)
