#!/usr/bin/env python3

'''
    vuldb_api_demo - Python VulDB API Demo
    
    License: GPL-3.0    
    Required Dependencies: requests, argparse, json
    Optional Dependencies: None
'''

import requests
import argparse
import json

# Define arguments for API script
parser = argparse.ArgumentParser()
parser.add_argument('--recent', dest='recent', default=5, type=int, help='It is possible to show the most recent entries with the request method recent. The method itself demands a number of entries which shall be shown.')
parser.add_argument('--details', dest='details', default=0, type=int, help='The field details is 0 or 1 and declares if the results are basic or detailed. This difference influences the API credit consumption.')
parser.add_argument('--id', dest='id', help='It is very simple to request the details for a vulnerability entry. The argument demands a VulDB Id.')
args = parser.parse_args()

# Add your personal API key here
personalApiKey = ''

# Set HTTP Header
userAgent = 'VulDB API Advanced Python Demo Agent'
headers = {'User-Agent': userAgent, 'X-VulDB-ApiKey': personalApiKey}

# URL VulDB endpoint
url = 'https://vuldb.com/?api'

# Choose the API call based on the passed arguments
# Default call is the last 5 recent entries
if args.recent is not None:
	postData = {'recent': int(args.recent)}
elif args.id is not None:
	postData = {'id': int(args.id)}
else:
	postData = {'recent': 5}

if args.details is not None:
	postData['details'] = int(args.details)

# Get API response
response = requests.post(url,headers=headers,data=postData)

# Display result if evertything went OK
if response.status_code == 200:

	# Parse HTTP body as JSON
	responseJson = json.loads(response.content)
	
	# Output
	for i in responseJson['result']:		
		print(i['entry'])
		#print(i["entry"]["id"])
		#print(i["entry"]["title"])