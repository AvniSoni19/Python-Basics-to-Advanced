while True:
    
    n=input("Enter the Operation:\n '1' for Addition\n '2'for Subtraction\n '3'for Multiplication\n '4'for Division \n To exit press 'done':\n")
    
    sum=0 
    if (n=='1'):
       print("Enter input and if done, press 'd':")
       while True:
        i=input("\n")
        if (i=='d'):
            break
        i=int(i)
        sum=sum+i
       print("Total= {} ".format(sum))
    elif (n=='2'): 
       i,j=map(int,input("Enter the minuend and the subtrahend:\n").split())
       sub=i-j
       print("Difference= {}".format(sub))
    elif (n=='3'):
       i,j=map(int,input("Enter the multiplicand and the multiplier:\n").split())
       mul=i*j
       print("Result= {}".format(mul))
    elif (n=='4'):
       i,j=map(int,input("Enter the dividend and the divisor:\n").split())
       div=i/j
       print("Result= {}".format(div))
    elif(n=='done'):
       break
    else:
       print("Oops! Not Supported.")
       