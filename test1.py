import pymongo

client = pymongo.MongoClient("mongodb+srv://root:ParzivalAshu13@cluster0.zwmochs.mongodb.net/?retryWrites=true&w=majority")
db = client.test

list_of_records = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},

    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},

    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'}
]

database = client["schoolinfo"]
collection = database["studentinfo"]
collection.insert_many(list_of_records)