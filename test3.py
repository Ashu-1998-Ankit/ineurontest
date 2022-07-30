import pymongo

client = pymongo.MongoClient("mongodb+srv://root:ParzivalAshu13@cluster0.zwmochs.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client["schoolinfo"]
collection = database["studentinfo"]

# records = collection.find()
# for i in records:
#     print(i)

# data = collection.find({"companyName" : "iNeuron"})
data = collection.find({"courseOffered" : {"$gt" : "E"}})
for i in data:
    print(i)