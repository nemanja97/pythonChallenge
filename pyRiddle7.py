# Start URL = http://www.pythonchallenge.com/pc/def/channel.html
# We are getting a zip file from : http://www.pythonchallenge.com/pc/def/channel.zip

import zipfile

inFile = zipfile.ZipFile('channel.zip') # creating an object for the zip file
num = '90052'
end = '.txt'
cmt = '' # comment section of the zip contents
while True:
    try:
        text = inFile.read(num + end)
    except:
        break
    cmt += inFile.getinfo(num + end).comment
    print text

    num = ''
    for i in range(-1,(len(text)*-1),-1):
        if text[i].isdigit() == True:
            num += text[i]
    num = num[::-1]

print cmt

# End URL: http://www.pythonchallenge.com/pc/def/oxygen.html