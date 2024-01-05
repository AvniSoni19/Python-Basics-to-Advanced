def double(a):
    return a + a
def exponent(n):
    return n**5 

i,j,k,l,m=map(int,input("Enter 5 numbers").split())
num=[i,j,k,l,m]
print("Square of the given number is:\n")
sqresult=map(double,num)
print(list(sqresult))
print("5th exponential of the given number is:\n")
expresult=map(exponent,num)
print(list(expresult))
   
def sq(num):
    return num**2
lst=[3,6,5,8,9]
m=list(map(sq,lst))
