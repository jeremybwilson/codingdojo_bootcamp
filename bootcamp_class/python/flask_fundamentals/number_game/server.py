from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'bobdobalina'

import random
# imports python function random

@app.route('/')
def index():
  print "*" * 60
  print "Here is the session info:", session

  # initialize the target number
  # try: 
  #   session['target']
  # except KeyError:
  #   session['target'] = random.randint(0, 101)

  # generate correct result using randint method and add into session
  if 'correct' not in session:
    session['correct'] = random.randint(0, 101)

  # generate the result value and add into session
  if 'result' not in session:
    result = "no result"
  else:
    result = session["result"]

  # generate the guessed value and add into session
  if 'guessed' not in session:
    guessed = 'no guess'
  else:
    guessed = session['guessed']

  print "Here is the randomly generated value: ", session['correct']
  print "Here is the result", result
  print "Here is your guess", guessed

  return render_template('index.html', title="Great Number Game", result=result, guessed=guessed)

@app.route('/guess', methods=['POST'])
def guess_match():
  print "*" * 60
  # print "Here is the request.form info:", request.form

  # set session['guessed'] information that of the submitted form
  session['guessed'] = request.form['guess']
  # convert form data submitted into int and assign to 'guess' variable
  guess = int(request.form['guess'])
  # set session['correct'] information to 'correct' variable for comparison logic below
  correct = session['correct']
  print "We just guessed {} number is {}".format(guess, correct)

  if guess > correct:
    session['result'] = 'high'
  elif guess < correct:
    session['result'] = 'low'
  else:
    session['result'] = 'correct'

  return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
  session.clear()
  return redirect('/')

app.run(debug=True)