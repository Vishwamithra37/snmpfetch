#! C:\Users\mithr\AppData\Local\Programs\Python\Python39\python.exe
#!/usr/bin/env python3

#This code is typed and owned By Vishwa Mithra Tatta for the assignment 3 of the subject ET-2598

import sys

from pysnmp.hlapi import *

#####Please download the above packages if not available#####
#####Initializing########

dum=0 #Dummy variable
nargs=(len(sys.argv))#This is the number of input arguments
print('Total number of arguments:',format(len(sys.argv)))


a=[None]*nargs 

for b in sys.argv:
 a[dum]=b                         #All the input arguments are put into this variable-'a'
 dum=dum+1
 

dum=0
c=str(a[1]).split(':')
agip=str(c[0])   #This is the agent_ip.
print("This is the agent_ip:",agip)
po=int(c[1])     #This is the port number.
print("This is the port-number:", po)
com=str(c[2])    #this is the community string.
print("This is the community-string:", com)
safreq=float(a[2])      #This is the sample frequency. This is catching the inputs correctly. DOuble checked
print("This is the sample-freq:", safreq)
nsamp=int(a[3])   #This is the number of samples.
print("This is the number of samples:", nsamp)
tp=1/safreq      #This is the time period of the frequencies input.
print("This is the time period for number of samples:", tp)

oids=[None]*(nargs-3)
for b in range(4,nargs):
 oids[dum]=str(a[b]) #Assigning all the oids to this oids variable
 print("this is the oid:", oids[dum])
 dum=dum+1
 print("Number of OIDs given:", dum)



