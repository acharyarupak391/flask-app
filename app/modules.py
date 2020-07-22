from app.utils.database import connect

class DB():
  def __init__(self):
    self.db = connect('flask');

  def add_single_document(self, collection_name, data):
    coll = self.db[collection_name];
    coll.insert_one(data)
  
  def add_ip(self, collection_name, ip):
    coll = self.db[collection_name];
    if(coll.count_documents({'ip': ip}, limit = 1) == 0):
      data = {'ip': ip, 'count': 1}
      self.add_single_document('users', data)
    else:
      # coll.find_one({'ip': ip})
      coll.update_one({'ip': ip}, {"$inc": {"count": 1}})
