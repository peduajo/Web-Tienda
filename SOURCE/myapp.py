from flask import Flask,render_template, make_response

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

@app.route('/sitemap.xml')
def sitemap():
    template = render_template('sitemap.xml')
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'
    return response

if __name__=="__main__":
    app.run(threaded=True)
