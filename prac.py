from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USER_CREDENTIALS = {"user": "123"}  # user database

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            return redirect(url_for("home"))

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html", error=None)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/flask-info")
def flask_info():
    return render_template("flask_info.html")

@app.route("/python-info")
def python_info():
    return render_template("python_info.html")

if __name__ == "__main__":
    app.run(debug=True)
