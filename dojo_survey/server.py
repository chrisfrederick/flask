from flask import Flask , render_template, request, redirect

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("User Created")

    return redirect('/')

@app.route ('/result', methods=['POST'])
def result():
    name=request.form['name']
    language= request.form['language']
    location=request.form['location']
    comment=request.form['comment']
    return render_template("result.html", language=language, location=location, name=name, comment=comment)


app.run(debug=True)