#!/bin/python
import requests

token = '12345'

# this should stay the same
url = 'https://locals.seiu.org/api/v1/jobs/token/'
fullurl = url + token

r = requests.get(fullurl)

print r.text
