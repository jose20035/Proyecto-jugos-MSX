from flask import Flask, render_template,abort
import json
import os

with open('MSX.json') as file:
    libros=json.load(file)

app = Flask(__name__)

@app.route('/juegos', methods=["GET","POST"])
def inicio():
    return render_template("Inicio.html",datos=libros,categoria=categoria)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=False)