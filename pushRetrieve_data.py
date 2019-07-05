import csv
from pymongo import MongoClient

filename = 'C://Program Files//MongoDB//Server//4.0//bin//nginx_devplatformv1.4_filter_copy.csv'

#Opening file
with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    #Connecting to mongoDB
    try:
        client=MongoClient('localhost',27017)
        print("Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")

    #Creating database and collection
    db = client.AI_assets
    db.train_anomaly

    #Defining header
    header = ["ip", "geoip_region_name", "user_name", "time"]

    #Iterating data
    for each in reader:
        row={}
        for field in header:
            row[field]=each[field]

        #Insering and Updating
        db.train_anomaly.insert_one(row)
        db.train_anomaly.update_many({}, {'$currentDate': {'insert_datetime': {'$type': 'date'}}}, upsert=True)
        db.train_anomaly.update_many({},{'$rename':{'user_name':'user','ip':'ip_address','geoip_region_name':'ip_region','time':'login_time'}})