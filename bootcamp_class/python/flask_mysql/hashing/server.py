from flask import Flask, request, redirect, render_template, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector

import md5 # do this at the top of your file where you import modules

app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'user_dashboard')
# an example of running a query
# print mysql.query_db("SELECT * FROM friends")

@app.route('/')
def index():
  users_from_db = mysql.query_db('SELECT * FROM users')
  print "*" * 80
  print 'Here is the query:', users_from_db

  return render_template('index.html', users=users_from_db, title="User Dashboard")

@app.route('/users/create', methods=['POST'])
def create_user():
  
  username = request.form['username']
  email = request.form['email']
  password = md5.new(request.form['password']).hexdigest()

  query = "INSERT INTO users (username, email, password, created_at, updated_at) VALUES (:username, :email, :password, NOW(), NOW())"

  query_data = { 
    'username': username, 
    'email': email, 
    'password': password 
  }
  mysql.query_db(query, query_data)

  print "*" * 80
  print 'Here is the query:', users_from_db

  return redirect('/')

app.run(debug=True)