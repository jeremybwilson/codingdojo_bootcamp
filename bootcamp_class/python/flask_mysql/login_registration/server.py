#################
#### imports ####
#################

from flask import Flask, request, redirect, render_template, session, flash
## import the Connector function
from mysqlconnection import MySQLConnector
## the "re" module will let us perform some regular expression operations
import re 
## use md5 for password hashing before sending to the database
# import md5, os, binascii
## use bcrypt instead of md5
from flask_bcrypt import Bcrypt

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'bobdobalina'

# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'login_registration')
flask_bcrypt = Bcrypt(app)

@app.route('/')
def index():
  # an example of running a query
  # print mysql.query_db('SELECT * FROM friends')
  query = 'SELECT * FROM users'

  users_from_db = mysql.query_db(query)

  if not 'login_status' in session:
    session['login_status'] = False

  if not 'user_id' in session:
    u_id = 'No id available!'
  else:
    u_id = users_from_db[0]['id']

  return render_template('index.html', u_id=users_from_db[0], users=users_from_db, title="User Dashboard")

@app.route('/create', methods=['POST'])
def create():

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
    # The following two lines combined md5 and salt 
    # to create the input value (password).  They are now deprecated
    # salt = binascii.b2a_hex(os.urandom(15))
    # hashed_password = md5.new(password + salt).hexdigest()
    # use bcrypt to hash password instead
    hashed_password = flask_bcrypt.generate_password_hash(password)
    print "Here is the hashed password: ", hashed_password, '\n'

    insert_query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())'

    # print "Here is the insert query: ", insert_query, '\n'
    data = {
      'first_name': first_name,
      'last_name': last_name,
      'email': email,
      'pw_hash': hashed_password
    }

    user_id = mysql.query_db(insert_query, data)
    print 'User ID returned from query', user_id
    session['user_id'] = user_id
    session['login_status'] = True
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

  # if we find a user with this email address, try to check the password
  if len(users_list) > 0:
    user = users_list[0]
  else:
    errors.append('Invalid username or password')

  # create salt and combine with input value (password)
  # salt = user['salt']  # salt no longer need => using bcrypt
  # hashed_input = md5.new(password + salt).hexdigest()

  # use bcrypt to hash password instead
  form_input = flask_bcrypt.generate_password_hash(password)
  print "*" * 80
  print "User password entered: ", form_input, '\n'
  print "User password from db: ", user['password']
  print "*" * 80

  if flask_bcrypt.check_password_hash(user['password'], form_input):  # returns True => success
    session['user_id'] = user['id']
    print "Successful login"
    # return redirect('/')
  else:  # failed login
    errors.append('Invalid username or password')
    # return redirect('/new')
    print "Password validation failed!"

    # print "*" * 80
    # print "Session user_id is: ", session['user_id']

  if len(errors) > 0:
    for error in errors:
      flash(error)
    return redirect('/new')
  # if all error validations cleared, then success
  else:
    for success in successes:
      flash(success)
    session['login_status'] = True
    print "*" * 80
    print "Successful login! session status is now: ", session['login_status']
    print "*" * 80
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


@app.route('/<user_id>')
def show(user_id):

  query = 'SELECT * FROM users WHERE id = :user_id'

  data = {
    'user_id': user_id
  }
  users_from_db = mysql.query_db(query, data)

  print "*" * 80
  print users_from_db
  print session
  print "*" * 80

  return render_template('show.html', u_id=user_id, users=users_from_db, title="Show user")


@app.route('/<user_id>/edit')
def edit(user_id):

  query = 'SELECT * FROM users WHERE id = :user_id'

  data = {
    'user_id': user_id
  }
  users_from_db = mysql.query_db(query, data)

  print "*" * 80
  print users_from_db
  print "*" * 80

  return render_template('edit.html', u_id=user_id, user=users_from_db[0], title="Edit user")


@app.route('/<user_id>/update', methods=['POST'])
def update(user_id):

  # variable to shorten all request.form references to just 'form'
  form = request.form
  first_name = form['first_name']
  last_name = form['last_name']
  email = form['email']

  # create an empty list to store errors/successes
  errors = []
  successes = []
  if len(first_name) < 1:
    errors.append('First name must not be blank.')
  if len(first_name) < 3:
    errors.append('First name must be at least 3 characters.')
  if len(last_name) < 1:
    errors.append('Last name must not be blank.')
  if len(last_name) < 3:
    errors.append('Last name must be at least 3 characters.')
  if len(email) < 1:
    errors.append('Email must not be blank.')
  if not EMAIL_REGEX.match(email):
    errors.append('You must enter a valid email address!')
  else:
    successes.append('Success')

  if len(errors) > 0:
    for error in errors:
      flash(error)
    return redirect('/<user_id>/edit')
  # if all error validations cleared, then success
  else:
    for success in successes:
      flash(success)

  # Write query to select specific user by id and update that users information, including updated_at
  update_query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, updated_at = NOW() WHERE id = :specific_user_id"
  
  # define user_id with dictionary from the POST data received.
  data = {
    'specific_user_id': user_id,
    'first_name': first_name,
    'last_name': last_name
  }
 
  # Run query, with dictionary values injected into the query.
  mysql.query_db(udpdate_query, data)

  return redirect('/')

@app.route('/<user_id>/delete')
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