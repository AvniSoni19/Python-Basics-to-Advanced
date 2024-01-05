s="Hello all hope you all are good"
print(s.capitalize())

print(s.upper())

print(s.lower())

print(s.count("l"))

print(s.find("l"))

print(s.center(30,'*'))

s=s.replace('a','A',1)

p='good morning'
p=p.title()
print(p)

s=s.title()

print(s)

print(s.isalnum()) #if your statement is having even a space then it will return false

print(s.isalpha())

print(s.islower())

print(s.isspace())

print(s.istitle())

print(s.endswith('l'))

print(s.startswith("H"))

q=s.split(" ")
print(q)

print(" ".join(q))

print(s.partition('All')) #partition is always in tuple format

