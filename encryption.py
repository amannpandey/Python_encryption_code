message=input('enter the massage:')     #hello
alphabet='abcdefghijklmnopqrstuvwxyz'
key=7
encrypt=''
decrypt=''
for i in message:
    position=alphabet.find(i)
    newposition=(position+5)%26         #26%26=0
    encrypt+=alphabet[newposition]
print(encrypt)

for i in encrypt:
    var=alphabet.find(i)
    newvar=(var-5)%26               #26%26=0
    decrypt+=alphabet[newvar]
print(decrypt)
