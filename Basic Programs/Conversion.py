#kg to miles
def kg_to_miles(k):
    m=k*0.621371
    return m

n=int(input("Enter value in kilometers :\n"))
print("Value in miles is : {}\n".format(kg_to_miles(n)))

#celsius to fahrenheit
def C_to_F(c):
    f=(c*(9/5))+32
    return f

h=int(input("Enter degree(s) of celsius: \n"))
print("Value in fahrenheit is : {}\n".format(C_to_F(h)))