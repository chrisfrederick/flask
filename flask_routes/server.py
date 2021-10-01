from flask import Flask, render_template ##need to set up a folder in project called templates for all .html files
import facts
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")


@app.route("/monsters/<monster>") ##takes a variable as the function argument -- monster
def monster_page(monster): ##injects the route argument into the parameter
    if monster == 'dracula':
        return render_template("monster.html", monster_name =monster.capitalize(), facts = facts.dracula)
    elif monster == 'frankenstein':
        return render_template("monster.html", monster_name =monster.capitalize(), facts = facts.frankenstein)
    elif monster == 'mummy':
        return render_template("monster.html", monster_name =monster.capitalize(), facts = facts.mummy)    
##keep this if method at the bottom of the file
##run in cmd python server.py to start the server && ctl-c to quit
if __name__ == "__main__":
    app.run(debug=True) ##Remember to add the debug=True