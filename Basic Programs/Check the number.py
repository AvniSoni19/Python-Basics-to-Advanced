def check(a):
    if a>0:
        print("The number you have entered is Positive!")
    elif a<0:
        print("The number you have entered is Negative!")
    else:
        print("The number you have entered is neither positive nor negative!")

n=int(input("Enter a number:\n"))
check(n)