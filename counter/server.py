from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)
app.secret_key="counter"

@app.route('/')
def index():
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return render_template("index.html", count=session['count'])


@app.route('/addtwo')
def addtwo():
    session['count']+=1
    return redirect('/')

@app.route('/destroy')
def destroy():
    session['count']=0
    return redirect('/')


app.run(debug=True)