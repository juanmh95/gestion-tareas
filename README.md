# Gestión de Tareas

Este es un proyecto de gestión de tareas desarrollado en Python 3.10 con el framework Flask y utilizando SQLite como base de datos.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

- `app` (carpeta)
  - `__init__.py` (archivo)
  - `forms.py` (archivo)
  - `models.py` (archivo)
  - `routes.py` (archivo)
  - `templates` (carpeta)
    - `base.html` (archivo)
    - `index.html` (archivo)
    - `editar_tarea.html` (archivo)
    - `agregar_tarea.html` (archivo)
  - `static` (carpeta)
    - `css` (carpeta)
      - `style.css` (archivo)
- `install.sh` (archivo)
  - Script para instalar las dependencias del proyecto y inicializar la base de datos **Para sistemas Unix-like**.
- `install.bat` (archivo)
  - Script para instalar las dependencias del proyecto y inicializar la base de datos **Para Windows**.
- `config.py`: Archivo de configuración de la aplicación.

## Configuración

Para configurar la aplicación, se utilizan los siguientes componentes:

- Flask: Framework web utilizado para construir la aplicación.
- Flask-SQLAlchemy: Extensión de Flask para interactuar con la base de datos SQLite.
- Flask-Migrate: Extensión de Flask para gestionar las migraciones de la base de datos.

## Razones para Utilizar SQLite3 como Base de Datos

En este proyecto, he optado por utilizar SQLite3 como sistema de gestión de bases de datos por varias razones:

1. **Facilidad de Uso**: SQLite3 es una base de datos ligera y de fácil uso, lo que la hace perfecta para proyectos pequeños y medianos, como una aplicación de gestión de tareas.

2. **Sin Configuración Compleja**: No es necesario configurar un servidor de base de datos por separado. SQLite3 almacena la base de datos en un solo archivo, lo que simplifica la configuración y eliminación de dependencias adicionales.

3. **Sin Mantenimiento Constante**: Al no depender de un servidor externo, no es necesario realizar un mantenimiento constante. SQLite3 se encarga de administrar la base de datos automáticamente.

4. **Portabilidad**: El archivo de base de datos de SQLite3 es portátil y puede copiarse fácilmente entre sistemas operativos, lo que facilita la distribución de la aplicación.

5. **Rendimiento**: Para aplicaciones pequeñas a medianas, SQLite3 ofrece un rendimiento satisfactorio. La velocidad de acceso a los datos es alta debido a la naturaleza local de la base de datos.

6. **Compatibilidad con Python**: SQLite3 se integra perfectamente con Python y cuenta con una biblioteca estándar (`sqlite3`) que permite interactuar con la base de datos de manera eficiente.

7. **Bajo Consumo de Recursos**: SQLite3 utiliza recursos mínimos en comparación con sistemas de base de datos más grandes, lo que es beneficioso para proyectos con recursos limitados.

8. **Licencia de Dominio Público**: SQLite3 se distribuye bajo el dominio público, lo que significa que es de código abierto y gratuito para su uso en proyectos comerciales y no comerciales.

Si bien SQLite3 es una excelente elección para proyectos más simples como este, es importante recordar que tiene limitaciones en cuanto a escalabilidad y concurrencia. Para proyectos que requieran un alto volumen de escrituras concurrentes o una gran cantidad de datos, podriamos considerar otras bases de datos como PostgreSQL o MySQL.

## Funcionalidades

El proyecto de gestión de tareas ofrece las siguientes funcionalidades:

- Listar todas las tareas.
- Agregar una nueva tarea.
- Editar una tarea existente.
- Borrar una tarea.

## Uso

Para ejecutar la aplicación, puedes seguir estos pasos:

1. Clona este repositorio o descarga el código fuente.
2. Asegúrate de tener Python 3.10 instalado en tu sistema.
3. Ejecuta el script de instalación para configurar el entorno, instalar las dependencias y realizar la inicialización de la base de datos:

   **Para sistemas Unix-like:**

   ```bash
   ./install.sh
   ```

   **Para Windows**

   ```bash
   ./install.bat
   ```

4. Ejecuta la aplicación:

   ```bash
   flask run
   ```

La aplicación estará disponible en <http://localhost:5000>.

## Contribuciones

Si deseas contribuir a este proyecto, no dudes en crear un "pull request" o reportar problemas en la sección de problemas.

## Licencia

Este proyecto se encuentra bajo la licencia [MIT](https://opensource.org/license/mit/).

¡Espero que esta aplicación de gestión de tareas te sea útil!
