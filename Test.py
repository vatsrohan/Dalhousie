##!/usr/bin/env python
## coding: utf-8
#
## In[3]:
#
#
#import math
#x = input("Enter a number of two digits:")
#y = math.sqrt(float(x))
#print(y)
#
#
## In[2]:
#
#
#x = int(input("Enter a number for checking:"))
#def check (x):
#    y = x [::-1]
#    return (x == y)
#z = check (x)
#print (z)
#
#
## In[8]:
#
#
#y = input("Enter a string:")
#v = ''.join(sorted(y))
#for x in v:
#    print (x)
#
#
## In[4]:
#
#
#import turtle
#a = turtle.Turtle()
#side = 30
#for j in range(side):
#    a.fd(10)
#    a.lt(360/side)
#    
#for j in range(side):
#    a.fd(10)
#    a.rt(360/side)
#
#a.fd(700)
#
#
## In[7]:
#
#
#d = { 'XS' : 'chini loda', 'S' : 'bone ka loda', 'M' : 'desi average', 'L' : 'Mota loda', 'XL'  : 'BBC'}
#x = input("Enter size in capitals")
#print("Size is {} ".format(d.get(x)))
#
#
## In[1]:
#
#
#i = 1
#while i < 6:
#  print(i)
#  i += 1
#else:
#  print("i is no longer less than 6 so we stopped")
#
#
## In[2]:
#
#
#help()
#
#
## In[15]:
#
#
##
#x = int(input("Enter the first number "))
#y = int(input("Enter the second number "))
#z = int(input("Enter the third number "))
#
#def summ(a,b,c):
#    if (a==b==c):
#        return 0
#    elif (b==c): 
#        return a
#    elif (a==c): 
#        return b
#    elif (a==b):
#        return c
#    else :
#        return (a+b+c)
#    
#w = summ(x,y,z)
#print(w)
#
#
#print("Initial number is zero")
#number = 0
#
#def countup (number):
#    print (number)
#    if number < 100:
#      countup (number+1)
#      
#countup(number)
#
#word = str(input("Enter the word: "))
#char = str(input("Enter the alphabet: "))
#letter = 0
#
#def mywordcount (word, char):
#  count = 0
#  for letter in word:
#      if (letter == char):
#          count += 1
#          return count
#      else:
#          return 0
#        
#y = mywordcount(word, char)
#print(("{} has {} 's").format(word, char))