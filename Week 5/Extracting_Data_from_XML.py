import urllib.request, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print("Retrieving", url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
res = sum([int(ele.find('count').text) for ele in tree.find('comments').findall('comment')])
print(res)

## Testcases
# 1. input "http://py4e-data.dr-chuck.net/comments_42.xml"
#    output 2553
# 2. input "http://py4e-data.dr-chuck.net/comments_189815.xml"
#    output 2490


