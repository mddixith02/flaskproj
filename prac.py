from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Secret key for session security
app.secret_key = "your_secret_key"

# Hardcoded user credentials
users = {"user": "123"}  # Username: "user", Password: "123"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["user"] = username  # Store user in session
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Credentials, try again!"

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", username=session["user"])
    return redirect(url_for("login"))

@app.route("/flask_info")
def flask_info():
    if "user" in session:
        return render_template("flask_info.html")
    return redirect(url_for("login"))

@app.route("/python_info")
def python_info():
    if "user" in session:
        return render_template("python_info.html")
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.clear()  # Completely remove all session data
    return redirect(url_for("login"))

# Prevent browser from caching logged-in pages
@app.after_request
def prevent_back(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response 

if __name__ == "__main__":
    app.run(debug=True)

