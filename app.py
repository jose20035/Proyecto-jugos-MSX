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
        met=0
        respuesta=[]
        busq=request.form.get("busqueda")
        if busq = "":
            return render_template("juegos.html" met=met lista=juegos)
        else:
            for juego in juegos:
                if juegos.get("nombre").startswith(busq):
                    respuesta.append(juego)
            return render_template("juegos.html" met=met lista=respuesta)
            

port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=False)