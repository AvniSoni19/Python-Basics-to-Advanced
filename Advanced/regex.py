#regex, a shortform for regular expressions.
#A pattern to modify or shorten your code.

text="The person's phone number is +91-7697621658. Call soon!!"

print('phone' in text)

print('persons' in text)

import re
pattern='phone'
print(re.search(pattern,text))
print(text[12:17])

match=re.search(pattern,text)
print(match.start())
print(match.span())

txt="I am having a new phone and my friend is having an old phone"
print(re.search('phone',txt))
matches=re.findall('phone',txt)
print(len(matches))
print(matches)
a=[match.span() for match in re.finditer("phone",txt)]
print(a)

phone=re.search(r'\d\d-\d\d\d\d\d\d\d\d\d\d',text)
print(phone.group())
#or
phone=re.search(r'\d{2}-\d{10}',text)
print(phone.group())

#for multiple numbers
"""txt1="I am having a new phone 91-9926360338 and my friend is having an old phone 91-7697621658"
phno=re.findall(r'\d{2}-\d{10}',txt1)
print(phno.group())"""

t="A man just passed from here"
#when you are confused for a word
print(re.search(r'man|woman',t))

text="the cat in the hat sat hereasdfat sdfgat sdfhlrat"
print(re.findall(r"..at",text))

print(re.findall(r"\S+at",text))

text="This ends with 2"
print(re.findall(r"\d$",text))
text="1 is the number after 0"
print(re.findall(r"^\d",text))
print(re.findall(r"\d$",text))

text="This is a text! having a PUNCTUATION, how to remove it? ..."
punc=re.findall('[^!,.? ]+',text)
print(punc)
punc=" ".join(punc)
print (punc)

text1="do you like catfish?"
text2="do you have catdog?"
print(re.search(r"cat(fish|dog|claw)",text1))
print(re.search(r"cat(fish|dog|claw)",text2))

