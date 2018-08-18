from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'bobdobalina'
# import library for date/time information
from datetime import datetime
# must import python function random 
import random

@app.route('/')
def index():
  return render_template('index.html', title="Ninja Gold")

@app.route('/process_money', methods=['POST'])
def income():
  try:
    temp = session['activities']
  except KeyError:
    temp = []

  form = request.form
  loc = form['location']
  location_map = {
    'cave': random.randint(3,7),
    'house': random.randint(2,5),
    'farm': random.randint(7,15),
    'casino': random.randint(-50,50)
  }

  print loc
  print location_map[loc]
  curr_gold = location_map[loc]
  date_time = datetime.now().strftime("%H:%m:%p on %d/%m/%y")

  if not 'gold' in session:
    session['gold'] = curr_gold
  else:
    session['gold'] += curr_gold

  if curr_gold > 0:
    message = {
      'class': 'green',
      'content': 'You won {} gold at {} at {}'.format(curr_gold, loc, date_time)
    }
    # won = True
  else:
    message = {
      'class': 'red',
      'content': 'You lost {} gold at {} at {}'.format(curr_gold, loc, date_time)
    }
  # won = False
  if not 'activities' in session:
    session['activities'] = [message]
  else:
    # session['activities'].append(message)
    session['activities'].insert(0, message)
    session.modified = True
    print date_time

  return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
  session.clear()
  return redirect('/')

app.run(debug=True)