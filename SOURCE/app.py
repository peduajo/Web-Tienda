# encoding: utf-8
from flask import Flask,render_template,request,redirect,url_for
import os
import io


app = Flask(__name__)


@app.route('/tienda')
def tienda():
	return render_template('tienda.html')

@app.route('/noticias')
def noticias():
	return render_template('noticias.html')

@app.route('/sobre_nosotros')
def sobre_nosotros():
    return render_template('sobreNosotros.html')

@app.route('/contacto')
def contacto():
    return render_template('ubicacion.html')


if __name__=="__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)