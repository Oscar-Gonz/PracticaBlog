from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def url_principal():
	return render_template("template.html" , nombre = "Oscar González")

if __name__ == "__main__":
	app.run(debug = True)
