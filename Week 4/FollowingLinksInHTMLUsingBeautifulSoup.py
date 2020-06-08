# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
cnt = int(input('Enter count: '))
pos = int(input('Enter position: '))

for cnt_pos in range(cnt+1):
    print("Retrieving: "+url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[pos-1]['href']


## Testcases
# 1. input :
#           url : "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
#           count : 4
#           position 3
#    output : Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
#             Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
#             Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
#             Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
#             Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html
# 2. input:
#           url : "http://py4e-data.dr-chuck.net/known_by_Kristal.html"
#           count : 7
#           position 18
#    output:  Retrieving: http://py4e-data.dr-chuck.net/known_by_Kristal.html
#             Retrieving: http://py4e-data.dr-chuck.net/known_by_Luci.html
#             Retrieving: http://py4e-data.dr-chuck.net/known_by_Alasdair.html
#             Retrieving: http://py4e-data.dr-chuck.net/known_by_Mariyah.html
#             Retrieving: http://py4e-data.dr-chuck.net/known_by_Dalton.html
#             Retrieving: http://py4e-data.dr-chuck.net/known_by_Shani.html
#             Retrieving: http://py4e-data.dr-chuck.net/known_by_Lettice.html
#             Retrieving: http://py4e-data.dr-chuck.net/known_by_Rheanan.html
