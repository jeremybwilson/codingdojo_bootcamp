from flask import Flask, request, redirect, render_template, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
# the "re" module will let us perform some regular expression operations
# use md5 for password hashing before sending to the database
import re, md5, os, binascii
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'bobdobalina'

# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'login_registration')

@app.route('/')
def index():
  # an example of running a query
  # print mysql.query_db('SELECT * FROM friends')
  query = 'SELECT * FROM users'
  users_from_db = mysql.query_db(query)

  return render_template('index.html', users=users_from_db, title="Login and Registration")


@app.route('/<user_id>/edit', methods=['POST'])
def edit(user_id):

  query = 'SELECT * FROM users WHERE id = :user_id'

  data = {
    'user_id': user_id
  }
  users_from_db = mysql.query_db(query, data)
  print users_from_db

  # variable to shorten all request.form references to just 'form'
  form = request.form
  # create an empty list to store errors/successes
  errors = []
  successes = []
  form['first_name']
  form['last_name']
  form['email']
  form['password']
  form['confirm_password']

  return render_template('edit.html', u_id=user_id, user=users_from_db[0])

@app.route('/create', methods=['POST'])
def create():
  print "*" * 80
  print request.form
  print "*" * 80

  # variable to shorten all request.form references to just 'form'
  form = request.form
  first_name = form['first_name']
  last_name = form['last_name']
  email = form['email']
  password = form['password']
  confirm_password = form['confirm_password']

  # create an empty list to store errors/successes
  errors = []
  successes = []
  # validation TTD:
  # no blank fields
  # validate email
  # password is lat least 8 chars
  # password must contain at least one number
  # password and confirm_password must match

  if len(first_name) < 1:
    errors.append('First name must not be blank.')
  if len(first_name) < 3:
    errors.append('First name must be at least 3 characters.')
    # errors = True
  if len(last_name) < 1:
    errors.append('Last name must not be blank.')
  if len(last_name) < 3:
    errors.append('Last name must be at least 3 characters.')
  if len(email) < 1:
    errors.append('Email must not be blank.')
  if not EMAIL_REGEX.match(email):
    errors.append('You must enter a valid email address!')
  # else:
  #   successes.append('Success')

  if len(password) < 1:
    errors.append('Password must be not be blank.')
  if len(password) < 1:
    errors.append('Confirm password must not be blank.')
  # if len(form['password']) < 8:
  #   errors.append('Password must be at least 8 characters.')
  # if len(form['confirm_password']) < 8:
  #   errors.append('Confirm password must be at least 8 characters.')
  if password != confirm_password:
    errors.append('Passwords must match!')

  # check to see if user email exists in the db
  exists_query = 'SELECT email FROM users WHERE email = :email'
  exists_data = {
    'email': email
  }
  users_list = mysql.query_db(exists_query, exists_data)

  print "*" * 80
  print "Here is a matching list of users: ", users_list
  print "*" * 80

  if len(users_list) > 0:
    errors.append('Email already exists, choose another.')

  if len(errors) > 0:
    for error in errors:
      flash(error)
    return redirect('/new')
  # if all error validations cleared, then success
  else:
    for success in successes:
      flash(success)
  # create salt and combine with input value (password)
    salt = binascii.b2a_hex(os.urandom(15))
    hashed_password = md5.new(password + salt).hexdigest()

    print "Here is the hashed password: ", hashed_password, '\n'

    insert_query = 'INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, :salt, NOW(), NOW())'

    print "Here is the insert query: ", insert_query, '\n'

    data = {
      'first_name': first_name,
      'last_name': last_name,
      'email': email,
      'salt': salt,
      'pw_hash': hashed_password
    }

    user_id = mysql.query_db(insert_query, data)
    print 'returned from query', user_id
    session['user_id'] = user_id

    return redirect('/')

# login route
@app.route('/login', methods=['POST'])
def login():

  # create an empty list to store errors/successes
  errors = []
  successes = []
  # capture email and password values
  form = request.form
  email = form['email']
  password = form['password']

  # define query to validate email and password exist in database
  query = 'SELECT * FROM users WHERE email = :email'

  data = {
    'email': email
  }

  users_list = mysql.query_db(query, data)
  print "*" * 80
  print "User list result from db: ", users_list[0]

  # if we find a user with this email address, try to check the password
  if len(users_list) > 0:
    user = users_list[0]

  # create salt and combine with input value (password)
  salt = binascii.b2a_hex(os.urandom(15))
  hashed_input = md5.new(password + salt).hexdigest()

  print "*" * 80
  print "User password entered: ", hashed_input, '\n'
  print "User password from db: ", user['password']

  # pw_from_database = hashed_db_password # => password column + salt column
  if hashed_input != user['password']:
    errors.append('Invalid username or password')

  else:
    session['user_id'] = user['id']
    return redirect('/')

  if len(errors) > 0:
    for error in errors:
      flash(error)
    return redirect('/new')
  # if all error validations cleared, then success
  else:
    for success in successes:
      flash(success)
    return redirect('/')

  errors.append('Invalid username or password')
  return redirect('/new')


# logout route
@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')


# register new user route
@app.route('/new')
def new():

  return render_template('new.html', title="Create user")


@app.route('/<user_id>/delete', methods=['POST'])
def delete(user_id):
  # delete query for specific user_id passed with results
  delete_query = "DELETE FROM users WHERE id = :specific_user_id"

  # define user_id with dictionary
  data = {
    'specific_user_id': user_id
  }
  # execute query to delete data by user_id
  mysql.query_db(delete_query, data)

  return redirect('/')

app.run(debug=True) 