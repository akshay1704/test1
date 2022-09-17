#using socket
'''
import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()
'''
#using request-response
'''
from textwrap import indent
import requests
import json

url = 'https://api.pushshift.io/reddit/search/submission'
filter1 = {'subreddit' : 'pushshift', 
            'size' : 2
}

response = requests.get(url,filter1)

data = response.json()['data']
f = open("file1.txt",'w')
f.write(json.dumps(data,indent=4))

print(data)
'''
#using regex and urllib
'''
import urllib.request, urllib.parse, urllib.error
import re

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    line = line.decode().rstrip()
    st = re.findall('a.*?d',line)
    if len(st) == 0 : continue
    print(st)
'''

import json
import requests

response = requests.get('http://35.193.99.196:8983/solr/mycol1/schema/')
print (response.content)  
data = response.json()
f = open("file1.txt",'w')
f.write(json.dumps(data,indent=4))  
    
