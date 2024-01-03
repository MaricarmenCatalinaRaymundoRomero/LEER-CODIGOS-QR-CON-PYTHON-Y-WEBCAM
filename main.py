from flask import Flask, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/<string:codigo>')
def index(codigo=None):
    mi_conexion = sqlite3.connect("BASE.db")
    cursor = mi_conexion.cursor()
    consulta = cursor.execute("SELECT * FROM REGISTROS")
    consulta = cursor.fetchall()
    contador = len(consulta)

    if codigo != None and codigo != "favicon.ico":
     ahora = datetime.now()
     ahora = str(ahora.strftime("%m/%d/%Y, %H:%M:%S"))
     sql = "INSERT INTO REGISTROS(FECHAHORA, PROVEEDOR) VALUES (?,?)"
     cursor.execute(sql, (ahora, codigo))
     mi_conexion.commit()
     contador = contador + 1


    cursor.close()
    mi_conexion.close()

    return render_template('index.html', codigo=codigo, contador=contador)

if __name__ == '__main__':
    app.run(debug=True)
