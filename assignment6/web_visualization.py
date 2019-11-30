from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/handle_login', methods=['POST'])
def handle_login():

    assert request.method == 'POST'   # Check that we are really in a POST request

    # Acces the form data:
    username = request.form["username"]
    password = request.form["password"]

    if username == "simon" and password == "safe":
        return "You are logged in Simon"
    else:
        error = "Invalid credentials"
        return render_template("login.html", error=error)

if __name__ == "main":
    app.run()
