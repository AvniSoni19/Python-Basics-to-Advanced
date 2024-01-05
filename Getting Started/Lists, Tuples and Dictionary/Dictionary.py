my_dict={"Apple":12,"Banana":8,"Mango":14,"Orange":7} #Create a dictionary

print(type(my_dict)) #Check the type 

print(my_dict.keys()) #Print all the keys

print(my_dict.values()) #Print all the values

print(my_dict.items()) #Print all the items in the dictionary

print(len(my_dict.items())) #Number of pairs in the dictionary

my_dict["Apple"]=10 #Updating the value of a particular key

print(my_dict.items()) #Check the previous operation

print(type(my_dict["Apple"])) #Check the type of a value of a particular key and can also apply operations accordingly (ex. if string, we can also use the len function)

my_dict['Cherries']= my_dict.pop("Banana") #Updating keys

print(my_dict) #Check the previous operation

my_dict["Banana"]=3 #Adding a new pair

print(my_dict) #Check the previous operation

del my_dict["Apple"] #Deleting a pair using del function

print(my_dict) #Check the previous operation

print(my_dict.items()) #Check the previous operation

print(my_dict['Banana']) 

we=list(my_dict)

print(type(we))

print (we)

#Nested Dictionary
dict1={"Nested":{"Dictionary":{"is":{"Somewhat":{"Shown":{"Here"}}}}}}
a=dict1["Nested"]
b=dict1["Nested"]["Dictionary"]
c=dict1["Nested"]["Dictionary"]["is"]
d=dict1["Nested"]["Dictionary"]["is"]["Somewhat"]
e=dict1["Nested"]["Dictionary"]["is"]["Somewhat"]["Shown"]
print(a)
print(b)
print(c)
print(d)
print(e)