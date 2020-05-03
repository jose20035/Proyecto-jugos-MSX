from flask import Flask, render_template,abort,request
import json
import os

with open('MSX.json') as file:
    juegos=json.load(file)

cate=[]
for juego in juegos:
    if juego.get("categoria") not in cate:
        cate.append(juego.get("categoria"))

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def inicio():
    if request.method=="GET":
        met=1
        return render_template("juegos.html",met=met,cate=cate)
    else:
        respuesta=[]
        busq=request.form.get("busqueda")
        if busq == "":
            return render_template("juegos.html",lista=juegos)
        else:
            for juego in juegos:
                if str(juego.get("nombre")).startswith(busq):
                    respuesta.append(juego)
            return render_template("juegos.html",lista=respuesta)
            

port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=True)