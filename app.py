from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.get("/")
def home():
    return "<p>Te damos la bienvenida a MacoWins</p>"

@app.get("/prendas/")
def get_all_prendas():
    return f"<p>Mostrando todas las prendas</p>"

@app.get("/prendas/<int:id>")
def get_prenda(id):
    return f"<p>Mostrando la prenda {escape(id)}</p>"
