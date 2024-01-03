from flask import Flask, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/<string:codigo>')
def index(codigo=None):
    # Conectar a la base de datos SQLite
    with sqlite3.connect("BASE.db") as mi_conexion:
        cursor = mi_conexion.cursor()

        # Ejecutar una consulta SELECT para recuperar todos los registros de la tabla "REGISTROS"
        consulta = cursor.execute("SELECT * FROM REGISTROS")
        consulta = cursor.fetchall()

        # Contar el número de registros
        contador = len(consulta)

        # Verificar si se proporciona un código y no es una solicitud de favicon.ico
        if codigo != None and codigo != "favicon.ico":
            # Obtener la fecha y hora actual y darle formato
            ahora = datetime.now()
            ahora = str(ahora.strftime("%m/%d/%Y, %H:%M:%S"))

            # Insertar un nuevo registro en la tabla "REGISTROS"
            sql = "INSERT INTO REGISTROS(FECHAHORA, PROVEEDOR) VALUES (?, ?)"
            cursor.execute(sql, (ahora, codigo))
            
            # Confirmar la transacción
            mi_conexion.commit()

            # Incrementar el contador de registros
            contador += 1

        # Cerrar el cursor y la conexión a la base de datos
        cursor.close()

    # Renderizar la plantilla HTML con la información relevante
    return render_template('index.html', codigo=codigo, contador=contador)

if __name__ == '__main__':
    # Ejecutar la aplicación Flask en modo de depuración
    app.run(debug=True)
