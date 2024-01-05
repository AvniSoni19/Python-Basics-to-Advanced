import random
print(random.randint(0,100))
print(random.random()) #for float
print(random.randrange(1,11,2)) #for odd numbers
from random import shuffle
list1=[1,2,3,4,5,6,7,8,9,10]
shuffle(list1)
print(list1)
list1.sort()


print(list1)
random.seed(101) #Seed is something that gives the same random number all the time as 101 seed always gives 74 random integer
print(random.randint(0,100))

l1=[3,6,7,9,1,3,4,7,5]
print(random.choices(l1,k=2))#with replacement
print(random.sample(l1,k=3))#without replacement
print(l1)
