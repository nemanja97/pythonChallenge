# Start URL = http://www.pythonchallenge.com/pc/def/linkedlist.php
# We have to follow the chain

import urllib

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
# first number is - 12345
# second main sequence stats at 8022
# number that we stopped on 64834
# number that we stopped on 40253
number = '12345'

for count in range(1,4000):
    workingURL = url + number
    urllib.urlretrieve(workingURL,'book.txt')
    file = open('book.txt', 'r')
    contents = file.read()
    print contents
    number = ''
    for i in range(-1,(len(contents)*-1),-1):
        if contents[i].isdigit() == True:
            number += contents[i]
    number = number[::-1]

'''
Running after a while gives us:
----------------------------------
and the next nothing is 16044
Yes. Divide by two and keep going.
and the next nothing is 72758
'''

'''
After running for even more it gets us to:
-----------------------------------
and the next nothing is 82682
There maybe misleading numbers in the
text. One example is 82683. Look only for the next nothing and the next nothing is 63579
and the next nothing is 34098
'''

'''
Finally:
-----------------------------------
and the next nothing is 66831
peak.html
'''

# End URL: http://www.pythonchallenge.com/pc/def/peak.html