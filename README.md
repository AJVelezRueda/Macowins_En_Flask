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

1. Creá un archivo `main.py`
2. Importá Flask e instanciá un objeto `app` de la clase `Flask`, que será nuestra forma de comunicarnos con el _framework_:

```python
from flask import Flask

app = Flask(__name__)
```

> Nota: si necesitás repasar conceptos como objetos y clases, podés hacerlo [acá](https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/POO/Teoria/Introducci%C3%B3n_a_POO.md) 

## Definición de las rutas

Nuestra aplicación Flask se compondrá de una o más rutas que expondrán los distintos recursos de nuestro sistema. Cada ruta nos dice, como mínimo dos cosas: 

1. Bajo qué URL se expondrá el recurso
2. Qué se responderá cuando se lo acceda


Explicando los metodos HTTP
Mostrando que se pueden devolver cosas diferentes
    Mostrando en particular
        HTML
        JSON (e introduciendo la idea de API vs App Web)
        Otros formatos (ejemplo CSV)
Un ejemplo un poco mas completo con todo (y un diccionario en memoria, y/o una generaciòn de un CSV a partir de un DF) 



