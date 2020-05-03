from flask import Flask, render_template,abort,request
import json
import os

with open('MSX.json') as file:
    juegos=json.load(file)

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def inicio():
    if request.method=="GET":
        met=1
        return render_template("juegos.html" met=met)
    else:
        busq=request.form.get("busqueda")
        for 

port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=False)