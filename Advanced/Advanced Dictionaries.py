#Dictionary Comprehension
a={x:x**2 for x in range(10)}
print(a)

print(a.keys())
print(a.values())
print(a.items())

b={'num '+str(i): j for i,j in a.items()}
print(b)
print(b.keys())
print(b.values())

b['num 5']=100
print(b)

words=['phy','chem','math','bio']
marks=[14,12,15,8]

res={i : j for i,j in zip(words,marks) if j>12 }
print (res)
    
