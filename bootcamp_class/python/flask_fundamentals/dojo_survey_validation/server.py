from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)

app.secret_key = 'bobdobalina'

@app.route('/')
def index():
  print "*" * 60
  print "Hello! You've reached the index route!"

  if not 'name' in session:
    session['name'] = 'No name entered'
  if not 'location' in session:
    session['location'] = 'No location entered'
  if not 'language' in session:
    session['language'] = 'No language chosen'
  if not 'comments' in session:
    session['comments'] = 'No comments entered'

  print session['name'], "\n", session['location'], "\n", session['language'], "\n", session['comments'], "\n"
  return render_template('index.html', title="Coding Dojo Survey")


@app.route('/process', methods=['POST'])
def show_result():
  print "*" * 60
  print "Got Post Info"
  # notice how the key we are using to access the info corresponds with the names
  # of the inputs from our html form
  form = request.form
  errors = []

  # recall the name attributes we added to our form inputs
  # to access the data that the user input into the fields we use request.form['name_of_input']

  # if length of request.form name less than three
  if len(form['name']) < 3:
    errors.append('Name value must be at least three characters long!') # just pass a string to the flash function
  # else:
  #   errors.append('Success! Your name is {}'.format(form['name'])) # just pass a string to the flash function

  if form['location'] == '':
    errors.append('You did not choose a location!')  # just pass a string to the flash function
  # else:
  #   errors.append('Success! Your city is: {}'.format(form['location'])) # just pass a string to the flash function

  if form['language'] == '':
    errors.append('You did not choose a language!')  # just pass a string to the flash function
  # else:
  #   errors.append('Success! Your favorite language is: {}'.format(form['language'])) # just pass a string to the flash function

  if len(form['comments']) < 10 or len(form['comments']) > 120:
    errors.append('Comments must be at least 10 characters and no greater than 120 characters long!') # just pass a string to the flash function
  # else:
  #   errors.append('Success! Your comment is: {}'.format(form['comments'])) # just pass a string to the flash function

  if len(errors) > 0:
    for error in errors:
      flash(error)
    return redirect('/') # redirects back to '/' route
  else:
    session['name'] = form['name']
    session['location'] = form['location']
    session['language'] = form['language']
    session['comments'] = form['comments']
    return redirect('/result') # redirects to the '/result' route

@app.route('/result', methods=['GET'])
def success():
  print "*" * 60
  print "Got post info"

  # recall the name attributes we added to our form inputs
  # to access the data that the user input into the fields we use request.form['name_of_input']
  print session['name'], "\n", session['location'], "\n", session['language'], "\n", session['comments'], "\n"
  return render_template('result.html', title="Submitted Info")

app.run(debug=True)
