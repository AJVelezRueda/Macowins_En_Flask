from flask import Flask, render_template
from markupsafe import escape
import pandas as pd

app = Flask(__name__)

prendas = pd.DataFrame({
    100: {"name": "Remera talle m", "price": 50},
    150: {"name": "Remera talle s", "price": 40}
})

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/prendas/")
def get_all_prendas():
    return f"<p>Mostrando prendas {prendas.to_html()}</p>"
