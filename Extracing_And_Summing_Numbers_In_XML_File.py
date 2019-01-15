import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

string = ''
total = 0

fhand = open('File.xml')

for line in fhand:
	input = line.rstrip()
	string = string + input
tree = ET.fromstring(string)
lst = tree.findall('.//comment')

for item in lst:
	total = total + int(item.find('count').text)
print('Total of Numbers in your XML File is:', total)