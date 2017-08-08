# !/usr/bin/python
# -*- coding: utf-8 -*-

#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['stableinterface'],
                    'supported_by': 'core'}

DOCUMENTATION = '''
---
module: listner
short_description: take output from netstat to json
version_added: "2.4"
author: Sean S <ssulliva@redhat.com>
description:
  - This module takes the input in for the from of output from the shell command:
  'netstat -tulpn | awk "{if (NR>2) {print}}"'
  It then takes the that data and converts it into a JSON format.
'''

EXAMPLES = '''
- name: Netstat output
  shell: 'netstat -tulpn | awk "{if (NR>2) {print}}"'
  register: netstat

- name: Convert Netstat output to Json
  listener:
    netstat: "{{netstat.stdout_lines | to_json}}"
  register: result
'''

RETURN = '''{
        "changed": false,
        "listeners": [
            {
                "foreign_address": "0.0.0.0",
                "foreign_port": "*",
                "local_address": "192.168.124.1",
                "local_port": "53",
                "pid": "1414",
                "process": "dnsmasq",
                "protocol": "tcp",
                "state": "LISTEN"
            },
            {
                "foreign_address": "0.0.0.0",
                "foreign_port": "*",
                "local_address": "127.0.0.1",
                "local_port": "631",
                "pid": "2202",
                "process": "cupsd",
                "protocol": "tcp",
                "state": "LISTEN"
            },
        ]
    }

'''

import json
from ansible.module_utils.basic import *
from itertools import chain
import requests

entryList = []


def parserow(netstatDatastr):
    # Split the string into a list
    netstatData = netstatDatastr.split()
    # Define Dicts for 8 entries
    tmpDict = {}

    # Split the LocalIP/Port into a list
    tmpLocal = netstatData[3].rsplit(':', 1)
    # Split the ForeignIP/Port into a list
    tmpForeign = netstatData[4].rsplit(':', 1)
    # Define the 8 dicts based on their netstat column names
    tmpDict["protocol"] = netstatData[0]
    tmpDict["local_address"] = tmpLocal[0]
    tmpDict["local_port"] = tmpLocal[1]
    tmpDict["foreign_address"] = tmpForeign[0]
    tmpDict["foreign_port"] = tmpForeign[1]
    # Test 5th element for alphabet char, if alpha its a State otherwise a PID
    if str(netstatData[5])[:2].isalpha():
        # We have a State, that data
        tmpDict["state"] = netstatData[5]
        # Split the PID/process on the /
        tmpPID = netstatData[6].split('/')
        tmpDict["pid"] = tmpPID[0]
        tmpDict["process"] = tmpPID[1]
    else:
        # We have a PID load that data
        tmpDict["state"] = ""
        tmpPID = netstatData[5].split('/')
        tmpDict["pid"] = tmpPID[0]entry1List
        tmpDict["process"] = tmpPID[1]
    # append all items to the list
    entryList.append(tmpDict)


def main():
    module = AnsibleModule(
        argument_spec=dict(
            netstat=dict(required=True, type='str'),
        )
    )

    if module.check_mode:
        module.exit_json(changed=False)
    # import data from input
    netstat = (module.params['netstat'])

    # Process each line of the input
    for i in range(len(json.loads(netstat))):
        parserow(str(json.loads(netstat)[i]))
    # Exit module with JSON output
    module.exit_json(listeners=(entryList), changed=False)


if __name__ == '__main__':
    main()
