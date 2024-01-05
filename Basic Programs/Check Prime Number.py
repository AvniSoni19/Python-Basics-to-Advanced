def prime_number(a):
    p=False #flag value
    if a==1:
            print("1 is neither prime nor composite")
    elif a>1:
        for i in range(2,a): #in range function the last value as in "a" is excluded

            if a%i==0:
              p=True
              break
        
        if p:
            print(a ,"is not a prime number!")
        else:
            print(a ,"is a prime number!")
    else:
        print("Sorry! its a negative number.")

n=int(input("Enter a positive number:"))
prime_number(n)

#SimpleWay
def prime(a):
    for i in range(2,a):
        if (a%i==0):
            print("Not prime")
    else:
        print("Prime")

n=int(input("Enter a number:"))
prime(n)