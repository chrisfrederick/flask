from flask import Flask
from flask import render_template, request, redirect, session
from flask.templating import render_template_string
app = Flask(__name__)
app.secret_key = "pixarMovie"

@app.route("/")
def index():
    if("voters" not in session):
        session["voters"] = []

    if "votes" not in session:
        session["votes"] = {"total": 0, "Toy Story": 0, "Luca": 0, "Finding Nemo": 0}
    return render_template("index.html")

@app.route("/vote", methods=["POST"])
def vote():
    temp_user = {
        "name": request.form["name"],
        "age": request.form["age"],
        "movie": request.form["movie"]
    }
    session["voters"].append(temp_user)

    session["votes"]["total"] += 1
    session["votes"][temp_user["movie"]] += 1
    session.modified = True
    return redirect("/results")

@app.route("/results")
def results():
    return render_template("results.html", voters = session["voters"])

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)