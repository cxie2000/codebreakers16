# Name: chloe
# Exercise: otp~~
# Date:7/26/16

import os # we type this so that we can use a function called os.urandom(n)
#NOTE: os.urandom(n) will produce n random bytes

###### PROBLEM 1

# Question: What is the largest possible value of ord?  The smallest?  Therefore,
# how many different characters (one "letter" of a string) are there in total?
#
# Answer:255. There's many in total

###### PROBLEM 2

# Write a function to turn any string into its ascii encoding.
# Make sure it returns (not prints) the answer.
def stringToAscii(string):
    yurp = []
    for x in string:
        yurp.append(ord(x))
    return yurp

print("Problem 2: These should return True")
print(stringToAscii("trees") == [116, 114, 101, 101, 115])
print(stringToAscii("1%9 '") == [49, 37, 57, 32, 39])

###### PROBLEM 3

# PART A:
# Question: What type is the output of your stringToAscii(string) function?
#
# Answer: It's an integer

# PART B: Write a function that turns the ascii encoding back to a string, using
# the library function "chr", which reverses "ord".

def asciiToString(ascii):
    yarg = ""
    for x in ascii:
        yarg = yarg + chr(x)
    return yarg# replace this!

print("Problem 3: These should return True")
print(asciiToString(stringToAscii("apple")) == "apple")
print(asciiToString([116, 114, 101, 101, 115]) == "trees")

###### PROBLEM 4

# PART A:
# Question: Write out the ascii encoding of "a" in binary, and 
# the ascii encoding of "d" in binary, then do the XOR
# operation to them and write out the answer in binary.  What is the 
# *decimal number* that corresponds to this binary number?
#
# Answer:
bird = ord("a")^ord("d")
print (bird)
# PART B:

# XOR the characters 'a' and 'd' together using the caret (^).
# Make sure you get the same thing as in part A.

##### PROBLEM 5
# Write a function that uses a for loop to XOR (^) every element of
# lists of ASCII numbers ascii1 and ascii2 (with equal length), puts 
# the result in a new list, and returns it
def xor(ascii1, ascii2):
    elist= []
    for x in range(len(ascii1)):
        z = ascii1[x]^ascii2[x]
        elist.append(z)
    return elist
print("Problem 5: these should be True")
print(xor(stringToAscii('asdf'), stringToAscii('1234')) == [80, 65, 87, 82])
print(xor(stringToAscii("sixteen-byte msg"), stringToAscii("16-byte string!!!")) == 
 [66, 95, 85, 22, 28, 17, 11, 13, 17, 13, 6, 12, 78, 10, 82, 70])

###### PROBLEM 6

# Using this function will get you a list of n random bytes (numbers 
# between 0 and 255 - how many binary digits does it take to represent 
# these?). Try it with a few different numbers! You don't have to write 
# anything new, just try calling getKey on several different inputs.
def getKey(n):
 return list(os.urandom(n))

###### PROBLEM 7

# Write the functions encrypt and decrypt.  Encrypt will convert the message from a
# string to ascii, then XOR it with the key and return the result.  Decrypt will
# XOR the ciphertext with the key, convert the result from ascii to a string,
# then return the result.

def encrypt(message, key):
    return xor((stringToAscii(message)),key)
def decrypt(ciphertext, key):    
    return asciiToString(xor(ciphertext, key))# replace this!

key = getKey(16)
message = "sixteen-byte msg"
ciphertext = encrypt(message, key)
print("Problem 7: This should look like gibberish (it should NOT say None):")
print(ciphertext)
print("Problem 7: This should be True:")
print(decrypt(ciphertext, key) == message)
