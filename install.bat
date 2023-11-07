@echo off

rem Crear y activar un entorno virtual
python3.10 -m venv venv
venv\Scripts\activate

rem Instalar paquetes requeridos de Python
pip install -r requirements.txt

rem Inicializar y actualizar la base de datos
flask db init
flask db migrate
flask db upgrade
