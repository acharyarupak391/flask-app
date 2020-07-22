from app import app
from flask import render_template
from app.utils.database import DB
db = DB()

@app.errorhandler(404)
def error_handler(e):
  return "Oops! Seems like the page you're trying to get doesn't exist.", 404

@app.route('/')
def hello():
  return render_template('home.htm', data={'name': 'Rupak'})