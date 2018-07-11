
# coding: utf-8

# In[12]:

#Name: Chloe Xie
#Exercise: 2
#Date: 07/19/16
#Collaborators:
#Exercise_2
#Strings + concatenations + datatype conversion + Indexing + Library Functions + Lists


##########################################
# (A)
##########################################

#Use len() to find the length of the following strings and print it

string1 = "cryptography"
string2 = "Am I doing this right?"
string3 = "whatAboutThis?"
string4 = "BuCodeBreakers2016!!!"

print (len(string1))
print (len(string2))
print (len(string3))
print (len(string4))
#Does the length function ignore or count spaces?
#Answer: 
#it counts
#Does length work on integers? Try it out below to see.
#Answer:
#print (len(5))
#No it doesn't work. Len only works on strings

##########################################
# (B)
##########################################

#Create a list with 5 integers
x = [1,2,3,4,5]
print (x)


##########################################
# (C)
##########################################

#Create an empty list and append 5 strings

s = []
s.append('vaporeon')
s.append('jolteon')
s.append('flareon')
s.append('weepinbell')
s.append('geodude')
print(s)

##########################################
# (D)
##########################################

#Using the format of the example string, mmddyyyy, assign you birthday to a variable. 
#Use indexing and conversion to separately print the month, day and year.

example_string = "01012001"
bday = "1102000"
month = bday[:2]
print ("Month is " + month+ ".")
day = bday[2:4]
print("Day is " +day + ".")
year = bday[-4:]
print ("Year is " +year + ".")

##########################################
# Bonus
##########################################

#Figure out how to add these 2 strings together and print the result
#There are multiple ways to attempt this question

a = [1,2,3]
b = [5,6,7]

c = a+b
print (c)
#second method
#there's nothing here my b
a.append(b)
print (a)
##########################################
# Bonus2
##########################################

#Try to get as many different python errors as possible
#Record them down somewhere
"""e=str(b)
f= str(a)
d = f.append(e)
print (d)"""
#g = [ddkdkd,1,h6]
"""g= [5]
g[10]"""
#print (4/0)
"""cashmoney"""
