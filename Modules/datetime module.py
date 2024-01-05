import datetime

print(datetime.datetime.now())
#year,month,day,hour,minute,second,microsecond
#OR

x=datetime.datetime.now()
print(x.year)
print(x.month)
print(x.day)
print(x.date())
print(x.time())
print(x)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)



print(x.ctime())

d1=datetime.date(2020,3,21)
print(d1)



print(d1.strftime("%B"))

print(d1.strftime("%d/%B/%Y %A"))

print("Earliest time: ",datetime.time.min)
print("Latest time: ",datetime.time.max)

print("Earliest day: ",datetime.date.min)
print("Latest day: ",datetime.date.max)
