from flask import Flask, request, render_template, redirect, session, url_for
import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017")
db = db_client["users"]
details_table = db["details"]

app = Flask(__name__)

app.secret_key = 'no secret key'

@app.route("/", methods=["GET","POST"])
def registration():
    if request.method=="POST":
        form_data = dict(request.form)
        user = form_data["username"]
        password = form_data["password"]
        email = form_data["email"]
        phone = form_data["phone"]

        details_table.insert_one({"username": user, "password": password, "email address": email, "phone": phone})

    return render_template("registration.html", **locals())


if __name__ == "__main__":
    app.run(debug=True)