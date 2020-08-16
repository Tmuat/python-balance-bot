import os

creds_path = os.path.expanduser('~/Desktop/Python/')

username = 'tmuat1'
password = open(creds_path + 'bfpass.txt').read()
apikey = open(creds_path + 'bfapi.txt').read()
