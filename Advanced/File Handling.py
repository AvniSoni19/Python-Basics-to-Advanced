""" open()

'r'= Read
'a'= Append
'w'= Write
'x'= Creating

't'= to open a file in text mode
'b'= opens a file in binary mode
"""

f=open('File Handling.txt')
#The statement on line 3 is equals to the statement on line 5
f=open("File Handling.txt",'rt')

print(f.read())

f=open("File Handling.txt",'r')
print(f.read(15))

f=open("File Handling.txt",'r')
print(f.readline())
print(f.readline())
print(f.readline())


f=open("File Handling.txt",'r')
list1=f.readlines()
print(list1[0])
print(list1[1])
print(list1[2])
print('\n'.join(list1))
print(list1[0][6:])

f=open('File Handling.txt','r')
for x in f:
    print (x)

f=open('File Handling.txt','a')
f.write("\nLast Line added explicitly")
f.close()

f=open('File Handling.txt','r')
print(f.read())

with open ('File Handling.txt','r+') as f : # '+' for updation
    d=f.readlines()
    f.seek(0)
    for i in d:
        if i != "Last Line added explicitly":
            f.write(i)
    f.truncate()

f=open("File Handling.txt",'r')
print(f.readlines())

print(f.tell())
print(f.seek(10))


