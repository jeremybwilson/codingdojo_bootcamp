from flask import Flask, render_template, redirect
app = Flask(__name__)
app.secret_key = 'bobdobalina'

@app.route('/')
def index():
  print "*" * 60
  print "Hello! You've reached the index route!"

  # try:
  #   session['ninja']
  # except KeyError:
  #   session['ninja'] = ''

  # if not 'ninjas' in session:
  #   session['ninjas'] = 'No ninjas here!'
  return render_template('index.html', title="Disappearing Ninja")

@app.route('/ninja')
def ninja():
  print "*" * 60
  print "Hello! You've reached the ninja display route!"

  return render_template('ninjas.html', title="Ninja page")

@app.route('/ninja/<color>')
def ninja_color(color):

  if color == 'blue':
    template_to_render = 'leo.html'
  elif color == 'orange':
    template_to_render = 'michel.html'
  elif color == 'purple':
    template_to_render = 'dona.html'
  elif color == 'red':
    template_to_render = 'raph.html'
  else:
    template_to_render = 'not.html'

  ninja_map = {
    'purple': 'donatello.jpg',
    'blue': 'leonardo.jpg',
    'orange': 'michaelangelo.jpg',
    'red': 'raphael.jpg'
  }
  # for some_key, some_value in ninja_map.iteritems():
  #   print "My" + " " + str(some_key) + " " + "is" + " " + str(some_value)
  #   session['color'] = str(some_key)
  #   session['image'] = str(some_value)

  # if color in ninja_map:
  #   to_send_color = ninja_map[color]
  # else:
  #   to_send_color = "notapril.jpg"

  return render_template(template_to_render)

@app.route('/clear')
def clear():
  session.clear()
  return redirect('/')

app.run(debug=True)