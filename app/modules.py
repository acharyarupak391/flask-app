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
    
  def createBucket(self, name):
    d = datetime.now()
    name = name \
            #  + '-' + str(d.year) + str(d.month) + str(d.day)\
            #  + str(d.hour) + str(d.minute) + str(d.second) + str(d.microsecond)
    self.s3_client.create_bucket(Bucket=name)

  def upload_file_to_bucket(self, bucket_name, file, file_name):
    # file_id = self.add_single_document('user-images', {'user': file_name})
    file_id = "5f197c4d6ae7cdc6c2a89e1a"

    self.s3_client.put_object(ACL='private', Body=file, Bucket=bucket_name, 
                              Key=file_name+'.jpg', Metadata={'_id': str(file_id)},
                              ContentType=file.content_type)
