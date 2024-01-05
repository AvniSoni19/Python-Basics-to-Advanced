def leap_year(a):
    if a%4==0:
        print("The year is a leap year!")
    else:
        print("Umm..its a normal year having 365 days!")

n=int(input("Enter a year\n"))
leap_year(n)