#!/usr/bin/python
import json
from ansible.module_utils.basic import *
from itertools import chain
import requests
import pprint ##prettyprinter for debug only

#declare the json object to store data
netstatJSON = {}
entryList = []


def parserow(netstatDatastr):
    #Split the string into a list
    netstatData = netstatDatastr.split()
    #Define Dicts for 8 entries
    tmpDict ={}

    #Split the LocalIP/Port into a list
    tmpLocal = netstatData[3].rsplit(':',1)
    #Split the ForeignIP/Port into a list
    tmpForeign = netstatData[4].rsplit(':',1)
    #Define the 8 dicts based on their netstat column names
    tmpDict["protocol"] = netstatData[0]
    tmpDict["local_address"] = tmpLocal[0]
    tmpDict["local_port"] = tmpLocal[1]
    tmpDict["foreign_address"] = tmpForeign[0]
    tmpDict["foreign_port"] = tmpForeign[1]
    ##Test 5th element for alphabet char, if alpha its a State otherwise a PID
    if str(netstatData[5])[:2].isalpha():
       #We have a State, that data
       tmpDict["state"] = netstatData[5]
       #Split the PID/process on the /
       tmpPID = netstatData[6].split('/')
       tmpDict["pid"] = tmpPID[0]
       tmpDict["process"] = tmpPID[1]
    else:
       #We have a PID load that data
       tmpDict["state"] = ""
       tmpPID = netstatData[5].split('/')
       tmpDict["pid"] = tmpPID[0]
       tmpDict["process"] = tmpPID[1]
    #append all items to the list
    entryList.append(tmpDict)
    #print tmpDict




#read data in
netstat = open('netstat.json', 'r').read()

#Load input into a string
#tmpstring = str(json.loads(netstat)[11])

for i in range(len(json.loads(netstat))):
    parserow(str(json.loads(netstat)[i]))


#create Dict, append list to the Dict
netstatJSON["listeners"] = entryList
#netstatJSON["listeners"] = json.dumps(entryList)

#print tmplist
#print json.loads(netstat)[0]

#pprint.pprint (json.dumps(netstatJSON))


#available = set(base_json.keys())
#satchel = set(secondary_json.keys())

# fruit not in your satchel, but that is available
#print available.difference(satchel)
#for key, value in secondary_json[]:
#    print key, value
