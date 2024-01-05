from collections import Counter
lst=[1,3,4,5,7,4,2,5,7,9,7,5,6,8,9,5,3,2,4,5,7,8,9,7,5,3]
print(Counter(lst))

c=Counter("Asdgfjryuwtavxnkgirtywqrasfxbggodksrsdfwe")

d=c.most_common(3)
print(d)

from collections import defaultdict
d={}
d1=defaultdict(object)
print(d1['one'])

for i in d1:
    print(i)

    


