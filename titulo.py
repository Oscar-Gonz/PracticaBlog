from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def url_principal():
	return render_template("template.html" , nombre = "Oscar González")

@app.route("/estudios")
def url_estudios():
 	tipos = [
 		"Americano",
 		"Latte"
 	]
 	return render_template("menu.html", tipos=tipos, nombre="Oscar González")

@app.route("/deporte")
def url_deporte():
 	tipos = [
 		"Americano",
 		"Latte"
 	]
 	return render_template("deporte.html", tipos=tipos, nombre="Oscar González")

@app.route("/ocio")
def url_ocio():
 	tipos = [
 		"Americano",
 		"Latte"
 	]
 	return render_template("ocio.html", tipos=tipos, nombre="Oscar González")

@app.route("/regresar")
def url_regresar():
 	tipos = [
 		"Americano",
 		"Latte"
 	]
 	return render_template("template.html", tipos=tipos, nombre="Oscar González")

if __name__ == "__main__":
	app.run(debug = True)
