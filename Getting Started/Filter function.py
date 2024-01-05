def check_even(num):
    return num%2==0
nums=[1,2,3,4,5,6,7,8,9,10]
m=list(filter(check_even,nums))
print(m)