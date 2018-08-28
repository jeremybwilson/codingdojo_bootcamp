from flask import Flask, request, redirect, render_template, session, flash

# import the Connector function
from mysqlconnection import MySQLConnector

# use bcrypt instead of md5
from flask_bcrypt import Bcrypt

# import regular expression library
import re

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)

app.secret_key = 'bobdobalina'

# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'airbnb_clone')

flask_bcrypt = Bcrypt(app)


@app.route('/')
def index():

  if 'user_id' not in session:
    session['user_id'] = 'No User ID in session'
    # return redirect('/new')
  else:
    user_id = session['user_id']
    print "Here is the session['user_id'] info: ", user_id

  return render_template('index.html', title="Home")


@app.route('/register', methods=['POST'])
def register():

  # shorten the request.form call
  form = request.form
  errors = []
  successes = []
  print "Form data is: ", form

  #validate the data
  is_valid = True

  if len(form['name']) < 1:
    is_valid = False
    errors.append('Name field cannot be blank.')
  if len(form['email']) < 1:
    is_valid = False
    errors.append('Email field cannot be blank.')
  if not EMAIL_REGEX.match(form['email']):
    is_valid = False
    errors.append('You must enter a valid email address!')

  if len(form['password']) < 1:
    is_valid = False
    errors.append('Password cannot be blank.')
  # if len(form['password']) < 4:
  #   is_valid = False
  #   errors.append('Password must be at least 4 characters long.')
  if len(form['confirm_password']) < 1:
    is_valid = False
    errors.append('Confirm password cannot be blank.')
  if form['password'] != form['confirm_password']:
    is_valid = False
    errors.append('Passwords do not match!')

  # check to see if user email exists in the db
  exists_query = 'SELECT email FROM users WHERE email = :specific_user_email'
  
  exists_data = {
    'specific_user_email': form['email']
  }
  users_list = mysql.query_db(exists_query, exists_data)

  if len(users_list) > 0:
    is_valid = False
    errors.append('Email already exists, choose another.')

  # if any validations above failed, then set is_valid to false and flash errors
  if is_valid != True:
    if len(errors) > 0:
      for error in errors:
        flash(error)
      return redirect('/')
  else:
    # use bcrypt to hash password instead
    hashed_password = flask_bcrypt.generate_password_hash(form['password'])
    print "Here is the hashed password: ", hashed_password

    insert_query = "INSERT INTO users (name, email, password, created_at, updated_at) VALUES (:name, :email, :pw_hash, NOW(), NOW())"

    data = {
      'name': form['name'],
      'email': form['email'],
      'pw_hash': hashed_password
    }

    user_id = mysql.query_db(insert_query, data)
    print 'The ID returned for this query is: ', user_id
    print 'You have successfully registered!'
    session['user_id'] = user_id
    session['login_status'] = True
    # print "Here is the session user_id: ", user_id

  return redirect('/')


@app.route('/login', methods=['POST'])
def login():

  # shorten the request.form call
  form = request.form
  print "*" * 80
  print "form data is: ", form

  errors = []
  successes = []
  is_valid = True

  if len(form['email']) < 1:
    is_valid = False
    errors.append('Email field cannot be blank.')
  if not EMAIL_REGEX.match(form['email']):
    is_valid = False
    errors.append('You must enter a valid email address!')

  if len(form['password']) < 1:
    is_valid = False
    errors.append('Password field cannot be blank.')

  print "*" * 80

  if is_valid != True:
    if len(errors) > 0:
      for error in errors:
        flash(error)
      # return redirect('/')
  else:
    query = "SELECT * FROM users where email = :specific_user_email"

    data = {
      'specific_user_email': form['email']
    }

    users_list = mysql.query_db(query, data)
    print "*" * 80

    if len(users_list)> 0:
      user = users_list[0]
      print "User result from database is: ", user
      password = form['password']
      result = flask_bcrypt.check_password_hash(user['password'], password)
      if result == True:
        session['user_id'] = user['id']
        return redirect('/dashboard')
      else:
        errors.append('Invalid entry')
    else:
      errors.append('Email does not exist')

  session['logged_id'] = user['id']
  return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():

  print "*" * 80
  print "Here is the session ID: ", session['user_id']

  query = 'SELECT * FROM users WHERE id = :specific_user_id'

  data = {
    'specific_user_id': session['user_id']
  }

  users_list = mysql.query_db(query, data)
  user = users_list[0]

  property_query = 'SELECT * FROM properties JOIN users ON users.id = properties.user_id'
  properties = mysql.query_db(property_query)
  bookings_query = "SELECT * FROM bookings JOIN properties ON properties.id = property_id WHERE bookings.user_id = {}".format(session['user_id'])
  bookings = mysql.query_db(bookings_query)

  return render_template('dashboard.html', all_users=users_list, properties=properties, bookings=bookings, title="Dashboard")


@app.route("/property/create", methods=['POST'])
def property_create():
  # shorten the request.form call
  form = request.form

  errors = []
  successes = []

  if len(form['price']) < 1:
    errors.append('Price field cannot be blank.')
  if len(form['room']) < 1:
    errors.append('Room field cannot be blank.')
  if len(form['address']) < 1:
    errors.append('Address field cannot be blank.')

  if len(errors) > 0:
    for error in errors:
      flash(error)
    return redirect('/dashboard')
  else:
    for success in successes:
      flash(successes)

    # validation
    query = "INSERT INTO properties (`price`, `rooms`, `address`, `user_id`, `created_at`, `updated_at`) VALUES (:price, :room, :address, :user_id, NOW(), NOW())"

    data = {
      'price': form['price'],
      'room': form['room'],
      'address': form['address'],
      'user_id': session['user_id']
    }

    result = mysql.query_db(query, data)
    return redirect('/dashboard')

  return redirect('/')

@app.route('/property/show/<property_id>', methods=['POST'])
def property_show(property_id):

  property_query = 'SELECT * FROM properties WHERE id = :property_id'
  data = {
    'property_id': property_id
  }
  mysql.query_db(property_query, data)

  property_bookings = "SELECT * FROM bookings JOIN users ON users.id = user_id WHERE bookings.property_id = {}".format(property_id)
  bookings = mysql.query_db(property_bookings)

  return redirect('/dashboard')

@app.route('/bookings/<property_id>', methods=['POST'])
def bookings(property_id):
  # shorten the request.form call
  form = request.form

  # validation
  query = "INSERT INTO bookings (`user_id`, `property_id`, `from`, `to`, `price`, `created_at`, `updated_at`) VALUES (:user_id, :property_id, :from, :to, :price, NOW(), NOW());"
  data = {
    'user_id': session['user_id'],
    'property_id': property_id,
    'from': form['from'],
    'to': form['to'],
    'price': form['price']
  }

  mysql.query_db(query, data)
  return redirect('/dashboard')

@app.route('/logout')
def logout():

  session.clear()
  return redirect('/')


app.run(debug=True)