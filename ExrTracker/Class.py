import pymongo

class Customer:

    def __init__(self, name, age=None, gender=None, height=None, weight=None, daysperweak=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight


class Workout:

    def __init__(self, level=None, time=None, caloriesburned=None, workoutday=None):
        self.level = level
        self.time = time
        self.caloriesburned = caloriesburned
        self.workoutday = workoutday


class CustomerDBHelper:

    def __init__(self):
        client = pymongo.MongoClient(
            "mongodb+srv://rajvir:rajvir@cluster0.191grik.mongodb.net/?retryWrites=true&w=majority")
        #Select the database in mongodb
        self.db = client['exetracker']
        #from the mongoDB Select the collection
        self.collection = self.db['Customer']



    def insert(self, document):
        result = self.collection.insert_one(document)
        print("Inserted Data:", result.inserted_id)

    def fetch(self):
        documents = self.collection.find()
        data =[]
        for document in documents:
            print(document, type(document))
            data.append(document)
        return data

    def fetch_selected(self, query):
        documents = self.collection.find(query)
        for document in documents:
            print(document)

    def delete(self, query):
        result = self.collection.delete_one(query)
        print(result.deleted_count)

    def update(self, document, query):
        update_query = {"$set": document}
        result = self.collection.update_one(query, update_query)
        print(result.modified_count)


class MongoDBHelper:

    def __init__(self):
        client = pymongo.MongoClient(
            "mongodb+srv://rajvir:rajvir@cluster0.191grik.mongodb.net/?retryWrites=true&w=majority")
        #Select the database in mongodb
        self.db = client['exetracker']
        #from the mongoDB Select the collection
        self.collection = self.db['Workout']


    def insert(self, document):
        result = self.collection.insert_one(document)
        print("Inserted Data:", result.inserted_id)

    def fetch(self):
        documents = self.collection.find()
        data =[]
        for document in documents:
            print(document, type(document))
            data.append(document)
        return data

    def fetch_selected(self, query):
        documents = self.collection.find(query)
        for document in documents:
            print(document)

    def delete(self, query):
        result = self.collection.delete_one(query)
        print(result.deleted_count)

    def update(self, document, query):
        update_query = {"$set": document}
        result = self.collection.update_one(query, update_query)
        print(result.modified_count)

def main():
    db_helper = MongoDBHelper()

    customer1 = Customer(name="lia", age="9999977777", gender="lia@example.com", height=22, weight="female")
    customer_dictionary = vars(customer1)
    print(customer_dictionary, type(customer_dictionary))
    db_helper.insert(document=customer_dictionary)

    workout1 = Workout(level="32", time=32, caloriesburned="3435", workoutday="wednesday" )
    workout_dictionary = vars(workout1)
    print(workout_dictionary, type(workout_dictionary))
    db_helper.insert(document=workout_dictionary)

if __name__ == "__main__":
    main()
