# Q5. Write a Python program to combine each line from the first file with corresponding line in the
# second file and save it into the Third file.
data1=data2=""
with open("abc.txt") as file1:
    data1=file1.read()
with open("test.txt") as file2:
    data2=file2.read()
# data1=data1+"\n"
data1=data1+" "+data2

with open("file3.txt",'w') as file3:
    file3.write(data1)


