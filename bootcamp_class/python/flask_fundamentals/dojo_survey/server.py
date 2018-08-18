from flask import Flask, render_template, request, redirect, session

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
  return render_template('index.html', title="Home")


@app.route('/process', methods=['POST'])
def show_result():
  print "*" * 60
  print "Got post info"
  # recall the name attributes we added to our form inputs
  # to access the data that the user input into the fields we use request.form['name_of_input']
  # if length of request.form name greater than zero

  if len(request.form['name']) > 0:
    session['name'] = {
      'color': 'default',
      'content': request.form['name']
    }
  else:
    session['name'] = {
      'color': 'red',
      'content': 'No name entered'
    }
  if session['location'] != '':
    session['location'] = {
      'color': 'default',
      'content': request.form['location']
    }
  else:
    session['location'] = {
      'color': 'red',
      'content': 'No location entered'
    }
  if session['language'] != '':
    session['language'] = {
      'color': 'default',
      'content': request.form['language']
    }
  else:
    session['language'] = {
      'color': 'red',
      'content': 'No language entered'
    }
  if len(request.form['comments']) > 0:
    session['comments'] = {
      'color': 'default',
      'content': request.form['comments']
    }
  else:
    session['comments'] = {
      'color': 'red',
      'content': 'No comments entered'
    }

  return redirect('/result')

@app.route('/result', methods=['GET'])
def success():
  print "*" * 60
  print "Got post info"
  # print session['name'], session['location'], session['language'], session['comments']

  # recall the name attributes we added to our form inputs
  # to access the data that the user input into the fields we use request.form['name_of_input']
  print session['name'], "\n", session['location'], "\n", session['language'], "\n", session['comments'], "\n"
  return render_template('result.html', title="Submitted Info")

app.run(debug=True)
