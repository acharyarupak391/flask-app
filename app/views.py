from app import app
from flask import render_template
from flask import request
from flask import Response
from app.modules import DB
import json

db = DB()

@app.errorhandler(404)
def error_handler(e):
  return "Oops! Seems like the page you're trying to get doesn't exist.", 404

@app.errorhandler(500)
def error_handler(e):
  return "Oops! Seems like there is some error in the server. Sorry for the inconvenience", 500

@app.route('/')
def hello():
  client_ip = request.remote_addr;
  # db.add_ip('users', client_ip)
  return render_template('home.htm', data={'name': 'Flask-app'})

@app.route('/upload', methods=["POST"])
def file_handle():
  if(request.files and request.form):
    image = request.files['image-file']
    user_name = request.form['user-name']
    image.seek(0, 2)
    size = image.tell()
    image.seek(0)
    if(size/1024/1024 > 5): return json.dumps({'error': 'File too large (Max File Size is 5 MB)'})
    if(image.content_type.split('/')[0] != 'image'): return json.dumps({'error': 'Only image files accepted'})
    db.upload_file_to_bucket('mynewbucket391', image, user_name)
    # body = db.get_file_object(bucket_name='mynewbucket391', file_key=(user_name+'.jpg'))


  return json.dumps({'msg': 'Image received successfully!'})
  # return Response(response=body, content_type=image.content_type)