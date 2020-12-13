#! C:\Users\mithr\AppData\Local\Programs\Python\Python39\python.exe
#!/usr/bin/env python3

#This code is typed and owned By Vishwa Mithra Tatta for the assignment 3 of the subject ET-2598

import sys
from puresnmp import get

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
agip=str(c[0])          #This is the agent_ip.
po=int(c[1])            #This is the port number.
com=str(c[2])           #this is the community string.
safreq=float(a[2])      #This is the sample frequency. This is catching the inputs correctly. DOuble checked
nsamp=int(a[3])         #This is the number of samples.
tp=1/safreq             #This is the time period of the frequencies input.

print("This is the agent_ip:",agip)
print("This is the port-number:", po)
print("This is the community-string:", com)
print("This is the sample-freq:", safreq)
print("This is the number of samples:", nsamp)
print("This is the time period for number of samples:", tp)


oids=[None]*(nargs-3)
for b in range(4,nargs):
 oids[dum]=str(a[b]) #Assigning all the oids to this oids variable
 print("this is the oid:", oids[dum])
 dum=dum+1
 print("Number of OIDs given:", dum)

oids = oids[:-1]
print(oids)
    
for oi in oids:
  result = get(agip, com, oi, port=po)
  print(result)    
    
    
    

    
    
    
    
    
    
    
    