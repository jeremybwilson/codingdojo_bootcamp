import requests

address_1 = 'https://api.github.com/events'
address_2 = 'https://api.github.com/users/jeremybwilson/events'
address_3 = 'https://github.com/timeline.json'
address_4 = 'https://tutsplus.com/'

r = requests.get(address_1)
# print r.text

encoding = r.encoding     # returns 'utf-8'
print encoding
status_code = r.status_code  # returns 200
print status_code

# print requests.codes['temporary_redirect']
# print requests.codes.teapot
# print requests.codes['o/']


def handle_exception():
  try:
    res = requests.get(address_1,timeout=30)
  except requests.ConnectionError as e:
    print "OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n"
    print str(e)

  except requests.Timeout as e:
    print "OOPS!! Timeout Error"
    print str(e)

  except requests.RequestException as e:
    print "OOPS!! General Error"
    print str(e)

  except KeyboardInterrupt:
    print "Someone closed the program"

handle_exception()