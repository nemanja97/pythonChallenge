# Start URL = http://www.pythonchallenge.com/pc/def/peak.html
# Peak Hell = 'pickle' and banner.p are used
# banner.p represents the data stream
# pickle represents the module

import urllib, pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
urllib.urlretrieve(url,'pickle.txt')
data = open('pickle.txt', 'r+')
contents = data.read()
unpickled = pickle.loads(contents)
for line in unpickled:
    print ''.join(elements[0] * elements[1] for elements in line)

for line in unpickled:
    print line

# End URL = http://www.pythonchallenge.com/pc/def/chanell.html