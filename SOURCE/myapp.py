from flask import Flask,render_template
import os

app = Flask(__name__)

@app.route('/')
def tienda():
	return render_template('tienda.html')

@app.route('/sobre_nosotros')
def sobre_nosotros():
    return render_template('sobreNosotros.html')

@app.route('/contacto')
def contacto():
    return render_template('ubicacion.html')

if __name__=="__main__":
    app.run(threaded=True)
