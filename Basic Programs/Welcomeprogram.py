a=input("Name?")
print("Welcome to Visual Code Studio, "+ a + "!" )
print("Now lets perform some basic mathematical calculations\n")
math=input("Are you interested?")
if math =='yes' or math == 'Yes':
    a,b,c,d,e=map(int,input("Enter five numbers:").split())
    num=[a,b,c,d,e]
    print (type(a)) 
    sum=a + b + c + d + e
    strsum=str(sum)
    print("Sum is :\n"+strsum)
    avg=sum/5
    print("Average of the given numbers is:\n"+str(avg))
else:
    print("No problem, Goodbye!")