#Sets are ordered collection of data
x=set("Whatsapp")
print(x)
y={3,6,5,8,2,4,6,7,8}
print(type(x))
print(type(y))
print(y)
x.add(200)
x.add(100)
x.add(300)
print(x)
x.add(100)
print(x) #Set always contains unique elements

lst=[1,4,3,7,4,2,8,4,6,5,9,7,6,9,2,1,3,4,8,0,]

t=set(lst)
print(t)

A={3,7,6,5,1,4}
B={6,8,1,3,5,0,6}
print(A|B)#union
print(A&B)#intersection
print(A-B) #Difference of sets
print(B-A) #Difference of sets
print(A^B,end="$")#Symmetric Difference, in this difference the common elements in both the sets are omitted and rest of the elements of both the sets are printed