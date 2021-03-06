from flask import Flask, request, redirect, render_template, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
# the "re" module will let us perform some regular expression operations
# babel for defining a filter
import re, babel, datetime
# use bcrypt instead of md5
from flask_bcrypt import Bcrypt

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'bobdobalina'

def format_datetime(value, format='medium'):
  if format == 'full':
    format="EEEE, d. MMMM y 'at' HH:mm"
  elif format == 'medium':
    format="EE dd.MM.y HH:mm"
  return babel.dates.format_datetime(value, format)

app.jinja_env.filters['datetimeformat'] = format_datetime

# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'the_wall')
flask_bcrypt = Bcrypt(app)

@app.route('/')
def index():

  if 'form_data' not in session:
    session['form_data'] = {}

  if 'posts' not in session:
    posts = 'No post value available'

  if not 'logged_id' in session:
    session['logged_id'] = False
    # print "session['logged_id'] NOT found, setting it to: ", session['logged_id']
  else:
    logged_id = session['logged_id']
    # print "session['logged_id'] found, setting it to: ", logged_id

  query = 'SELECT * FROM users'
  users_from_db = mysql.query_db(query)

  # purpose of this entire block of code is that I'm trying to return user information 
  # for just the user whose user['id'] matches the session['logged_id'] 
  # set during the /handle_user route 

  if session['logged_id'] != False:
    query = 'SELECT * FROM users WHERE id = :specific_user_id'

    data = {
      'specific_user_id': logged_id
    }
    # check for username
    specific_user_from_db = mysql.query_db(query, data)

    # print "Here is the :specific_user_id result: ", specific_user_from_db
    # print "Here is the value of logged_id: ", logged_id

  posts_query = 'SELECT users.first_name, users.last_name, messages.content, messages.id, messages.user_id, messages.created_at FROM messages JOIN users ON messages.user_id = users.id'
  posts = mysql.query_db(posts_query)

  comments_query = 'SELECT users.first_name, users.last_name, comments.comment, comments.id, comments.message_id, comments.user_id, comments.created_at FROM comments JOIN users ON comments.user_id = users.id JOIN messages ON comments.message_id = messages.id'
  comments = mysql.query_db(comments_query)

  return render_template('index.html', users=users_from_db, all_posts=posts, all_comments=comments, title="The Wall")
  # return render_template('index.html', user=specific_user_from_db[0], users=users_from_db, title="The Wall")  
  # => this breaks when the logout button is clicked and the session (and session['logged_id']) are cleared.  
  # I know why, it's because if there is no 'logged_id', the 2nd SQL query will not run 
  # and therefore user=specific_user_from_db[0] is pointless.


# create new user route
@app.route('/handle_user', methods=['POST'])
def users():
  # shorten request.form calls
  form = request.form
    
  # define an empty list to hold error messages
  errors = []
  successes = []

  # put into variables form input info
  action = form['action']
  first_name = form['first_name']
  last_name = form['last_name']
  username = form['username']
  email = form['email']
  password = form['password']
  confirm_password = form['confirm_password']

  # if action == 'register':
  session['form_data'] = {}

  print "Session form data is: ", session['form_data']

  if len(first_name) < 1:
    errors.append('First name cannot be blank!')
  if len(last_name) < 1:
    errors.append('Last name cannot be blank!')
  if len(username) < 1:
    errors.append('Username cannot be blank!')
  if len(email) < 1:
    errors.append('Email cannot be blank!')
  if not EMAIL_REGEX.match(email):
    errors.append('You must enter a valid email address!')

  if len(password) < 1:
    errors.append('Password must be not be blank.')
  if len(confirm_password) < 1:
    errors.append('Confirm password must not be blank.')
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
    return redirect('/')
  # if all error validations cleared, then success
  else:
    for success in successes:
      flash(success)

    # use bcrypt to hash password instead
    hashed_password = flask_bcrypt.generate_password_hash(password)
    print "Here is the hashed password: ", hashed_password, '\n'

    insert_query = 'INSERT INTO users (`first_name`, `last_name`, `username`, `email`, `password`, `created_at`, `updated_at`) VALUES (:first_name, :last_name, :username, :email, :pw_hash, NOW(), NOW())'

    data = {
      'first_name': first_name,
      'last_name': last_name,
      'username': username,
      'email': email,
      'pw_hash': hashed_password
    }

    user_id = mysql.query_db(insert_query, data)
    print 'User ID returned from query', user_id
    print 'You have successfully registered!'
    session['logged_id'] = user_id
    session['login_status'] = True

    return redirect('/')


