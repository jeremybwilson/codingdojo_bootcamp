# import the library
import urllib2

# NOTE: there's a urllib version for each version of Python:
# Use urllib2 if you're using Python 2
# Use urllib3 for Python 3
# Finally, use it...

# req = urllib2.request.Request('http://python.org/')
# with urllib.request.urlopen(req) as response:
#    the_page = response.read()
# import urllib.request
 
# html = urllib2.urlopen('https://arstechnica.com').read()
# print(html)

request = urllib2.Request('http://www.python.org')
response = urllib2.urlopen(request)
the_page = response.read()