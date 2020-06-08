# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
print(sum(
            [int(tag.contents[0]) for tag in tags]
))

## Testcases
# 1. input: "http://py4e-data.dr-chuck.net/comments_42.html"
#    output: 2553
# 2. input: "http://py4e-data.dr-chuck.net/comments_189813.html"
#    output:2430