# login route
@app.route('/login', methods=['POST'])
def login():

  # elif action == 'login':
    # shorten request.form calls
    form = request.form
    action = form['action']

    # define empty list to store error messaging
    errors = []
    successes = []

    # put into variables form input info
    username = form['username']
    password = form['password']

    # validate data
    if len(username) < 1:
      errors.append('Username cannot be blank!')
    if len(password) < 1:
      errors.append('Password cannot be blank!')

    if len(errors) > 0:
      for error in errors:
        flash(error)
      return redirect('/')
    else:
      for success in successes:
        flash(successes)

      query = 'SELECT * FROM users WHERE username = :given_username'

      data = {
        'given_username': username
      }
      # check for username
      users_list = mysql.query_db(query, data)

      # if we find a user with this email address, try to check the password
      if len(users_list) > 0:
        user = users_list[0]
      else:
        errors.append('Invalid username or password')
      
      # use bcrypt to check already hashed password
      if flask_bcrypt.check_password_hash(user['password'], password):  # returns True => success
        print "Successful login"
        session['logged_id'] = user['id']
        return redirect('/')
      else:  # failed login
        errors.append('Invalid username or password')
        # errors.append('Incorrect password')
        print "Failed login!"
        # return redirect('/')

      return redirect('/')

@app.route('/post_message', methods=['POST'])
def handle_messages():

  #handle form requests
  form = request.form

  # empty lists for errors/successes
  errors = []
  successes = []

  # user_id = form['id']
  content = form['content']
  session['form_data'] = {}

  print "Session form data is: ", session['form_data']

  if len(content) < 1:
    errors.append('Message field cannot be blank!')
  if len(content) > 1000:
    errors.append('Messages cannot be greater than 1000 characters!')

  if len(errors) > 0:
    for error in errors:
      flash(error)
    return redirect('/')
  else:
    for success in successes:
      flash(successes)

    # query database for logged-in user
    insert_query = 'INSERT INTO messages (`user_id`,`content`,`created_at`,`updated_at`) VALUES (:user_id, :message_content, NOW(), NOW())'

    data = {
      'message_content': content,
      'user_id': session['logged_id']
    }

    inserted_id = mysql.query_db(insert_query, data)
    # return "Successfully made posts!"
    print 'Here is the insert query: ', inserted_id
    print 'Here data in the post: ', data
    return redirect('/wall')

  errors.append('Message failed to post.  Try again')
  return redirect('/')

@app.route('/post_comment', methods=['POST'])
def handle_comments():
  #handle form requests
  form = request.form

  # empty lists for errors/successes
  errors = []
  successes = []

  # user_id = form['id']
  comment = form['comment']
  message_id = form['message_id']
  session['form_data'] = {}

  print "Session form data is: ", session['form_data']

  if len(comment) < 1:
    errors.append('Message field cannot be blank!')
  if len(comment) > 750:
    errors.append('Messages cannot be greater than 750 characters!')

  if len(errors) > 0:
    for error in errors:
      flash(error)
    return redirect('/')
  else:
    for success in successes:
      flash(successes)

    comment_query = 'INSERT INTO comments (`user_id`, `message_id`, `comment`,`created_at`,`updated_at`) VALUES (:user_id, :message_id, :comment_content, NOW(), NOW())'

    data = {
      'comment_content': comment,
      'user_id': session['logged_id'],
      'message_id': message_id
    }

    inserted_id = mysql.query_db(comment_query, data)
    # return "Successfully made posts!"
    print 'Here is the insert query: ', inserted_id
    print 'Here data in the post: ', data
    return redirect('/wall')

  errors.append('Comment failed to post.  Try again')
  return redirect('/')

@app.route('/wall')  # aka dashboard from previous lecture videos/examples
def wall():

  # check if logged_id is in session, redirect to index route if not
  if 'logged_id' not in session:
    return redirect('/')

  # query database for logged-in user
  logged_in_query = 'SELECT * FROM users WHERE id = :logged_id'

  data = {
    'logged_id': session['logged_id']
  }

  logged_in_user = mysql.query_db(logged_in_query, data)

  posts_query = 'SELECT users.first_name, users.last_name, messages.content, messages.id, messages.user_id, messages.created_at FROM messages JOIN users ON messages.user_id = users.id'
  posts = mysql.query_db(posts_query)

  comments_query = 'SELECT users.first_name, users.last_name, comments.comment, comments.id, comments.message_id, comments.user_id, comments.created_at FROM comments JOIN users ON comments.user_id = users.id JOIN messages ON comments.message_id = messages.id'
  comments = mysql.query_db(comments_query)

  return render_template('show.html', current_user=logged_in_user, all_posts=posts, all_comments=comments, title="Message page")


@app.route('/delete/<post_id>')
def delete_post(post_id):

  # delete query for specific user_id passed with results
  delete_query = 'DELETE FROM messages WHERE id = :specific_msg_id'

  # define user_id with dictionary
  data = {
    'specific_msg_id': post_id
  }

  # execute query to delete data by user_id
  mysql.query_db(delete_query, data)

  return redirect('/wall')


@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')

app.run(debug=True)
