import time
def func_one(n):
    return [str(num) for num in range(n)]

func_one(10)
start_time=time.time() #Staring time
res=func_one(10000000)
end_time=time.time() - start_time #give end time and time elapsed

print(end_time)