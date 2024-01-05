square= lambda num: num**2
#before colon(:)value used as input to function
#after colon(:)value to be returned based on operation

print(square(113))

m=list(map(lambda x: x**0.5,[4,9,16,36]))
print(m)

n=list(filter(lambda y: y[0]=='s',['shreya','please','start','after','tying','your','shoe','lace']))
print(n)

even_num=lambda x:'even' if len(x)%2==0 else x 
lst=['avni','riyanshi','yashika','vanshika','khushi']
m=list(map(even_num,lst))
print (m)