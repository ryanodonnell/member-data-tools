#!/bin/python
import requests

# Add your full token here
token = '12345'

# FileID
fileid = 'abcde'

# Take the base URL and then add the token to it
url = 'https://locals.seiu.org/api/v1/status/fileid/'
fullurl = url + fileid + '/token/' + token

# Make the actual GET request
r = requests.get(fullurl)

# Echo back the JSON response
print r.text
