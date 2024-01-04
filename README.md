# LEER CODIGOS QR CON PYTHON Y WEBCAM
- El proposito de este proyecto es que al momento de ejecutar en el comando con el archico "main.py", pueda abrir un codigo y diga la ruta de la pagina. Abrimos la ruta de la pagina y nos mostrara una camara donde mostraremos el qr y nos dira que se verifico correctamente.
- En la base de datos "DB Browser (SQLite)", se mostrara las veces que se verifique el qr en la camara.

1.- En el excel creamos los identidades de la tabla. Su nombre de la base de datos es "BASE".
![image](https://github.com/MaricarmenCatalinaRaymundoRomero/LEER-CODIGOS-QR-CON-PYTHON-Y-WEBCAM/assets/129924045/4afce23e-c9b4-4fc2-813a-5f473d97c421)

2.-El codigo "generar_qr.py" automatiza la generación de códigos QR para cada proveedor, lo que puede ser beneficioso en diversas aplicaciones donde se requiere una identificación rápida y única asociada a cada proveedor.

![image](https://github.com/MaricarmenCatalinaRaymundoRomero/LEER-CODIGOS-QR-CON-PYTHON-Y-WEBCAM/assets/129924045/28856d92-f1c6-4676-8775-17d31ec9e820)

3.- En el CMD dentro de la carpeta, escribimos "python generar_qr.py" para que pueda crear los qr de cada identidades.

![image](https://github.com/MaricarmenCatalinaRaymundoRomero/LEER-CODIGOS-QR-CON-PYTHON-Y-WEBCAM/assets/129924045/b9a2c8cb-f949-4926-a7be-a46603bd34db)

![Captura de pantalla (9)](https://github.com/MaricarmenCatalinaRaymundoRomero/LEER-CODIGOS-QR-CON-PYTHON-Y-WEBCAM/assets/129924045/19e82a46-cf03-42ba-9271-3b687bf9eaeb)

4.- El codigo del "main.py", este código crea una aplicación web simple que muestra información sobre registros almacenados en una base de datos SQLite llamada "BASE.db". La aplicación permite la inserción de nuevos registros cuando se proporciona un código en la URL. La información se presenta en una plantilla HTML llamada "index.html". La aplicación se ejecuta en modo de depuración cuando se ejecuta directamente desde el script.

![image](https://github.com/MaricarmenCatalinaRaymundoRomero/LEER-CODIGOS-QR-CON-PYTHON-Y-WEBCAM/assets/129924045/1e40ee73-4925-4f23-89dd-d8f8a81f722d)

![image](https://github.com/MaricarmenCatalinaRaymundoRomero/LEER-CODIGOS-QR-CON-PYTHON-Y-WEBCAM/assets/129924045/6855182c-adff-4afc-a6af-026578e77ef3)

5.-El codigo "generar_qr.py" automatiza la generación de códigos QR para cada proveedor, lo que puede ser beneficioso en diversas aplicaciones donde se requiere una identificación rápida y única asociada a cada proveedor.

![image](https://github.com/MaricarmenCatalinaRaymundoRomero/LEER-CODIGOS-QR-CON-PYTHON-Y-WEBCAM/assets/129924045/28856d92-f1c6-4676-8775-17d31ec9e820)

6-El archivo "BASE.xlsx" le comvertimos en "csv" y luego lo abrimos en el sql server y lo combertimos en "db" porque en el programa "DB Browser (SQLite)"solo permite siertos tipos de archivos.

![image](https://github.com/MaricarmenCatalinaRaymundoRomero/LEER-CODIGOS-QR-CON-PYTHON-Y-WEBCAM/assets/129924045/8ab087e0-ce32-4aae-89e3-33f5363a4caa)

```
CREATE TABLE REGISTROS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    FECHAHORA TEXT NOT NULL,
    PROVEEDOR TEXT NOT NULL
);
```

7.- Ejecutar en la consola CMD, "python main.py" y lo que se muestra copiamos el url "http://127.0.0.1:5000/". Lo pegamos en nuestro navegador.
![Captura de pantalla (13)](https://github.com/MaricarmenCatalinaRaymundoRomero/LEER-CODIGOS-QR-CON-PYTHON-Y-WEBCAM/assets/129924045/bdd37802-c489-492c-b140-b15e81757374)


![WhatsApp Image 2024-01-04 at 2 32 02 PM](https://github.com/MaricarmenCatalinaRaymundoRomero/LEER-CODIGOS-QR-CON-PYTHON-Y-WEBCAM/assets/129924045/0ca7e559-b81a-48cb-9355-78cb4db3031d)


![Captura de pantalla (16)](https://github.com/MaricarmenCatalinaRaymundoRomero/LEER-CODIGOS-QR-CON-PYTHON-Y-WEBCAM/assets/129924045/87bee6b2-c180-425e-bb2c-074c948a8917)
