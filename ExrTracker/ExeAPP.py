from flask import *
from Class import Customer, Workout
from Class import MongoDBHelper
from Class import CustomerDBHelper


app = Flask("ExerciseTracker", template_folder="./../abc")
customerdb_helper = CustomerDBHelper()
mongodb_helper = MongoDBHelper()

@app.route("/")
def main():
    return render_template("head.html")

@app.route("/addCustomer")
def add():
    return render_template("Add-customer.html")

@app.route("/addWorkout")
def addWorkout():
    return render_template("Add-workout.html")

@app.route("/view")
def view():
    #coll = mongodb_helper()
    #coll = mongodb_helper.fetch()
    #mongo = coll.fetch()
    customer = customerdb_helper.fetch()
    rows = mongodb_helper.fetch()
    print(customer)
    # newRow = []
    # workout = []
    # for i in rows:
    #     if 'name' in i.keys():
    #         newRow.append(i)
    #
    # for i in rows:
    #     if 'level' in i.keys():
    #         workout.append(i)

    return render_template("view-details.html", result=customer, workout=rows)


@app.route("/save-customer", methods=["POST"])
def save_customer_in_db():
    # (request.form)get data when submitting a form with the POST method

    cref = Customer(name=request.form.get("name"),
                    age=request.form.get("age"),
                    gender=request.form.get("gender"),
                    height=request.form.get("height"),
                    weight=request.form.get("weight"))

    print(vars(cref))
    customer_to_save = vars(cref)
    customerdb_helper.insert(document=customer_to_save)
    return render_template("save.html", message=cref.name+" Inserted Successfully")

@app.route("/save-workout", methods=["POST"])
def save_workout_in_db():
    # (request.form)get data when submitting a form with the POST method

    cref = Workout(level=request.form.get("level"),
                    time=request.form.get("time"),
                    caloriesburned=request.form.get("caloriesburned"),
                    workoutday=request.form.get("workoutday"))


    print(vars(cref))
    customer_to_save = vars(cref)
    mongodb_helper.insert(document=customer_to_save)
    return render_template("save.html", message=" Inserted Successfully")


def main():
    app.run()

if __name__ == "__main__":
    main()
