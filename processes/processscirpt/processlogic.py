#!/usr/bin/python
import json
from ansible.module_utils.basic import *
from itertools import chain
import requests
import pprint ##prettyprinter for debug only

#declare the json object to store data
netstatJSON = {}
entryList = []


def parserow(processDatastr):
    # Split the string into a list
    processData = processDatastr.split()
    # Define Dicts for 8 entries
    tmpDict = {}



    # Define the 8 dicts based on their netstat column names
    tmpDict["USER"] = processData[0]
    tmpDict["PID"] = processData[1]
    tmpDict["CPU_Perc"] = processData[2]
    tmpDict["MEM_Perc"] = processData[3]
    tmpDict["TTY"] = processData[6]
    tmpDict["STAT"] = processData[7]
    tmpDict["COMMAND"] = processData[10]
    # append all items to the list
    entryList.append(tmpDict)




#read data in
processes = open('process.json', 'r').read()

#Load input into a string
#tmpstring = str(json.loads(netstat)[11])

for i in range(len(json.loads(processes))):
    parserow((json.loads(processes)[i]).encode('utf-8'))


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
