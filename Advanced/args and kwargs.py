#Useful inside a function
# *args accepts tuples of values inside the function
def myfunc(a,b):
    return sum((a,b))*.5

print(myfunc(10,20))

def my_func(*nums):# '*nums' by default takes the value in an inbuilt tuple
    return sum(nums)
print(my_func(10,20,30,40,50,60))

# **kwargs builds dictionary of key/values
def otherfunc(**foo):
    if 'fruit' in foo:
        print(f"My favorite fruit is {foo['fruit']} ")
    if 'beverage' in foo:
        print(f"My favorite beverage is {foo['beverage']}")
    if 'drink' in foo:
        print(f"My favorite drink is {foo['drink']}")
    else:
        print("I don't like anything")
otherfunc()
print("\n")
otherfunc(fruit='Mango',drink='Milk',beverage='Coffee')