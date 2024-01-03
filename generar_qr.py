
"""
PASOS PREVIOS.

1. Se debe tener instalado PYTHON 3 en su computador.
2. Ejecutar desde consola CMD:

pip install qrcode
pip install pandas

"""

import qrcode
import pandas as pd
#LEEMOS LA CANTIDAD DE DATOS DE NUESTRA BASE
data = pd.read_csv('BASE.csv')
print(data.head())

for i in range(len(data)):
    cod_proveedor = data.iloc[i,0]
    nombre_proveedor = data.iloc[i,1]
    
    img = qrcode.make(cod_proveedor)
    img.save(f"img/{nombre_proveedor}.png")