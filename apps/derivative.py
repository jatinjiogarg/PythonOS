#-*-coding:utf8;-*-
#qpy:2
#qpy:console
from sympy import *
print "***************"
print "*             *"
print "*By Jatin Garg*"
print "*             *"
print "***************"
 

p = 1
z = input("Enter 1 for differentiation 0 for exit:- ")
if z==p:
 while z==p:
  x = symbols("x")
  y = input("Enter An Equation:- ")
  ydeff = diff(y ,"x")
  print(ydeff)
  z = input("Enter 1 for differentiation 0 for exit:- ")
  if z==0:
   print("Have A Nice Day")
   
elif z==0:
   print("Have A Nice Day")
 

  

   

  

