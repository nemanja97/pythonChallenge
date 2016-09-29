# Start URL = http://www.pythonchallenge.com/pc/def/map.html
# We need to solve the cypher by changing letter positions

# Checking by how much the letter position moves
print ord('M') - ord('K')
print ord('Q') - ord('O')
print ord('G') - ord('E')

# Default text
cypher = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp." \
         " bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle." \
         " sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

deciphered = []

# Changing letters
for i in range(0,len(cypher)):
    if cypher[i] == ' ' or cypher[i] == '.' or cypher[i] == "'" or cypher[i] == '(' or cypher[i] == ')':
        deciphered.append(cypher[i])
    elif ord(cypher[i])+2 > 122:
        deciphered.append(chr(ord(cypher[i])+2-(123-97))) # If it goes over 'z' we bring it around to 'a'
    else:
        deciphered.append(chr(ord(cypher[i])+2))

# Deciphered text
decipheredString = ''
for i in deciphered:
    decipheredString += i
print decipheredString

# Using it on start URL
decipheredURL = 'map'
deciphered = []
for i in range(0,len(decipheredURL)):
    if decipheredURL[i] == ' ' or decipheredURL[i] == '.' or decipheredURL[i] == "'" or decipheredURL[i] == '(' or decipheredURL[i] == ')':
        deciphered.append(decipheredURL[i])
    elif ord(cypher[i])+2 > 122:
        deciphered.append(chr(ord(decipheredURL[i])+2-(123-97))) # If it goes over 'z' we bring it around to 'a'
    else:
        deciphered.append(chr(ord(decipheredURL[i])+2))

# Deciphered URL
decipheredString = ''
for i in deciphered:
    decipheredString += i
print decipheredString
# End URL = http://www.pythonchallenge.com/pc/def/ocr.html