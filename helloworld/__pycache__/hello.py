from flask import Flask , render_template , url_for
app = Flask(__name__)

@app.route("/")
def hello():
	return "<h1>HOME PAGE</h1>"


@app.route("/about")
def about():
	return "<h1>ABOUT PAGE</h1>"

if __name__ == "__main__":
	app.run(debug=True)
			