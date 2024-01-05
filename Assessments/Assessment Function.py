#Warmup Section

'''Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
'''
def even_function(a,b):
    if (a%2==0 and b%2==0):
        if a>b:
            return b
        else:
            return a
    if ((a%2!=0 and b%2==0) or (a%2==0 and b%2!=0) ):
        if a>b:
            return a
        else:
            return b
            
print(even_function(2,8))


'''Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False'''

def animal_crackers(n):
    x=n.split(" ")
    if (x[0][0]==x[1][0]):
        return True
    else:
        return False
text='Crazy Kangaroo'
print(animal_crackers(text))
print("\n")


'''Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False'''
def numbers(m,n):
    if (m+n==20 or m==20 or n==20):
        return True
    else :
        return False
print(numbers(20,10))
print(numbers(12,8))
print(numbers(2,3))


#Level 1 Problems
'''Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald'''
def old_macdonald(name):
    new_macdonald=name[0].upper()+name[1:3]+name[3].upper()+name[4:]
    return new_macdonald
print(old_macdonald('macdonald'))


"""Given a sentence, return a sentence with the words reversed
    master_yoda('I am home') --> 'home am I'
    master_yoda('We are ready') --> 'ready are We'"""
def master_yoda(n):
    n=n.split()
    n=n[::-1]
    n=" ".join(n)
    return n
print(master_yoda('I am home'))
print(master_yoda('Are we ready for the picnic? '))


"""Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True"""

def almost_there(n):
    n=abs(n) #Makes number positive or absolute, whether it is negative or positive
    if (90<=n<=110 or 190<=n<=210):
        return True
    else:
        return False
    
print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
print("\n")

#Level 2 Problems
'''Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False'''

def has_33(n):
    for i,j in enumerate(n):
       
            if (j==3):
                if (n[i+1]==3):
                   return True
                else:
                   return False    
        
            
print(has_33([1,3,3]))
print(has_33([1,3,1,3]))
print(has_33([3,1,3]))
print(has_33([3,3,4,5]))


"""Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'"""
def paper_doll(text):
    x=[]
    for i in (text):
        y=(i*3)
        x.append(y)
        z="".join(x)
    return z
def paperdoll(text):
    res=''
    for i in text:
        res += i*3
    return res
print(paper_doll("Hello"))
print(paperdoll("Mississippi"))