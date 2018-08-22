from flask import Flask, request, redirect, render_template, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'bobdobalina'

# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'userdemodb')

@app.route('/')
def index():
  # an example of running a query
  # print mysql.query_db('SELECT * FROM friends')
  email_from_db = mysql.query_db('SELECT email FROM users')

  print "*" * 80
  print 'Here are the emails in the db:', email_from_db

  if not 'email' in session:
    email = 'No email entered!'
  else:
    email = session['email']

  return render_template('index.html', email=email_from_db, title="Home")

@app.route('/validate', methods=['POST'])
def validate():

  # try:
  #   email... = results[0]
  # except IndexError:
  #   ...

  # variable to shorten all request.form references to just 'form'
  form = request.form
  form['email']
  # create an empty list to store errors/successes
  errors = []
  successes = []

  # recall the name attributes we added to our form inputs
  # to access the data that the user input into the fields we use request.form['email']
  # Write query as a string.  => pass form entered email into the string
  validate_query = "SELECT email FROM users WHERE email = :email"
  
  # We'll then create a dictionary of data from the POST data received.
  data = {
    'email': form['email']
  }

  # Run query, with dictionary values injected into the query.
  results = mysql.query_db(validate_query, data)

  if len(results) == 0:
    email_from_db = "Email does not exist"
    errors.append('That email address does not exist!')
  else:
    email_from_db = results[0]['email']

  # print "*" * 80
  # print "Here is the email from the form: ", form['email'], "\n"
  # print 'Here is the email from the database:', email_from_db, '\n'

  # validate email address
  # if the email address is less than 1, the field is blank => error
  if len(form['email']) < 1:
    errors.append('Email address cannot be blank!')
  elif not EMAIL_REGEX.match(form['email']):
    errors.append('You must enter a valid email address!')
  else:
    successes.append('Success')

  if len(errors) > 0:
    for error in errors:
      flash(error)
    return redirect('/')
  # if all error validations cleared, then success
  else:
    # if length of success messages are > zero
    if len(successes) > 0:
      # print "Here are the db results: ", results, '\n'
      validated_email = email_from_db
      session['validated_email'] = validated_email
      session['success'] = True
      return redirect('/success')

@app.route('/success')
def success():

  # get emails and updated_at info from db
  query = "SELECT id, email, updated_at FROM users"

  results = mysql.query_db(query)

  return render_template('success.html', user_results=results, title="Success")


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