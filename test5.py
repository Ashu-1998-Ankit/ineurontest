import pymongo

client = pymongo.MongoClient("mongodb+srv://root:ParzivalAshu13@cluster0.zwmochs.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client["inventory"]
collection = database["table"]

#data = collection.find({"status" : "A"}) #Where satus = A
#data = collection.find({"status" : {"$in" : ["A","P"]}}) #Where status = A or P
for i in data:
    print(i)