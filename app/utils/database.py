from pymongo import MongoClient

def connect(db_name='flask'):
  client = MongoClient("mongodb+srv://newdbuser:I9hXhBTUMSOpNCSl@flask-app-cluster.dtoxs.gcp.mongodb.net/?retryWrites=true&w=majority")
  db = client[db_name]
  print('connected to database: ', db_name)
  return db