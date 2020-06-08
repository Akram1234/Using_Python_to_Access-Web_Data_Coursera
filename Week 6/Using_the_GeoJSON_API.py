import urllib.request, urllib.parse, urllib.error
import json

service_url = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42
address= input('Enter location: ')

parms={
    'address': address,
    'key'   : api_key
}

url = service_url + urllib.parse.urlencode(parms)
print('Retrieving', url)

uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)

print(js['results'][0]['place_id'])


### Testcases
## Testcase 1
# for "South Federal University" location as input
# the place_id would be ChIJ9e_QQm0sDogRhUPatldEFxw
## Testcase 2
# for "Faculdade de Tecnologia do Estado de Sao Paulo" location as input
# the place_id would be ChIJdeuBi19YzpQRhNYX7o0VQrc
