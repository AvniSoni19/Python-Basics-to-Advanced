lst=[]
total=0
n=int(input("How many numbers you want to add?"))
for i in range(0,n):
    e=int(input("Enter Number {}  \n".format(i+1)))
    lst.append(e)
    total=total+e

print("The numbers you entered are: {}".format(lst))
print("Sum of the entered number is: {}".format(total))