import os
from flask import (Flask, flash, render_template, redirect, request, session, url_for)
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
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exits
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user in 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration sucessful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exits
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        if existing_user:
            # check if hashed password matches user input
            if check_password_hash(existing_user["password"], 
            request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))

            else:
                # invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for('login'))

        else:
            # username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one({"username": session["user"]})["username"]

    if session['user']:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))
   

@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "catagory_name": request.form.get("catagory_name"),
            "recipe_name": request.form.get("recipe_name"),
            "ingredients": request.form.get("ingredients"),
            "recipe_description": request.form.get("recipe_description"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Succesfully Added")
        return redirect(url_for("get_recipes"))

    catagories = mongo.db.catagories.find().sort("catagory_name", 1)
    return render_template("add_recipe.html", catagories=catagories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    
    if request.method == "POST":
        submit = {
            "catagory_name": request.form.get("catagory_name"),
            "recipe_name": request.form.get("recipe_name"),
            "ingredients": request.form.get("ingredients"),
            "recipe_description": request.form.get("recipe_description"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Succesfully Updated")
       

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    catagories = mongo.db.catagories.find().sort("catagory_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, catagories=catagories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/get_catagories")
def get_catagories():
    catagories = list(mongo.db.catagories.find().sort("catagory_name", 1))
    return render_template("catagories.html", catagories=catagories)


@app.route("/add_catagory", methods= ["GET", "POST"])
def add_catagory():
    if request.method == "POST":
        catagory = {
            "catagory_name": request.form.get("catagory_name")
        }
        mongo.db.catagories.insert_one(catagory)
        flash("New Catagory successfully added")
        return redirect(url_for("get_catagories"))

    return render_template("add_catagory.html")


@app.route("/edit_catagory/<catagory_id>", methods=["GET", "POST"])
def edit_catagory(catagory_id):
    if request.method == "POST":
        submit = {
            "catagory_name": request.form.get("catagory_name")
        }
        mongo.db.catagories.update({"_id": ObjectId(catagory_id)}, submit)
        flash("Catagory Successfully Updated")
        return redirect(url_for("get_catagories"))
    catagory = mongo.db.catagories.find_one({"_id": ObjectId(catagory_id)})
    return render_template("edit_catagory.html", catagory=catagory)


@app.route("/delete_catagory/<catagory_id>")
def delete_catagory(catagory_id):
    mongo.db.catagories.remove({"_id": ObjectId(catagory_id)})
    flash("Catagory Successfully Deleted")
    return redirect(url_for("get_catagories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)