#!/usr/bin/python
import json
from ansible.module_utils.basic import *
from itertools import chain
import requests

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

base = open('yum_packages_short_2.json', 'r').read()
secondary = open('yum_packages_short.json', 'r').read()

base_temp = "[" + base.split(': [', 1)[1].replace(']}', ']')
base_json = json.loads(base_temp, object_hook=AttrDict)

secondary_temp = "[" + secondary.split(': [', 1)[1].replace(']}', ']')
secondary_json = json.loads(secondary_temp)

print getattr(base_json, )
fruit_available = {'apples': 25, 'oranges': 0, 'mango': 12, 'pineapple': 0 }

my_satchel = {'apples': 1, 'oranges': 0, 'kiwi': 13 }

#available = set(base_json.keys())
#satchel = set(secondary_json.keys())

# fruit not in your satchel, but that is available
#print available.difference(satchel)
#for key, value in secondary_json[]:
#    print key, value
