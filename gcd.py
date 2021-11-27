#Q1.you need to take input as number from the user and find out the greatest common divisor of those two number and save it in a C drive
# with the file name as g
def gcd(a, b):
    if b == 0:
       return a
    else:
        return gcd(b,a%b)
a=int(input("enter the first number"))
b=int(input("enter the second number"))
print(gcd(a,b))
























# Q4.write a python program to generate 26 text files named A.txt B.txt and so on upto Z.txt.

import string
alphabet=string.ascii_uppercase
for letter in alphabet:
 with open(letter+".txt",'w') as  file:
  file.write(letter)






