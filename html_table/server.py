from flask import Flask
from flask import render_template, request, redirect, session
from flask.templating import render_template_string
app = Flask(__name__)
app.secret_key = "html_table"


@app.route("/")
def index():
    users_list = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("index.html", user = users_list)


if __name__ == "__main__":
    app.run(debug=True)




