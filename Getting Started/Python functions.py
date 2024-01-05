nam="Avni"
def return_hello(x):
    print(f'Hello {x}')
return_hello("Avni")


def check_even(n):
    return n%2==0
print(check_even(35))

def even(n):
    m=[x for x in n if x%2==0]
    return m
n=[2,5,7,3,4,9,0,6,8,3,4,5,0,10,1,3,4]
print(even(n))
#OR
def even_chk(z):
    e=[]
    o=[]
    for i in z:
        if i%2==0:
            e.append(i)
        else:
            o.append(i)
    return e,o
print(even_chk(n))


def even_lst(b):
    for i in b:
        if i % 2==0:
            print(f"{i} = even")
        else:
            print(f"{i} = odd")
even_lst(n)