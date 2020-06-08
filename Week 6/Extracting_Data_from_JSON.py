import urllib.request, urllib.error
import json

url = input('Enter location: ')
print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
res= sum([ int(comment['count']) for comment in info['comments']])
print(res)


## Testcases
# for url = http://py4e-data.dr-chuck.net/comments_42.json
# result is 2553