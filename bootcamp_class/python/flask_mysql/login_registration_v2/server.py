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
mysql = MySQLConnector(app, 'login_registration_v2')
flask_bcrypt = Bcrypt(app)

@app.route('/')
def index():

  if 'logged_id' not in session:
    return redirect('/new')
  else:
    logged_id = session['logged_id']
    print "Here is the session['logged_id'] info: ", logged_id

  query = 'SELECT * FROM users'
  
  users_list = mysql.query_db(query)
  users = users_list
  logged_in_user = users_list[0]

  # print 'Here are the query results: ', users_list
  print 'Here is the logged in user\'s info: ', logged_in_user
  print 'Here is the logged in user\'s ID : ', logged_in_user['id']

  return render_template('index.html', users_list=logged_in_user, users_from_db=users, title="Home")


@app.route('/create', methods=['POST'])
def create():
  # processing the create form
  form = request.form
  first_name = form['first_name']
  last_name = form['last_name']
  email = form['email']
  password = form['password']
  confirm_password = form['confirm_password']

  # empty lists for error/success messages
  errors = []
  successes = []

  if len(form['first_name']) < 1:
    errors.append('First name cannot be blank.')
  if len(form['first_name']) < 3:
    errors.append('First name must be at least 3 characters long.')
  if len(form['last_name']) < 1:
    errors.append('Last name cannot be blank.')
  if len(form['last_name']) < 3:
    errors.append('Last name must be at least 3 characters long.')
  if len(form['email']) < 1:
    errors.append('Email cannot be blank.')
  if not EMAIL_REGEX.match(email):
    errors.append('You must enter a valid email address!')

  if len(form['password']) < 1:
    errors.append('Password cannot be blank.')
  if len(form['password']) < 4:
    errors.append('Password must be at least 4 characters long.')
  if len(form['confirm_password']) < 1:
    errors.append('Confirm password cannot be blank.')
  if password != confirm_password:
    errors.append('Passwords do not match!')

  # check to see if user email exists in the db
  exists_query = 'SELECT email FROM users WHERE email = :specific_user_email'
  
  exists_data = {
    'specific_user_email': email
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

    # use bcrypt to hash password instead
    hashed_password = flask_bcrypt.generate_password_hash(password)
    print "Here is the hashed password: ", hashed_password, '\n'

    insert_query = 'INSERT INTO users (`first_name`, `last_name`, `email`, `password`, `created_at`, `updated_at`) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())'

    data = {
      'first_name': first_name,
      'last_name': last_name,
      'email': email,
      'pw_hash': hashed_password
    }

    user_id = mysql.query_db(insert_query, data)
    print 'User ID returned from query', user_id
    print 'You have successfully registered!'
    session['logged_id'] = user_id
    session['login_status'] = True
    print "Here is the session user_id: ", user_id

  return redirect('/')

@app.route('/login', methods=['POST'])
def login():

  # processing the create form
  form = request.form
  # put into variables form input info
  email = form['email']
  password = form['password']
  
  # empty lists for error/success messages
  errors = []
  successes = []

  if len(form['email']) < 1:
    errors.append('Email cannot be blank.')
  if not EMAIL_REGEX.match(email):
    errors.append('You must enter a valid email address!')
  if len(form['password']) < 1:
    errors.append('Password cannot be blank.')

  # validate data
  if len(errors) > 0:
    for error in errors:
      flash(error)
    return redirect('/')
  else:
    for success in successes:
      flash(successes)

    query = 'SELECT * FROM users WHERE email = :specific_user_email'

    data = {
      'specific_user_email': email
    }
    # check for username
    users_list = mysql.query_db(query, data)

    if len(users_list) == 0:
      errors.append('Invalid email or password.')

    # if we find a user with this email address, try to check the password
    if len(users_list) > 0:
      user = users_list[0]
    else:
      errors.append('Invalid email or password.')
    
    # use bcrypt to check already hashed password
    if flask_bcrypt.check_password_hash(user['password'], password):  # returns True => success
      print "Successful login"
      # return redirect('/')
    else:  # failed login
      errors.append('Invalid username or password')
      print "Failed login!"
      return redirect('/new')

    session['logged_id'] = user['id']
    return redirect('/')


@app.route('/<user_id>/edit')
def edit(user_id):
  query = 'SELECT * FROM users WHERE id = :user_id'

  data = {
    'user_id': user_id
  }
  users_list = mysql.query_db(query, data)
  user = users_list[0]

  print "*" * 80
  print user
  print "*" * 80

  # processing the edit form
  return render_template('edit.html', user=user, title="Edit")


@app.route('/<user_id>/update', methods=['POST'])
def update(user_id):

  # processing the create form
  form = request.form
  # put into variables form input info
  first_name = form['first_name']
  last_name = form['last_name']
  email = form['email']

  # create empty lists for error and success messages
  errors = []
  successes = []

  if len(first_name) < 1:
    errors.append('First name cannot be blank')
  if len(last_name) < 1:
    errors.append('Last name cannot be blank')
  if len(email) < 1:
    errors.append('Email cannot be blank.')
  if not EMAIL_REGEX.match(email):
    errors.append('You must enter a valid email address!')

  if len(errors) > 0:
    for error in errors:
      flash(errors)
    return redirect('/<user_id>/edit')
  else:
    for success in successes:
      flash(successes)

    # Write query to select specific user by id and update that users information, including updated_at
    update_query = 'UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :specific_user_id'

    # define user_id with dictionary from the POST data received.
    data = {
    'specific_user_id': user_id,
    'first_name': first_name,
    'last_name': last_name,
    'email': email
    }

    # Run query, with dictionary values injected into the query.
    mysql.query_db(update_query, data)
    print "Successfully updated user: ", user_id

    # processing the update form
    return redirect('/')

  errors.append('User failed to update.  Try again')
  return redirect('/<user_id>/edit')


@app.route('/<user_id>')
def show(user_id):

  user_query = 'SELECT * FROM users WHERE id = :specific_user_id'

  data = {
    'specific_user_id': user_id
  }

  users_list = mysql.query_db(user_query, data)

  print "users_list info is: ", users_list
  user = users_list[0]

  reminder_query = 'SELECT * FROM reminders WHERE creator_id = :specific_user_id'

  reminders = mysql.query_db(reminder_query, data)

  return render_template('show.html', user=user, reminder_list=reminders, title="Show")

@app.route('/cheat-sheet')
def cheat_sheet():

  return render_template('restful-routes.html', title="RESTful Routes")


@app.route('/<user_id>/delete', methods=['POST'])
def delete(user_id):

  # delete query for specific user_id passed with results
  delete_query = 'DELETE FROM users WHERE id = :specific_user_id'
  # define user_id with dictionary
  data = {
    'specific_user_id': user_id
  }
  # execute query to delete data by user_id
  mysql.query_db(delete_query, data)
  # clear the session
  session.clear()

  # process the delete form and redirect to registration page
  return redirect('/new')

@app.route('/new')
def new():

  return render_template('new.html', title="New")


@app.route('/logout')
def logout():

  session.clear()
  return redirect('/')


@app.route('/remind_new')
def remind_new():

  return render_template('remind_new.html', title="New reminder")


@app.route('/remind_create', methods=['POST'])
def remind_create():

  # if not 'user_id' in session:
  #   return redirect('/new')
  if not 'logged_id' in session:
    return redirect('/new')
  else:
    logged_id = session['logged_id']
    print "Here is the session['logged_id'] info: ", logged_id

  form = request.form
  content = form['content']

  errors = []
  successes = []

  if len(content) < 3:
    errors.append('Reminder must be at least 3 characters.')

  if len(errors) > 0:
    for error in errors:
      flash(errors)
    return redirect('/remind_new')
  else:
    for success in successes:
      flash(successes)

    reminder_query = 'INSERT INTO reminders (content, remind_on_date, created_at, updated_at, creator_id) VALUES (:content, NOW(), NOW(), NOW(), :current_user_id)'

    reminder_data = {
      'content': content,
      'current_user_id': logged_id
    }

    reminder_result = mysql.query_db(reminder_query, reminder_data)


  return redirect('/')


app.run(debug=True)