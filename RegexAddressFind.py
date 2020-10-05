import re
from address import addressList
from addressRegex import regex

new_path = 'C:/Users/GulinDogan/Desktop/AddressNote.txt'
new_address = open(new_path,'w', encoding="utf-8")

for string in addressList:

    new_address.write(string +'\n')
    print("adress:",string)

    for Regex in regex:
        match = re.findall(Regex, string)

        if match is not None:  
            new_address.write(str(match) + '\n')
            print(match)
        else:
            print ("No match")

new_address.close()