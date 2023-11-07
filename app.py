from flask import Flask, request, render_template, redirect, url_for
from app.models import Tarea

app = Flask(__name__, template_folder= 'templates')

tareas = []

@app.route('/')
def index():
    return render_template('index.html', tareas=tareas)

@app.route('/agregar_tarea', methods=['POST'])
def agregar_tarea():
    titulo = request.form['titulo']
    descripcion = request.form['descripcion']
    vencimiento = request.form['vencimiento']
    estado = request.form['estado']

    tarea = Tarea(titulo, descripcion, vencimiento, estado)
    tareas.append(tarea)
    return redirect(url_for('index'))

@app.route('/editar_tarea/<int:index>', methods=['GET', 'POST'])
def editar_tarea(index):
    tarea = tareas[index]

    if request.method == 'POST':
        tarea.titulo = request.form['titulo']
        tarea.descripcion = request.form['descripcion']
        tarea.vencimiento = request.form['vencimiento']
        tarea.estado = request.form['estado']
        return redirect(url_for('index'))
    
    return render_template('editar_tarea.html', tarea=tarea, index=index)

@app.route('/borrar_tarea/<int:index>')
def borrar_tarea(index):
    tareas.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
