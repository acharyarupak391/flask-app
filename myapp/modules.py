from app.utils.database import connect_mongo, connect_s3
from datetime import datetime

class DB():
  def __init__(self):
    self.db = connect_mongo('flask');
    self.s3_client = connect_s3('s3')
    

  def add_single_document(self, collection_name, data):
    coll = self.db[collection_name];
    inserted = coll.insert_one(data)
    return inserted.inserted_id
  
  def add_ip(self, collection_name, ip):
    coll = self.db[collection_name];
    if(coll.count_documents({'ip': ip}, limit = 1) == 0):
      data = {'ip': ip, 'count': 1}
      self.add_single_document('users', data)
    else:
      # coll.find_one({'ip': ip})
      coll.update_one({'ip': ip}, {"$inc": {"count": 1}})

  def upload_file_to_bucket(self, bucket_name, file, file_name):
    # file_id = self.add_single_document('user-images', {'user': file_name})
    file_id = 1231434
    if(self.s3_client.head_bucket(Bucket=bucket_name)['ResponseMetadata']['HTTPStatusCode'] != 200):
      self.s3_client.create_bucket(Bucket=bucket_name)
    self.s3_client.put_object(ACL='public-read', Body=file, Bucket=bucket_name, 
                              Key=file_name+'.jpg', 
                              Metadata={'_id': str(file_id)},
                              ContentType=file.content_type)

  def get_file_object(self, bucket_name, file_key):
    return self.s3_client.get_object(Bucket=bucket_name, Key=file_key)['Body']
