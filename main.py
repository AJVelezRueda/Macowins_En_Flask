from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Te damos la bienvenida a Macowins</p>"