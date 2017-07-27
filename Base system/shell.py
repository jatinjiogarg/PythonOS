#-*-coding:utf8;-*-
#qpy:2
#qpy:console
def python_shell():
 import pip
 from shutil import copyfile
 import os
 home = "/storage/emulated/0/pythonos"
 try:
  os.stat(home)
 except:
  os.mkdir(home)
 installp = "/storage/emulated/0/pythonos/apps"
 pkginfo = home + "/" + "pyk/info.txt"
 y = os.getcwd()
 path = y
 from name import name
 Input = raw_input(name+"@python:" + path +"# ")
 cdpath = Input.split()
 lspath = Input.split()
 install = cdpath
 launch = install
 if Input=="help":
  print "ls:- for listing files "
  print "cd:- for changing directory"
  print "install:- for installing a python script to python os \n there must be a dependency file which contains dependency text for that script"
  print "e.g. - install sample.py dependency.txt"
  print " launch-: for launching installed python scripts"
  print " e.g- launch sample"
  print "maths:- for basic maths function"
  print "whoami :- prints your name"
  print "ls -: for listing files of directory"
 if cdpath[0]=="cd":
  if (len(cdpath))==1:
   print "Enter path follwed by space"
  else:   
   try:
    if cdpath[1]=="..":
     os.chdir("..")
    else:
     y = cdpath[1]
     os.chdir(y)
     path = y
   except Exception as e:
    print "No such file or directory"
 if lspath[0]=="ls":
    if (len(lspath))==1:
     try:
      path = os.getcwd()
      dirs = os.listdir(path)
      for file in dirs:
       print file
     except Exception as e:
      print "Permission denied"
    else:
     try:
      y = lspath[1]
      dirs = os.listdir(y)
      for file in dirs:
       print file
     except Exception as e:
      print "Permission denied"
      
 
    
 

 if Input=="whoami":
  from name import name 
  print name
 if Input=="maths":
  from maths import math
  math()
 if install[0]=="install":
  if not len(install)==3:
   print "Enter name of python script and dependency file\n follwed by space"
  else:
   y = install[1]
   x = install[2]
   ydash = y.split(".")
   ynew = ydash[0] + "\n"
   try:
    os.stat(installp)
   except:
    os.mkdir(installp)
   try:
    dependency = open(x,"r")
    file = dependency.readlines()
    z = len(file)
    for i in range(z):
     pip.main(['install', file[i]])
     i  = i + 1
    pathtoapp = installp + "/" + y
    copyfile(x,pathtoapp)
    chinfo = open(pkginfo, "a")
    chinfo.write(ynew)
    chinfo.close
    print "installation succesful"
   except:
    print "Unknown error"
 if launch[0]=="launch":
  if len(launch)==1:
   print "Installed Apps:"
   info = open(pkginfo, "r")
   x = info.readlines()
   y = len(x)
   for i in range(y):
    print x[i]
    i = i + 1
  else:
   info = open(pkginfo, "r")
   z = info.readlines()
   check = launch[1] + "\n"
   boolean = check in z
   if boolean==False:
    print "Enter valid app"
   else:
    try:
     x = launch[1]
     y = installp +"/"+ x + ".py"
     execfile(y)
    except:
     print "file not found"
     
   
   
   	
   
  
  
  
 