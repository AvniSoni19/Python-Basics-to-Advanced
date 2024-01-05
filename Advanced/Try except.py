'''
try:
    #Try some random code
except:
    #execute if error shown in try section
else:
    #It executes only when the try section runs
'''
def divide(x,y):
    try:
        result=x//y
        print(f"Your answer is {result}")
    except:
        print("You are dividing by zero, not possible :(")
    else:
        print(result)
divide(2,6)
divide(4,0)

y=[2,4,6,0,8]
for i in y:
    try:
        res=100/i
        print(res)
    except:
        print("Division with 0 is not possible :(")