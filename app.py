import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_places")
def get_places():
    places = list(mongo.db.places.find())
    return render_template("places.html", places=places)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the users username from mongo
    username = mongo.db.users.find_one(
        {"username": session["user"]}) ["username"]
    return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_places", methods=["GET", "POST"])
def add_places():
    place = {
        "category_name": request.form.get("category_name"),
        "location": request.form.get("location"),
        "image_url": request.form.get("image_url"),
        "description": request.form.get("description"),
        "place_name": request.form.get("place_name"),
        "date": request.form.get("date"),
        "created_by": session["user"]
    }
    if request.method == "POST":
        mongo.db.places.insert_one(place)
        flash("Place Successfully Added")
        return redirect(url_for("get_places"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_places.html", categories=categories)


@app.route("/edit_place/<place_id>", methods=["GET", "POST"])
def edit_place(place_id):
    submit = {
        "category_name": request.form.get("category_name"),
        "location": request.form.get("location"),
        "image_url": request.form.get("image_url"),
        "description": request.form.get("description"),
        "place_name": request.form.get("place_name"),
        "date": request.form.get("date"),
        "created_by": session["user"]
    }
    if request.method == "POST":
        mongo.db.places.update({"_id": ObjectId(place_id)}, submit)
        flash("Place Successfully Updated")
    place = mongo.db.places.find_one({"_id": ObjectId(place_id)})    
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_place.html", place=place, categories=categories)


@app.route("/delete_place/<place_id>")
def delete_place(place_id):
    mongo.db.places.remove({"_id": ObjectId(place_id)})
    flash("Place Successfully Deleted")
    return redirect(url_for("get_places"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)