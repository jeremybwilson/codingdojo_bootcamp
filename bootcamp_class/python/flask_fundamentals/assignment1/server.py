from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'bobdobalina'

@app.route('/')
def index():
  print "*" * 80
  print "Hello! You've reached the index route!"
  return render_template('index.html', title="Home")

@app.route('/ninjas')
def ninjas():
  list_of_ninjas = [
    {
      'ninja': 'Yoshida',
      'weapon': 'Shuriken',
      'uniform_color': 'black',
    },
    {
      'ninja': 'Tetsuo',
      'weapon': 'Ninjato',
      'uniform_color': 'Blue',
    },
    {
      'ninja': 'Akira',
      'weapon': 'Kakute',
      'uniform_color': 'black',
    }
  ]
  print "*" * 80
  print "Hello! You've reached the Ninja route!"
  return render_template('ninjas.html', title="Ninjas", ninja_list=list_of_ninjas)

@app.route('/dojos/new')
def dojos():
  print "*" * 80
  print "This is the Dojos page"
  return render_template('dojos.html', title="Dojos")

@app.route('/users', methods=['POST'])
def show_user_profile():
  print "Got post info"
  print "*" * 80
  # recall the name attributes we added to our form inputs
  # to access the data that the user input into the fields we use request.form['name_of_input']
  # session['username'] = request.form['username']
  # session['email'] = request.form['email']

  return redirect('/success')

app.run(debug=True)
