from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'bobdobalina'

@app.route('/', methods=['GET', 'POST'])
def index():
  print "Got Post Info"

  # if 'ninja_count' not in session:
  #   session['ninja_count'] = 0
  
  if not 'name' in session:
    session['name'] = 'No name entered'
  if not 'email' in session:
    session['email'] = 'No email entered'

  if 'session_count' not in session:
    session['session_count'] = 1
  else:
    session['session_count'] += 1

  return render_template('index.html', title="Form test")

@app.route('/users', methods=['GET', 'POST'])
def create_user():
  print "Got post info"
  print "*" * 80
  print request.form
  # recall the name attributes we added to our form inputs
  # to access the data that the user input into the fields we use request.form['name_of_input']
  session['name'] = request.form['name']
  session['email'] = request.form['email']
  # this does not work and returns KeyError in flask => it errors out because the create_user def is using a redirect and the data won't persist because of it.
  # name = request.form['name']
  # email = request.form['email']
  print session['name'], session['email']
  return redirect('/success') # redirects back to the '/success' route


@app.route('/success', methods=['GET'])
def success():
  print "Got post info"
  # recall the name attributes we added to our form inputs
  # to access the data that the user input into the fields we use request.form['name_of_input']
  return render_template('success.html')

app.run(debug=True)
