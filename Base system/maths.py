#-*-coding:utf8;-*-
#qpy:2
#qpy:console
def math():
 mathlist = ["add","subtract","product","divide","quadratic","derivative"]
 maths = raw_input("Type add,subtract,product,divide,derivative,quadratic,(More coming soon)-: ")
 boolean = maths in mathlist
 if boolean==True:
   if maths=="add":
  	 x = float(raw_input("Enter First no.-: ") )
  	 y = float(raw_input("Enter Second no. -: "))
  	 p = str(x + y)
  	 print " Answer Is  " + p
  	 return 1
  
   if maths=="subtract":
  	 x = float(raw_input("Enter First no.-: ") )
  	 y = float(raw_input("Enter Second no. -: "))
  	 p = str(x + y)
  	 print " Answer Is  " + p
  	 return 1
   if maths=="product":
  	 x = float(raw_input("Enter First no.-: ") )
  	 y = float(raw_input("Enter Second no. -: "))
  	 p = str(x*y)
  	 print " Answer Is  " + p
  	 return 1
  	
   if maths=="divide":
  	 x = float(raw_input("Enter First no.-: ") )
  	 y = float(raw_input("Enter Second no. -: "))
  	 p = str(x/y)
  	 print " Answer Is  " + p
  	 return 1
   if maths=="quadratic":
    import numpy
    from sympy import solve
    from name import x
    y = input("Enter A quadratic Equation-: ")
    roots = solve(y, x)
    print roots
    return 1
   if maths=="derivative":
    from name import x
    from sympy import *
    y = input("Enter Equation-: ")
    ydeff = diff(y, x)
    print ydeff
    
 else:
  print ("Enter a valid operation")
    
