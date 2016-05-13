#!/bin/python
import requests

# Add your full token here
token = '12345'

# Take the base URL and then add the token to it
url = 'https://locals.seiu.org/api/v1/jobs/token/'
fullurl = url + token

# Make the actual GET request
r = requests.get(fullurl)

# Echo back the JSON response
print r.text
