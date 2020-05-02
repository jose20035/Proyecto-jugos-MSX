from flask import Flask, render_template,abort
import json
import os

with open('books.json') as file:
    libros=json.load(file)

app = Flask(__name__)

@app.route('/categoria/<categoria>')
@app.route('/')
def inicio(categoria=" "):
    return render_template("Inicio.html",datos=libros,categoria=categoria)

@app.route('/libro/<isbn>')
def detail(isbn):
    for libro in libros:
        if isbn == libro.get("isbn"):
            return render_template("Detail.html",libro=libro)
    abort(404)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=False)