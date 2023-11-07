from app import db

class Tarea(db.Model):
    __tablename__ = 'tarea'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    vencimiento = db.Column(db.DateTime)
    estado = db.Column(db.String(20))

    def __init__(self, titulo, descripcion, vencimiento, estado):
        self.titulo = titulo
        self.descripcion = descripcion
        self.vencimiento = vencimiento
        self.estado = estado
