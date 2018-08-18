from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'bobdobalina'

@app.route('/')
def index():
  list_of_dicts = [
    {
      'first_name': 'Jeremy',
      'favorite_fruit': 'Mango',
      'favorite_instrument': 'saxophone',
      'favorite_language': 'Python'
    },
    {
      'first_name': 'Alex',
      'favorite_fruit': 'Apple',
      'favorite_instrument': 'drums',
      'favorite_language': 'Javascript'
    },
    {
      'first_name': 'Anika',
      'favorite_fruit': 'Banana',
      'favorite_instrument': 'Flute',
      'favorite_language': 'Python'
    }
  ]
  print "Hello! You've reached the index route!"
  return render_template('index.html', title="Form test", jinj_list=list_of_dicts)

@app.route('/process_form', methods=['POST'])
def process():
  print  "*" * 80
  print "Got Post Info!  processing..."
  print request.form['first_name'], request.form['favorite_fruit'], request.form['favorite_instrument'], request.form['favorite_language']
  # return redirect('/')
  return redirect('/')

@app.route('/other')
def other():
  return render_template('other.html', title="Dictionary Demo")

app.run(debug=True)
