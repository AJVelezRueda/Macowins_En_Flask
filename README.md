# Macowins en Flask

> Flask es un micro framework web, que nos permite la construcción de APIs y aplicaciones REST.  

## Instalación

1. Creá un proyecto nuevo: `mkdir Macowins_En_Flask && cd Macowins_En_Flask`
2. Iniciá un entorno virtual usando conda o venv:
    a. `conda create env --name Macowins_En_Flask` 
    b. `python3 -m venv venv`
3. Activá el entorno correspondiente:
    a. `conda activate Macowins_En_Flask`
    b. `. venv/bin/activate`
4. Instalar el paquete [`Flask`](https://flask.palletsprojects.com/en/2.2.x/): `pip install Flask`


## Creación del archivo de rutas

1. Creá un archivo `app.py`
2. Importá Flask e instanciá un objeto `app` de la clase `Flask`, que será nuestra forma de comunicarnos con el _framework_:

```python
from flask import Flask

app = Flask(__name__)
```

> Nota: si necesitás repasar conceptos como objetos y clases, podés hacerlo [acá](https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/POO/Teoria/Introducci%C3%B3n_a_POO.md) 

## Definición básica de las rutas

Nuestra aplicación Flask se compondrá de una o más rutas que expondrán los distintos recursos de nuestro sistema. Cada ruta nos dice, como mínimo dos cosas: 

1. Bajo qué URL se expondrá el recurso
2. Qué se responderá cuando se lo acceda

Para crear una ruta, deberemos definir una función que se encargará de responder a un pedido HTTP (2)...

```python
def home():
    return "<p>Te damos la bienvenida a MacoWins</p>"
```

...y la decoraremos con el decorador `@app.get` para inidicar a qué pedidos responderá (1):


```python
@app.get("/")
def home():
    return "<p>Te damos la bienvenida a MacoWins</p>"
```

En nuestro ejemplo, estamos indicándole al servidor que responda a los pedidos GET en / con el contenido HTML `"<p>Te damos la bienvenida ..."`.


## Inicio de la aplicación

Para iniciar el servidor en nuestra computadora local, se debe utilizar el comando `flask run`: 

```bash
$ flask --debug run
# si el nombre de archivo fuera diferente
# reeemplazar con el mismo sin la extensión .py
$ flask --app <nombre_de_archivo> --debug run
```

Este comando ejecutará nuestro archivo de rutas y comenzará a escuchar nuestros pedidos HTTP en el puerto `5000`:


...TODO agregar captura de pantalla del navegador... 

Además, el flag `--debug` permitirá que los cambios a nuestro código se reflejen automáticamente.   


## Rutas más avanzadas

Las rutas pueden estar parametrizadas. Por ejemplo, si queremos que nuestro servidor liste todas las prendas bajo `/prendas` y muestre una prenda específica bajo rutas como `/prendas/13`, podremos escribir lo siguiente:


```python
from markupsafe import escape

@app.get("/prendas/")
def get_all_prendas():
    return f"<p>Mostrando todas las prendas</p>"

@app.get("/prendas/<id>")
# id es un parámetro de tipo string que será enviado como parte de la ruta
def get_prenda(id):
    # es importante que escapemos todo elemento provisto externamente
    # que vaya a ser incluido en nuestro HTML resultante. De lo contrario
    # estaríamos dejando nuestra aplicación vulnerable a ataques de inyección HTML
    # https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/03-Testing_for_HTML_Injection
    return f"<p>Mostrando la prenda {escape(id)}</p>"
```

Además, si queremos que los parámetros sean automáticamente validados y convertidos a un tipo de dato particular, podremos indicarlo de la siguiente forma: 

```python
@app.get("/prendas/<int:id>")
def get_prenda(id):
    return f"<p>Mostrando la prenda {escape(id)}</p>"
```

Ahora, nuestro `id` deberá ser un entero, y lo recibiremos como tal. 

Mostrando que se pueden devolver cosas diferentes
    Mostrando en particular
        HTML
        JSON (e introduciendo la idea de API vs App Web)
        Otros formatos (ejemplo CSV)
Un ejemplo un poco mas completo con todo (y un diccionario en memoria, y/o una generaciòn de un CSV a partir de un DF) 



