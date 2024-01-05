lst=['Apple',12,'Banana',10,'Grapes',20]

lst[1]=6

print(lst)

print(len(lst))

print(type(lst))

print(lst[2:])

print(lst[:4])

lst2=['Cherries',15,'Pomegranate',4]

print((lst+lst2)*2)

x="Done"

print(x*5)

print(lst2[2])

lst.append("Litchi")

print(lst)

lst.append(1000000)#Because litchi is my favorite

print(lst)

lst.pop(5)

print(lst)

lst2.pop()
#in pop function to delete the element youhave to mention the index of that element 
#in remove function you have to mention the name of the element
print(lst2)

ab=['a','t','e','j','q','b','y']

ab.reverse()

print(ab)

ab.sort()

print(ab)

#Nest Lists

list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]

matrix=[list1,list2,list3]

print(matrix)

print(matrix[2][1])

#del function
del lst2


for i in range(0,3):
    print(matrix[i])
    
lst.insert(1,"Hello")

print(lst)