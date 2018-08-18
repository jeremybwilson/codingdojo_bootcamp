from flask import Flask, session, render_template, redirect, request, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'bobdobalina'

@app.route('/')
def index():
  print "*" * 80
  print "Hello! You've reached the index route!"

  if not 'name' in session:
    name = 'No name entered!'
  else:
    name = session['name']

  if not 'email' in session:
    email = 'No name entered!'
  else:
    email = session['email']

  return render_template('index.html', title="Basic Validation Form")

@app.route('/process', methods=['POST'])
def process_form():
  print "*" * 80
  print "Hello! You've reached the process route!"

  # variable to shorten all request.form references to just 'form'
  form = request.form
  # create an empty list to store errors
  errors = []
  successes = []

  # recall the name attributes we added to our form inputs
  # to access the data that the user input into the fields we use request.form['name_of_input']

  # if length of request.form name less than three
  if len(form['name']) < 1:
    errors.append('Name must not be blank!') 
  elif len(form['name']) < 3:
    # just pass a string to the flash function
    errors.append('You must enter a name of sufficient length!') 
  else:
    successes.append('Success')

  print "Here is the length of the name field: ", len(form['name'])

  if len(form['email']) < 1:
    errors.append('Email address cannot be blank!')
  elif not EMAIL_REGEX.match(request.form['email']):
    # just pass a string to the flash function
    errors.append('You must enter a valid email address!')
  else:
    successes.append('Success')

  print "Here is the length of the email field: ", len(form['email'])
  print "Here is the data stored for errors: ", errors
  print "Here is the data stored for success: ", successes
  print "Here is the data stored for session: ", session

  if len(errors) > 0:
    for error in errors:
      flash(error)
    return redirect('/')
  else:
    # session_name = form['name']
    session['name'] = form['name']
    # session_email = form['email']
    session['email'] = form['email']
    if len(successes) > 0:
      for success in successes:
        flash(successes)
    session['success'] = True
    return redirect('/success')

@app.route('/success')
def success():

  return render_template('success.html', title="Success")

@app.route('/clear')
def clear():

  session.clear()

  return redirect('/')

app.run(debug=True)