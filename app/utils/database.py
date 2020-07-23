from pymongo import MongoClient
import boto3
from secrets import mongo_user, mongo_pass, aws_access_key_id, aws_secret_access_key, aws_session_token

def connect_mongo(db_name='flask'):
  mongo_string = "mongodb+srv://"+mongo_user+":"+mongo_pass+"@flask-app-cluster.dtoxs.gcp.mongodb.net/?retryWrites=true&w=majority"
  client = MongoClient(mongo_string)
  db = client[db_name]
  print('connected to database: ', db_name)
  return db

def connect_s3(service):
  sess = boto3.Session(aws_access_key_id, aws_secret_access_key, aws_session_token)
  print('connected to aws s3')
  return sess.client(service)

def get_s3_resource(service):
  sess = boto3.Session(aws_access_key_id, aws_secret_access_key, aws_session_token)
  return sess.resource('s3')