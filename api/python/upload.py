#!/bin/python
import requests
import base64
import pysftp
import os

'''
This script does a few things in order to upload a file via SFTP and then make the /upload/ call to the MAPP API:
 - base64 encodes your filename (this is required since the filename will be part of your API URL
 - SFTPs the file to SEIU
 - Assembles the full API call
 - Makes the API call and retrieves the returned JSON

The script does not do a few key things you should implement:
 - Error handling or TRY/EXCEPT statements
 - Logging
 - Securely storing/passing SFTP credentials and token
'''

# Your filename
file = 'myfile.txt'
filename = file.rstrip()

# Create the base64 of the filename
filenameenc = base64.b64encode(filename)
filebase64 = filenameenc.rstrip()

# Print these just for feedback to developer
print("Your filename is: " + filename)
print("The base64 encoded filename is: " + filebase64)

# FTP the file to SEIU
# It is never recommended to store credentials directly in code. You should use envvars or a lookup mechanism for this.
# pysftp also allows for ssh key authentication
os.chdir('_/PATH/TO/FILE/_')
seiuhost = 'localsftp.seiu.org'
seiuusername = '_MYUSERNAME_'
seiupassword = '_MYPASSWORD_'
seiuport = '*****'
with pysftp.Connection(seiuhost, username=seiuusername, password=seiupassword, port=seiuport) as sftp:
    sftp.chdir('/incoming')
    sftp.put(filename)
    sftp.close()

# Add your full token here - again, do not store this directly in code
token = '12345'

# Flow
flow = '1' # Values are 1 = Catalist+VAN / 2 = Catalist only

# Take the base URL and then assemble the rest from there
url = 'https://locals.seiu.org/api/v1/upload/file/'
fullurl = url + filebase64 + '/flow/' + flow + '/token/' + token

# Make the actual GET request
r = requests.get(fullurl)

# Echo back the JSON response
print r.text
