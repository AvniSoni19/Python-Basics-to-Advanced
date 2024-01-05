s=set()
s.add(1)
s.add(14)

print(s)

s.clear()

print(s)

s={1,2,3,4}
c=s.copy()
print(s,c)

c={1,2,3,5,6}

print(s.difference(c))
print(c.difference(s))

s1={1,2,3}
s2={4,1,5}

print(s1.difference_update(s2))
print(s2.difference_update(s1))

s1.discard('1')
print(s1)

print(s1.intersection(s2)) #it returns a new set containing the intersecting elements

print(s1.intersection_update(s2))#s1 got updated with the intersecting elements of both te sets

print(s1.isdisjoint(s2))

print(s1.issubset(s2))
print(s2.issubset(s1))

print(s1.issuperset(s2))

print(s2.symmetric_difference(s1))

print(s1.union(s2))

