print([x for x in ("codequest") ])

print([x**2 for x in range(1,11)])

even_num= [x for x in range(11) if x%2==0] #for if condition do it after for loop
print(even_num)

x=[x+1 if x>5 else x-1 for x in range(11)] #if you are giving if, else condition use it before for loop
print (x)

temp_in_celcious=[5,10,20,5,43,9]
print([((9/5)*temp+32) for temp in temp_in_celcious])
