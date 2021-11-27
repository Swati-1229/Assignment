
# Q4.write a python program to generate 26 text files named A.txt B.txt and so on upto Z.txt.

import string
alphabet=string.ascii_uppercase
for letter in alphabet:
 with open(letter+".txt",'w') as  file:
  file.write(letter)
