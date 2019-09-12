from urllib.parse import urlencode 
from urllib.request import Request, urlopen

url			= 'https://vuldb.com/?api'									#url endpoint
post_fields	= { 'apikey': '[your_personal_api_key]', 'recent': '10' }	#request

request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)
