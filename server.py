from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "Could be whatever I want. Really."

@app.route('/')
def root():
    return render_template("index.html")

# never render on a post
@app.route('/users', methods=['POST'])
def user_post():
    print("You just hit submit")
    
    
    print(request.form['name'])
    print(request.form['email'])


    # add form data into session
    session['name'] = request.form['name']
    session['email'] = request.form['email']

    print(session['name'])
    print(session['email'])

    return redirect("/afterPost")

@app.route('/afterPost')
def from_post():
    print("Hitting new route after post")
    return render_template("second.html", n = session['name'], e = session['email'])


if __name__ == "__main__":
    app.run(debug=True, port=5001)