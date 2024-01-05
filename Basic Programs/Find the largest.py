def largest(a,b,c):
    if a>b and a>c:
        print("{} is the largest!".format(a))
    elif b>a and b>c:
        print("{} is the largest!".format(b))
    elif a==b==c:
        print("All are equal and largest")
    else:
        print("{} is the largest!".format(c))
    
x,y,z=map(int,input("Enter three numbers: ").split())
largest(x,y,z)