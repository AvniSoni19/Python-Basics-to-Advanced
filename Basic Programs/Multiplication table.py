def table(a):
    for i in range(1,11):
        print("{} x {} = {}". format(a,i,a*i))

n=int(input("Enter a number:\n"))
table(n)