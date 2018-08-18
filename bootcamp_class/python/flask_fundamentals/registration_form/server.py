from flask import Flask, session, render_template, redirect, request, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'.*([0-9]+).*')  # cannot contain numbers
PW_REGEX = re.compile(r'.*[a-z][A-Z].*$')  # cannot contain numbers

app = Flask(__name__)
app.secret_key = 'bobdobalina'

@app.route('/')
def index():
  print "*" * 80
  print "Hello! You've reached the index route!"

  if not 'first_name' in session:
    first_name = 'No first name entered!'
  else:
    first_name = session['first_name']
  if not 'last_name' in session:
    last_name = 'No last name entered!'
  else:
    last_name = session['last_name']
  if not 'email' in session:
    email = 'No email entered!'
  else:
    email = session['email']
  if not 'pw1' in session:
    pw1 = 'No password1 entered!'
  else:
    pw1 = session['pw1']
  if not 'pw2' in session:
    pw2 = 'No password2 entered!'
  else:
    pw2 = session['pw2']

  print session
  return render_template('index.html', title="Basic Validation Form")

@app.route('/process', methods=['POST'])
def process_form():
  print "*" * 80
  print "Hello! You've reached the process route!"
  # variable to shorten all request.form references to just 'form'
  form = request.form
  # create an empty list to store errors
  errors = []

  # recall the name attributes we added to our form inputs
  # to access the data that the user input into the fields we use request.form['name_of_input']

  # if length of request.form name less than three
  if len(form['first_name']) < 1:
    errors.append('First name must not be blank!')  # just pass a string to the flash function
  elif len(form['first_name']) < 3:
    errors.append('You must enter a name of sufficient length!')
  
  if NAME_REGEX.match(form['first_name']):
    errors.append('Your name may not include any numbers!')

  if len(form['last_name']) < 1:
    errors.append('Last name must not be blank!')
  elif len(form['last_name']) < 3:
    errors.append('You must enter a name of sufficient length!')
  
  if NAME_REGEX.match(form['last_name']):
    errors.append('Your name may not include any numbers!')

  print "Here is the length of the f_name field: ", len(form['first_name'])
  print "Here is the length of the l_name field: ", len(form['last_name'])

  if len(form['email']) < 1:
    errors.append('Email address cannot be blank!')
  elif not EMAIL_REGEX.match(form['email']):
    errors.append('You must enter a valid email address!')

  if len(form['pw1']) < 1 or len(form['pw2']) < 1:
    errors.append('You must fill out both password fields!')
  # elif not PW_REGEX.match(form['pw1']) or not PW_REGEX.match(form['pw2']):
  #   errors.append('You must enter a valid email address!')

  if form['pw1'] != form['pw2']:
    errors.append('Your passwords do not match.  Please check your passwords.')
  elif re.search('[0-9]', form['pw1']) is None or re.search('[0-9]', form['pw2']) is None:
    errors.append('Your password must contain at least one number.')
  elif re.search('[A-Z]', form['pw1']) is None or re.search('[A-Z]', form['pw2']) is None:
    errors.append('Your password must contain at least one capital letter.')

  # print "Here is the length of the email field: ", len(form['email'])
  # print "Here is the data stored for passwords: ", form['pw1'], form['pw2']
  # print "Here is the data stored for errors: ", errors

  if len(errors) > 0:
    for error in errors:
      flash(error)
    return redirect('/')
  else:
    session['first_name'] = form['first_name']
    session['last_name'] = form['last_name']
    session['email'] = form['email']
    session['pw1'] = form['pw1']
    session['pw2'] = form['pw2']
    session['success'] = True
    return redirect('/success')

  print "Here is the data stored for session: ", session

@app.route('/success')
def success():

  return render_template('success.html', title="Success")

@app.route('/clear')
def clear():
  session.clear()
  return redirect('/')

app.run(debug=True)