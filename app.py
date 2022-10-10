from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

prendas = {
    100: {"name": "Remera talle m", "price": 50},
    150: {"name": "Remera talle s", "price": 40}
}

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/prendas/")
def get_all_prendas():
    return render_template("prendas.html", prendas=prendas.items())

@app.get("/prendas/<int:id>")
def get_prenda(id):
    if id in prendas:
        prenda = prendas[id]
        return render_template('prenda.html', id=id, prenda=prenda)
    else:
        return ("no hay prenda", 404)

@app.get("/ventas/<int:id>")
def get_venta(id):
    return {"foo":1}
