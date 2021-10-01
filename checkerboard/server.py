from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("home.html")


@app.route("/<x>/<y>")
def hov_vert(x, y):
    return render_template("index.html", x=int(x), y=int(y))


if __name__ == "__main__":
    app.run(debug=True) ##Remember to add the debug=True