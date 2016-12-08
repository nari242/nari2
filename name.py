#! /usr/bin/python
import os
one= "nari"
two= "nunna"
three= 1
str_total= one+ " " +two
total= str_total*three
print str_total
print total
if three == 10:
	print "its equal"
elif three > 10:
	print "it's higher value"
elif three < 10:
	print "it's lower valu"
else:
	print "its not equal" 
xyz= raw_input("what u r studying")

print "iam studying "+ xyz

mycurrentworkingDir= os.system("mkdir  MUKESH")
if mycurrentworkingDir != 0:
	print "Directory exists"
else:
	print "New Directory created"
print "mydirectory :" + str(mycurrentworkingDir)

print "iam working on :"+ xyz

