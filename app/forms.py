from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField
from wtforms.validators import DataRequired

class TareaForm(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    vencimiento = DateField('Vencimiento', format='%Y-%m-%d', validators=[DataRequired()])
    estado = SelectField('Estado', choices=[
        ('Pendiente', 'Pendiente'),
        ('En Progreso', 'En Progreso'),
        ('Completado', 'Completado'),
        ('Cancelado', 'Cancelado'),
        ('Atrasado', 'Atrasado')
        ])
