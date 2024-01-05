#Generators
def cube(n):
    for i in range(n):
        c = i**3
        print(c) 
cube(5)
def cubes(n):
    for i in range(n):
        yield i**3
for num in cubes(10):
    print(num)
   

#Iterators
def simple():
    for x in range(10):
        yield x
g=simple()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))