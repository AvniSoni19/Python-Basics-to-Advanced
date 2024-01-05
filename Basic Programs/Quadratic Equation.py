x=int(input("Write the coefficient of x square:\n"))
y=int(input("Write the coefficient of x:\n"))
z=int(input("Write the constant:\n"))

def D(a,b,c):
    d=(b*b)-(4*a*c)
    global q
    q=d**0.5
    return q

def first_root(a,b,h):
    i=(-b+q)/(2*a)
    return i

def second_root(a,b,h):
    j=(-b-q)/(2*a)
    return j

D(x,y,z)
print("First root is {}  \n".format(first_root(x,y,q)))
print("Second root is {}  \n".format(second_root(x,y,q)))
