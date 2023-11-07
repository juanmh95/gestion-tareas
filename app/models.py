from datetime import datetime

class Tarea:

    def __init__(self, titulo, descripcion, vencimiento, estado):
        self.titulo = titulo
        self.descripcion = descripcion
        self.vencimiento = vencimiento
        self.estado = estado
        self.creacion = datetime.now()
