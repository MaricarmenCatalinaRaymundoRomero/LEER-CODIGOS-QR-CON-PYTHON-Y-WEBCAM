"""
PASOS PREVIOS.

1. Se debe tener instalado PYTHON 3 en su computador.
2. Ejecutar desde consola CMD:

pip install qrcode
pip install pandas

"""

import qrcode
import pandas as pd

# LEEMOS LA CANTIDAD DE DATOS DE NUESTRA BASE
data = pd.read_csv('BASE.csv')
print(data.head())

# Iteramos sobre cada fila de los datos
for i in range(len(data)):
    # Obtenemos el código del proveedor y su nombre
    cod_proveedor = data.iloc[i, 0]
    nombre_proveedor = data.iloc[i, 1]
    
    # Creamos un código QR con el código del proveedor
    img = qrcode.make(cod_proveedor)
    
    # Guardamos la imagen con el nombre del proveedor en la carpeta 'img'
    img.save(f"img/{nombre_proveedor}.png")
