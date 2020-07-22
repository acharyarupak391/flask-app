from app import app
from flask import render_template
from flask import request
from app.modules import DB

db = DB()

@app.errorhandler(404)
def error_handler(e):
  return "Oops! Seems like the page you're trying to get doesn't exist.", 404

@app.errorhandler(500)
def error_handler(e):
  return "Oops! Seems like there is some error in the server. Sorry for the inconvenience", 500

@app.route('/')
def hello():
  # data = {}
  # db.add_document('users', data)
  client_ip = request.remote_addr;
  db.add_ip('users', client_ip)
  return render_template('home.htm', data={'name': 'Rupak'})