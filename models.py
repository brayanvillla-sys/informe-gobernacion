from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), nullable=False)  # admin o trabajador
    informes = db.relationship('Informe', backref='autor', lazy=True)

class Informe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_evento = db.Column(db.String(80), nullable=False)
    telefono = db.Column(db.String(40), nullable=False)
    lugar = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.String(20), nullable=False)
    fotos = db.Column(db.Text, nullable=False)  # rutas separadas por ;
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creado = db.Column(db.DateTime, server_default=db.func.now())
    pagado = db.Column(db.Boolean, default=False)