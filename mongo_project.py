import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "recipe_book"
COLLECTION = "recipes"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option


def add_record():
    print("")
    catagory_name = input("Enter the catagory name > ")
    recipe_name = input("Enter the name of the recipe > ")

    try:
        doc = coll.find_one({"catagory_name": catagory_name.lower(), "recipe_name": recipe_name.lower()})


def add_record():
    print("")
    catagory_name = input("Enter the catagory name > ")
    recipe_name = input("Enter the name of the recipe > ")
    ingredients = input("Enter the list of ingredients > ")
    recipe_description = input("Enter the recipe > ")

    new_doc = {
        "catagory_name": catagory_name.lower(),
        "recipe_name": recipe_name.lower(),
        "ingredients": ingredients.lower(),
        "recipe_description": recipe_description.lower()
    }

    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()
