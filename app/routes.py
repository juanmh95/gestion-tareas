from app import app, db
from app.models import Tarea
from app.forms import TareaForm
from flask import render_template, redirect, url_for
from datetime import datetime

@app.route('/')
def index():
    tareas = Tarea.query.all()
    current_date = datetime.now()
    return render_template('index.html', tareas=tareas, current_date=current_date)

@app.route('/agregar_tarea', methods=['GET', 'POST'])
def agregar_tarea():
    form = TareaForm()

    if form.validate_on_submit():
        titulo = form.titulo.data
        descripcion = form.descripcion.data
        vencimiento = form.vencimiento.data
        estado = form.estado.data
        tarea = Tarea(titulo, descripcion, vencimiento, estado)
        db.session.add(tarea)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('agregar_tarea.html', form=form)

@app.route('/editar_tarea/<int:id>', methods=['GET', 'POST'])
def editar_tarea(id):
    tarea = Tarea.query.get_or_404(id)
    form = TareaForm(obj=tarea)

    if form.validate_on_submit():
        tarea.titulo = form.titulo.data
        tarea.descripcion = form.descripcion.data
        tarea.vencimiento = form.vencimiento.data
        tarea.estado = form.estado.data
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('editar_tarea.html', form=form, tarea=tarea)

@app.route('/borrar_tarea/<int:id>')
def borrar_tarea(id):
    tarea = Tarea.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for('index'))
