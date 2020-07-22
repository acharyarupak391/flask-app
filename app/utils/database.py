from pymongo import MongoClient

class DB():
  def __init__(self):
    self.connect();

  def connect(self):
    client = MongoClient("mongodb+srv://newdbuser:I9hXhBTUMSOpNCSl@flask-app-cluster.dtoxs.gcp.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    print('connected to db')
    return db