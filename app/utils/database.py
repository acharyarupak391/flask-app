from pymongo import MongoClient
from secrets import mongo_user, mongo_pass

def connect(db_name='flask'):
  mongo_string = "mongodb+srv://"+mongo_user+":"+mongo_pass+"@flask-app-cluster.dtoxs.gcp.mongodb.net/?retryWrites=true&w=majority"
  client = MongoClient()
  db = client[db_name]
  print('connected to database: ', db_name)
  return db