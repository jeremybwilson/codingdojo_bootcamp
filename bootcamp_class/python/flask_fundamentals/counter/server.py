from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'bobdobalina'

@app.route('/')
def index():

  if 'session_count' not in session:
    session['session_count'] = 1
  else:
    session['session_count'] += 1

  print "*" * 60
  print "Session count is at: ", session['session_count']
  print session

  return render_template("index.html", title="Count")

@app.route('/add_count', methods=['POST'])
def count():

  session['session_count'] += 1
  # session['session_count'] = request.form['some_value']

  print "*" * 60
  print "Session count is at: ", session['session_count']
  print session

  return redirect('/') # redirects back to the '/' route


@app.route('/clear')
def clear():
  session.clear()

  # if 'session_count' not in session:
  #   session['session_count'] = 1

  return redirect('/')

app.run(debug=True)