from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'bobdobalina'

@app.route('/')
def index():
  print "*" * 60
  if 'name' not in session:
    name = 'No name entered'
  else:
    name = session['name']

  if 'email' not in session:
    email = 'No email entered'
  else:
    email = session['email']

  print session
  print "Here is the name: ", name
  print "Here is your email: ", email

  return render_template("index.html", title="Form test", name=name, email=email)

@app.route('/users', methods=['POST'])
def create_user():
  print "*" * 60
  print "Got Post Info"
  # notice how the key we are using to access the info corresponds with the names
  # of the inputs from our html form
  form = request.form
  errors = []

  if name == 'No name entered': 
  # if session['name'] == 'No name entered':
  # if len(session['name']) > 0:
    session['name'] = {
      'color': 'red',
      'content': errors.append('No name entered')
    }
  else:
    session['name'] = {
      'color': 'default',
      'content': form['name']
    }
  if email == 'No email entered':  
  # if session['email'] == 'No email entered':  
  # if len(session['email']) > 0:
    session['email'] = {
      'color': 'red',
      'content': errors.append('No email entered')
    }
  else:
    session['email'] = {
      'color': 'default',
      'content': form['email']
    }
  print "Here is the session info from the /users route: ", session

  if len(errors) > 0:
    for error in errors:
      flash(error)
    return redirect('/') # redirects back to '/' route
  else:
    session['name'] = form['name']
    session['email'] = form['email']
    return redirect('/show') # redirects to the '/show' route


@app.route('/show')
def show_user():

  print session
  print "Here is the name: ", session['name']
  print "Here is your email: ", session['email']
  
  return render_template('user.html', title="Sessions", name=session['name'], email=session['email'])

@app.route('/clear')
def clear():
  session.clear()
  return redirect('/')

app.run(debug=True)