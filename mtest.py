import pymongo

client = pymongo.MongoClient("mongodb+srv://root:ParzivalAshu13@cluster0.zwmochs.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

data = {
    "name" : "student1",
    "email" : "student1@ineuron.ai",
    "subject" : ["physics","chemistry","math"]
}
database = client["schoolinfo"]
collection = database["studentinfo"]
collection.insert_one(data)