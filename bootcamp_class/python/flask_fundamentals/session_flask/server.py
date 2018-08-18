from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

app.secret_key = 'bobdobalina'

@app.route('/')
def index():

  if 'ninja_count' not in session:
    session['ninja_count'] = 0

  print "Hello! You've reached the index route!"
  return render_template('index.html', title="Home")


@app.route('/ninjas/<color>')
def ninja(color):
  # print color

  if 'ninja_count' not in session:
    session['ninja_count'] = 1
  else:
    session['ninja_count'] += 1

  color_map = {
    'blue': 'raphael.jpg',
    'red': 'donatello.jpg'
  }
  if color in color_map:
    to_send = color_map[color]
  else:
    to_send = "default.jpg"

  return render_template('ninja.html', ninja=to_send)

@app.route('/clear')
def clear():
  session.clear()
  return redirect('/')

app.run(debug=True)