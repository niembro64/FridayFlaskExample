from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

# never render on a post
@app.route('/users', methods=['POST'])
def user_post():
    return redirect("/afterPost")

@app.route('/afterPost')
def from_post():
    return render_template("second.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)