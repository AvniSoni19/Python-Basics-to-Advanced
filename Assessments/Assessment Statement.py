#Use for, split() and if to create a statement that will print out words that start with 's'
st="Print only those words that start with s in this sentence"
s_words=st.split()
print(s_words)
for i in s_words:
    if (i[0]=='s'):
        print(i)
    else:
        continue
"""In a short way"""
s="Print only those words that start with s in this sentence".split()
s_words=lambda x: x[0]=='s' 
s=list(filter(s_words,s))
print(s)



#Use range() to print all the even numbers from 0 to 10:
for i in range(0,11):
    if (i%2==0):
        print (i)
    else:
        continue
"""In a short way"""
i=[x for x in range(0,11) if x%2==0 ]
print(i)


#Use a list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
div_3=[x for x in range(0,50) if x%3==0]
print(div_3)


#Go through the string below and if the length of a word is even print "even!"
st='Print every word in this sentence that has an even number of letters'.split()
for i in st:
    if (len(i)%2==0):
        print (i)
print("These are the words with even number of letters")
"""In a short way"""
even_check =lambda x : "even" if len(x)%2==0 else x
even=lambda x: len(x)%2==0
even_words=list(filter(even,st))
st=list(map(even_check,st))
print(st)
print(even_words)


#Write a program that prints the integer from 1 to 100. But for multiples of three print"Fizz" instead of the number and for the multiples of five print "Buzz" For numbers which are multiples of both three and five print"FizzBuzz"
for i in range(1,101):
    if (i%3==0 and i%5==0 ):
        print("FizzBuzz")
    elif (i%5==0):
        print("Buzz")
    elif (i%3==0):
        print('Fizz')
    else:
        print(i)

#Use list comprehension to create a list of the first letters of every word in the sttring below:
st="Create a list of the first letters of every word in this string".split()
st_lst=[x[0] for x in st]
print(st_lst)