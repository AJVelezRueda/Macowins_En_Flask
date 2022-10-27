from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/success/')
def success():
   return render_template('success.html')


@app.route('/prendas/new/', methods=('GET', 'POST'))
def create_prenda():
    if request.method == 'POST':
        valor_input = request.form.get("name").split(',')
        prendas[int(valor_input[0])] = {"name": valor_input[1], "price": valor_input[2]}
        return redirect(url_for('success'))
    else:
      return render_template('new_prendas.html')