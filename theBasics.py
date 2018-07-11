# coding: utf-8

# In[ ]:

#Name: Chloe!
#Exercise: 3
#Date: 7/11/18
#Collaborators: 
#Exercise_3_Functions
#Booleans + Conditionals + Functions

##########################################
# (A)
##########################################

#Write a function, printWorld() that takes no inputs and prints “Hello World!”
def printWorld():
    print ("Hello World!")
#first define the function, remember to put empty brackets when there are no inputs


#now call the function
printWorld()    

##########################################
# (B)
##########################################

#Now write a function, multiply_by_2(n), that takes one integer input, multiplies it by 2 and prints the result

#function here
def multiply_by_2(n):
    y = n * 2
    print(y)

print("")
print("Multiply by 2")
multiply_by_2(2)
multiply_by_2(16)
multiply_by_2(225)
multiply_by_2(12143)
print("Answers should be: 4, 32, 450, 24286")

##########################################
# (C)
##########################################

#Now write a function, multiply_by_3(n), that takes one integer input, multiplies it by 2 and RETURNS the result
#print the result


#function here
def multiply_by_3(n):
    var = n*3
    return (var)

print("")
print("Multiply by 3")
print(multiply_by_3(3) == 9)
print(multiply_by_3(5) == 15)
print(multiply_by_3(125) == 375)
print(multiply_by_3(102934) == 308802)
print("All should be True")




##########################################
# (D)
##########################################

num = 5
#Use the previous 2 functions to multiply num by 36
#Do not use the asterisk (*) operator 




##########################################
# (E)
##########################################

#Write a function, multiply(n, m), that takes two integer inputs, n and m.
#Take n and multiply by m
#return the result
#print what the function returns 

def multiply(n,m):
    return n*m
print (multiply(3,4))

##########################################
# (F)
##########################################

#Write a Python program, equal_to_five(n), that accepts an integer n, and returns True if it is equal to 5
#Return False, if not equal

def equal_to_five(n):
    if n == 5:
        return True
    else:
        return False

##########################################
# Bonus 1
##########################################

#Write a Python function to find the Max of three numbers
#Remember to use if statements and == to compare values

def max_of_3(a,b,c):
    if (a > b) and (a > c):
        print (a)
    elif (b > a) and (b > c):
        print (b)
    else:
        print(c)
max_of_3(1,2,3)
max_of_3(124,122,1)


##########################################
# Bonus 2
##########################################

#Write a Python program, compare(n,m), that accepts an integer n
#if n is less than m, return  -  n "is less than" m
#if n is equal to than m, return  -  n "is equal to" m
#if n is more than m, return  -  n "is more than" m
#Be sure to use if, elif and else along with the proper boolean functions


def compare(n,m):
    if n < m:
        return (n + "is less than" + m)
    elif n == m:
        return (n + "is equal to" + m)
    else:
        return (n "is more than" m)
compare(12,4)

##########################################
# Bonus 2
##########################################


Chloe Xie <19xiec@wpsraiders.org>
7/20/16
to me 
# coding: utf-8

# In[ ]:

#Name:
#Exercise: 4
#Date: 
#Collaborators:
#Lists and For Loops

##########################################
# (A)
##########################################

#Write a for loop that prints out each individual letter of the following string on a new line.
#Remember to use len() to find the length of the string

word = "cryptography"
def letter(str):
    for i in range (len(str)):
        x = str[i] 
        print (x)
print (letter(word))
      
##########################################
# (B)
##########################################

#Write a Python program that reverses the following word. Print the whole reversed word together.
word2 = "cybersecurity"
x = len(word2)
t = ""
while (0<x<=13):
    s = (word2[x-1])
    t = t + s
    x = x - 1
print (str(t))



##########################################
# Lists
##########################################

#Here are some lists that you will use below. Do not change them.
a = [1,2,3,4,5,6,7,8,9,10]
b = [100,90,80,70,60,50,40,30,20,10]
c = [20,103,14,34,47,19,52,146,33,89]
d = [10,1,9,2,8,3,7,4,6,5]


##########################################
# (C)
##########################################

#Using loops, write a python function to sum all the items in a list. Do not use the sum() function.

def sum_of_list(list1):
    #write code here
    s = 0
    for x in list1:
        s = s + x
    return (s)# make sure you return something

    
#Tester
print(sum_of_list(a) == sum(a))
print(sum_of_list(b) == sum(b))
print(sum_of_list(c) == sum(c))
print(sum_of_list(d) == sum(d))
print("All should be True")


##########################################
# (D)
##########################################

#Using loops, write a python function to find the largest number in a list. Do not use the max() function

def max_num_in_list(list1):
    m = 0
    for x in list1:
        if (x >= m):
            m = x
            
        
        #write code here
    return (m)#make sure you return something


print("")
print("Largest Number:")

#Tester
print(max_num_in_list(a) == max(a))
print(max_num_in_list(b) == max(b))
print(max_num_in_list(c) == max(c))
print(max_num_in_list(d) == max(d))
print("All should be True")


##########################################
# (E)
##########################################

#Write a Python function that takes two lists and returns True if they have at least one common member

def common_list(list1, list2):
    for x in list1:
        m = x
        for y in list2:
            if m == y:
                return (True)
    return (False)

        #write code here
    return (y)#make sure you return something
    
print("")
print("Common Number:")

"""a = [1,2,3,4,5,6,7,8,9,10]
b = [100,90,80,70,60,50,40,30,20,10]
c = [20,103,14,34,47,19,52,146,33,89]
d = [10,1,9,2,8,3,7,4,6,5]"""    
#Tester
print(common_list(a,b) == True)
print(common_list(a,c) == False)
print(common_list(a,d) == True)
print(common_list(b,c) == True)
print(common_list(b,d) == True)
print(common_list(c,d) == False)
print("All should be True")


##########################################
# (F)
##########################################

#Write a Python function to find the index of an item of a specified list
#If the item is not in the list, return a string that says so
def find_index(list1,item):
    for x in list1:
        y = 0
        if list1[y] == item:
            return y
        else:
            y = y + 1
    return ("item not in list try again")        
                
        #write code here
#make sure you return something
    
print(find_index(a,2))
##########################################
# Bonus 1
##########################################

#Write a Python program to get the difference between the sum of two lists
#You may call other previously written functions (Hint: (C))
def find_diff(list1,list2):
    #write code here
    if sum_of_list(a) >= sum_of_list(b):
        return(sum_of_list(a) - sum_of_list(b))
    else:
        return(sum_of_list(b) - sum_of_list(a))
    
#make sure you return something
print (find_diff(a,b))

"""def sum_of_list(list1):
    #write code here
    s = 0
    for x in list1:
        s = s + x
    return (s)"""
