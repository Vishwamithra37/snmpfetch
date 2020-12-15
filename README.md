# snmpfetch
mo2.py is the real bomb des


################################### Extending SNMP Agent #########################################

This assignment shows rate of change of the counter values of the custom OIDs requested to the from the sub-agent

################################### Execution : Step-by-Step #########################################

Operating System: Ubuntu 16.04 LTS

Open a terminal using:

	CTRL+ALT+T

The format of the command is as follows:

	$ python prober.py <IP_address:Port:Community> <Sampling_Interval> <OIDs>

#Community		-	determines a public or a private community, here we use public community
#IP_address		-	determines the IP address of the Sub-agent device, can also be localhost(127.0.0.1)
#OID			-	determines the OIDs requested, here our custom OID is .1.3.6.1.4.1.4171.40.0
#Sampling_Interval	-	determines the sampling rate of successive probes
#Port			- 	determines the port number to be used for SNMP 

Now, for example type the following command and include the custom OIDs, IP_address, Port, Community, Sampling_interval

	$ python prober.py 127.0.0.1:161:public 1 .1.3.6.1.4.1.4171.40.2 .1.3.6.1.4.1.4171.40.4

Here, if the IP address is of the device from which we want to probe.

