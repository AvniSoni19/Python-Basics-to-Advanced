x=35
def sample():
    x=50
    print(x)
    return x
sample()
print(sample())
print(x)

def simple():
    global x #when global is called in a function and then the changes made to that variable are the changes made globally.
    x=10
    return x
print(simple())
print(x)