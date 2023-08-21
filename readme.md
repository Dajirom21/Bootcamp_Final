# WEB CRYPTOMONEDAS
- Proyecto Final BootCamp Zero- KeepCoding

- Aplicación web de cryptomonedas con  Flask

- Simulador de conversión, tradeo e inversión en Cryptomonedas

# Compra-ventas y tradeo de Cryptomonedas

Programa hecho en lenguaje python. Tambien se ha usado Flask, Html5, CSS3 y Jinja.
Para recuperar el valor de las criptos hemos utilizado la API Coinapi.io

## Instalación 🔧

- Obtener la apikey en https://www.coinapi.io/ 
- Obtener una Scret Key en https://randomkeygen.com/ 
- Hacer una copia del fichero `config_template.py`:
    - En apikey  poner tu clave
    - En el SECRET_KEY poner tu Secret Key

```

```
   

```

```

- Renombrar al fichero copia como `config.py`
- Descargar la app DB Browser for SQLite
- En la carpeta data hay un fichero llamado create.sql que tiene la estructura para crear la tabla de la base de datos en DB Browser
- Hacer una copia del fichero `.env_template` y el FLASK_DEBUG poner True o False
- Renombrar la copia `.env_template` a el nombre `.env`


### Instalacion de dependencias

- Ejecutar `pip install -r requirements.txt``

- Por ultimo ejecutar:

```
flask run
```
- Si el servidor 5000 esta ocupado ejecutar entonces:
```
flask run -p 5001
```

