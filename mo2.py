#!/usr/bin/env python3

#This code is typed and owned By Vishwa Mithra Tatta for the assignment 3 of the subject ET-2598

###################Modules Required####################

import sys
import time
from puresnmp import get
import puresnmp.transport
import threading
from nested_dictionaries import NestedDictionaries as nd

#####Please download the above packages if not available#####
#####Initializing########


gloval=nd()                                ##########The place where all the OID values are stored###########           
glotime=nd()                               ##########The place where all the time of sampling values are stored########### 
glorate=nd()                                ##########The place where all the rate values are stored###########
print("\n\n")
print("Input data check:\n")
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
print(oids,"\n\n\n\n")


#########END OF TAKING INPUTS ##################
#########     Time-Giver      #####################

def ti1():                                                #Returns Time in unix units
 return round(time.time())

#########END of Time function#####################
#########Start of rate calculation################

def rato11(a,b,dt1,dt2):        #######If it works the first time and gives time######
 ra=(b-a)/(dt2-dt1)
 return ra
 
def rate12(a,b,t1,t2):         #########If it doesn't work and we need to use our time#######
 ra=(b-a)/(t2-t1) 
 return ra


###########End of Rate Calculation################
#########Start of Fetching   ################   

def fletcher(oi,cou): 
 
               result = get(agip, com, oi, port=po)
               value=result
               ti4=ti1()                                #Time of recieving the value
               currtime=ti4
               
               gloval[cou][oi]=result
               glotime[cou][oi]=currtime
               
               glorate[cou][oi]=rate12(gloval[cou-1][oi],gloval[cou][oi],glotime[cou-1][oi],glotime[cou][oi]) #####The magic piece#####
               print(glorate[cou][oi], end=" | ")
                   
               
              
def fletcher2(oi,cou): 
 
               result = get(agip, com, oi, port=po)
               print(result, end = " | ")
               currtime=ti1()
               
               gloval[cou][oi]=result
               glotime[cou][oi]=currtime
               
               
           
              





###################End of fetching   ###################
###################Start of threading################

puresnmp.transport.BUFFER_SIZE = 4096
puresnmp.transport.RETRIES = 1
n=0      #Dummy variable
troll=1
ball=1
for cou in range(1,nsamp+1):
     
     
     print('\n')
     time.sleep(tp)
     print(ti1(),end=" | ")
     

     for apple in oids:
      if ball==1:
       f1=threading.Thread(target=fletcher2(apple,cou))
       f1.daemon=True
       f1.start() 
      else:
       f1=threading.Thread(target=fletcher(apple,cou))
       f1.daemon=True
       f1.start() 
     
           
     ball=2
        









     
  
   
 
      
    
    
    

    
    
    
    
    
    
    
    