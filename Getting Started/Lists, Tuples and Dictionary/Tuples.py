#As lists are mutable and tuples are immutable, so to make some data safer which does not need to be edited in future for example the calendar once made does not need to be edited later in such case tuples are used instead of lists.

t=(1,4,3,1,"Hello",5,1)

print(type(t))

print(len(t))

print(t[0])

print(t.index(3))

print(t.count(1))

#nested tuple
a=(1,("Avni"),4,"Here")
print(a)

b=(1,5,3,6)
print(a+b)