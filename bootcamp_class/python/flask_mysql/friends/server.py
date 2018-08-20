from flask import Flask, request, redirect, render_template, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector

app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'friendsdb')
# an example of running a query
# print mysql.query_db("SELECT * FROM friends")

@app.route('/')
def index():
  # an example of running a query
  # print mysql.query_db('SELECT * FROM friends')
  friends_from_db = mysql.query_db('SELECT * FROM friends')
  print "*" * 80
  print friends_from_db

  return render_template('index.html', friends=friends_from_db, title="Home")

@app.route('/friends', methods=['POST'])  #
def create():
  request.form['first_name']
  request.form['last_name']
  request.form['occupation']

  # Write query as a string. Notice how we have multiple values we want to insert into our query.
  query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
  # We'll then create a dictionary of data from the POST data received.
  data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'occupation': request.form['occupation']
  }
  # Run query, with dictionary values injected into the query.
  friends_update = mysql.query_db(query, data)

  print "*" * 80
  print friends_update
  mysql.query_db(query, data)

  return redirect('/')

@app.route('/friends/<friend_id>')
def show(friend_id):
  # Write query to select specific user by id. At every point where
  # we want to insert data, we write ":" and variable name.
  query = "SELECT * FROM friends WHERE id = :specific_friend_id"
  # Then define a dictionary with key that matches :variable_name in query.
  data = {
    'specific_friend_id': friend_id
  }
  # Run query with inserted data.
  friends_from_db = mysql.query_db(query, data)
  print "*" * 80
  print friends_from_db
  # Friends should be a list with a single object,
  # so we pass the value at [0] to our template under alias one_friend.
  return render_template('show.html', one_friend=friends_from_db[0], title="Show user")

@app.route('/friends/<friend_id>/edit')
def edit(friend_id):
  # Write query to select specific user by id. At every point where
  # we want to insert data, we write ":" and variable name.
  query = "SELECT * FROM friends WHERE id = :specific_friend_id"
  # Then define a dictionary with key that matches :variable_name in query.
  data = {
    'specific_friend_id': friend_id
  }
  # Run query with inserted data.
  friends_from_db = mysql.query_db(query, data)

  return render_template('edit.html', u_id=friend_id, one_friend=friends_from_db[0], title='Edit user')

@app.route('/friends/<friend_id>/update', methods=['POST'])
def update(friend_id):
  
  first_name = request.form['first_name']
  last_name = request.form['last_name']
  occupation = request.form['occupation']

  # Write query to select specific user by id and update that users information, including updated_at
  query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation, updated_at = NOW() WHERE id = :specific_friend_id"
  # We'll then create a dictionary of data from the POST data received.
  data = {
    'specific_friend_id': friend_id,
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'occupation': request.form['occupation']
  }
  # Run query, with dictionary values injected into the query.
  mysql.query_db(query, data)

  return redirect('/')

@app.route('/friends/<friend_id>/delete', methods=['GET'])
def delete(friend_id):

  # Write query to delete specific user by id. 
  query = "DELETE FROM friends WHERE id = :specific_friend_id"
  # We'll then create a dictionary of data from the POST data received.
  data = {
    'specific_friend_id': friend_id
  }
  # Run query, with dictionary values injected into the query.
  mysql.query_db(query, data)

  return redirect('/')

app.run(debug=True) 