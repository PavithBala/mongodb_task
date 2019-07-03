import csv
from pymongo import MongoClient

#Reading csv file
csvfile = open('C:\\Program Files\\MongoDB\Server\\4.0\\bin\\nginx_devplatformv1.4_filter_copy.csv', 'r')
reader = csv.DictReader(csvfile)

#Connecting mongodb
client = MongoClient('localhost',27017)
try:                                                
      conn = MongoClient()                            
      print("Connected successfully!!!")              
except:                                             
      print("Could not connect to MongoDB") 

#Creating database and collection
database = client.newtraindb
database.train_anomaly.drop()

#Defining header
header= ["ip","geoip_region_name","user_name","time"]

#Iterating data
for each in reader:
    row={}         #Initailizing empty dict
    for data in header:
        row[data]=each[data]

#Inserting and Updating to mongodb
    database.train_anomaly.insert_one(row)
    database.train_anomaly.update_many({},{'$currentDate': {'insert_datetime': { '$type': 'date' }}},upsert=True)
    database.train_anomaly.update_many({},{'$rename':{'user_name':'user','ip':'ip_address','geoip_region_name':'ip_region','time':'login_time'}})


#$CurrentDate :   Sets the value of field to current date.
#$rename      :   Renames the mentioned field  name.
#upsert       :   Creates new  document when no document matches query criteria.
#DictReader   :   Maps the csv file data as key-value pairs (read like a dictionary).


