from pymongo import MongoClient

#Connecting to mongoDB
try:
    client = MongoClient('localhost',27017)
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = client.AI_assets
collection = db.train_anomaly
cursor = collection.distinct("user")
#print(type(cursor))
for record in cursor:
    print(record)