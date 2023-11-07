#!/bin/bash

# Crear y activar un entorno virtual
python3.10 -m venv venv
source venv/bin/activate

# Instalar paquetes requeridos de Python
pip install -r requirements.txt

# Inicializar y actualizar la base de datos
flask db init
flask db migrate
flask db upgrade
