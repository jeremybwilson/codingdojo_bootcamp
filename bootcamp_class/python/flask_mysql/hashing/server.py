from flask import Flask, request, redirect, render_template, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector

import md5, os, binascii # do this at the top of your file where you import modules

app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'userdemodb')


@app.route('/')
def index():
  users_from_db = mysql.query_db('SELECT * FROM users')
  print "*" * 80
  print 'Here is the query:', users_from_db

  return render_template('index.html', users=users_from_db, title="User Dashboard")

@app.route('/users/create', methods=['POST'])
def create_user():

  name = request.form['name']
  email = request.form['email']
  password = request.form['password']
  errors = False

  salt = binascii.b2a_hex(os.urandom(15))
  hashed_pw = md5.new(password + salt).hexdigest()

  insert_query = "INSERT INTO users (name, email, password, salt, created_at, updated_at) VALUES (:name, :email, :hashed_pw, :salt, NOW(), NOW())"

  print "*" * 80
  print 'Here is the query:', insert_query

  query_data = { 
    'name': name, 
    'email': email, 
    'hashed_pw': hashed_pw,
    'salt': salt 
  }

  if len(request.form['name']) < 1:
    flash('Username must not be blank!')
    errors = True
  if len(request.form['email']) < 1:
    flash('Email address must not be blank!')
    errors = True

  if errors:
    # return to the login/registration page
    return redirect('/')
  else:
    # run the insert query to the database only if no validation errors
    mysql.query_db(insert_query, query_data)
    # return to the success page
    return redirect('/success')

@app.route('/login', methods=['POST'])
def login():

  # name =  request.form['name']
  email = request.form['email']
  password = request.form['password']
  errors = False

  user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
  query_data = {'email': email}
  user = mysql.query_db(user_query, query_data)

  if len(user) != 0:
    encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
    if user[0]['password'] == encrypted_password:
      # this means we have a successful login!
      print 'We have a successful login!'
      # success
    else:
      # invalid password!
      flash('Invalid password entered!')
      errors = True
    # else:
      # invalid email!

  if errors:
    # return to the login/registration page
    return redirect('/login')
  else:
    mysql.query_db(insert_query, query_data)
    return redirect('/')

@app.route('/users/<user_id>/edit')
def edit(user_id):
  # Write query to select specific user by id. At every point where
  # we want to insert data, we write ":" and variable name.
  query = "SELECT * FROM users WHERE id = :specific_user_id"
  # Then define a dictionary with key that matches :variable_name in query.
  data = {
    'specific_user_id': user_id
  }
  # Run query with inserted data.
  users_from_db = mysql.query_db(query, data)

  return render_template('edit.html', u_id=user_id, one_user=users_from_db[0], title="Edit user")

@app.route('/users/new')
def new():

  return render_template('new.html', title="Welcome New User")

app.run(debug=True)
