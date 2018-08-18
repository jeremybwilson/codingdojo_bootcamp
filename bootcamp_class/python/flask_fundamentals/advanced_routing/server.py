from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'bobdobalina'

@app.route('/')
def index():
  print "Got Post Info"
  return render_template('index.html', title="Usernames")

@app.route('/users', methods=['POST'])
def show_user_profile():
  print "Got post info"
  print "*" * 80
  # recall the name attributes we added to our form inputs
  # to access the data that the user input into the fields we use request.form['name_of_input']
  session['username'] = request.form['username']
  session['email'] = request.form['email']

  return redirect('/success')


@app.route('/success', methods=['GET'])
def success():
  print "Got post info"
  # recall the name attributes we added to our form inputs
  # to access the data that the user input into the fields we use request.form['name_of_input']

  return render_template('users.html')

app.run(debug=True)
