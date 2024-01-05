#Write an equation that uses multiplication, division, an exponent, addition and subtraction that is equal to 100.25
x= (20*2)+(120/2)+(5.5**2)-30
print(x)

#Answer these three questions without execution
a=4*(6+5) #44
b=4*6+5 #29
c=4+6*5 #34
print(a,b,c)

#What is the type of the result of the expression 3+1.5+4 ?
print(type(3+1.5+4))#float

#What would you use to find a number's square root as well as its square?
sq=16**2 #Square
sqrt=16 **0.5 #Square root
print (sq,sqrt)

#Given the string "hello", give an index command that returns "e".
s="Hello"
print(s[1])

#Reverse the string "Hello" using slicing:
print(s[::-1])

#Given the string hello, give two methods of producing the letter "o" using indexing
print(s[4])#Method1
print(s[-1])#Method2

#Build this list[0,0,0] two seperate ways.
list1=[0,0,0]
#list2=

#Reassign 'Hello' in this nested list to say 'Goodbye' instead:
list3=[1,2,[3,4,'hello']]
list3[2][2]='Goodbye'
print(list3)

#Sort the list below:
list4=[5,3,4,6,1]
list4.sort()
print(list4)

#Using keys and indexing, grab the 'Hello' from the following dictionaries:
d={'simple_key':'hello'}
print(d['simple_key'])
d={'k1':{'k2':'hello'}}
print(d['k1']['k2'])
d={'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])
d={'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

#Use a set to find the unique values of the list below:
list5=[1,2,2,33,4,4,11,22,3,3,2]
s=set(list5)
print(s)

#Boolean statements
a=3
b=4
print(a==b)#False
print(a!=b)#True
print(a>b)#False
print(a<b)#True
print(a>=b)#False
print(a<=b)#True
print("\n")


print(2>3)#False
print(3<=2)#False
print(3==2.0)#False
print(3==3.0)#True
print(4**0.5!=2)#False
print("\n")

l1=[1,2,[3,4]]
l2=[1,2,{'k1':4}]
print(l1[2][0]>=l2[2]['k1'])#False