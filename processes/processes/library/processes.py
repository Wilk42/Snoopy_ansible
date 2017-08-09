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
module: ps_aux
short_description: take output from ps aux to json
version_added: "2.4"
author: Sean S <ssulliva@redhat.com>
description:
  - This module takes the input in for the from of output from the shell command:
  ' ps aux '
  It then takes the that data and converts it into a JSON format.
'''

EXAMPLES = '''
- name: PS Aux output
  shell: 'ps aux '
  register: ps_aux

- name: Convert ps_aux output to Json
  listener:
    ps_aux: "{{ps_aux.stdout_lines | to_json}}"
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


def main():
    module = AnsibleModule(
        argument_spec=dict(
            processes=dict(required=True, type='str'),
        )
    )

    if module.check_mode:
        module.exit_json(changed=False)
    # import data from input
    processes = (module.params['processes'])

    # Process each line of the input
    for i in range(len(json.loads(processes))):
        parserow((json.loads(processes)[i]).encode('utf-8'))
    # Exit module with JSON output
    module.exit_json(processes=(entryList), changed=False)


if __name__ == '__main__':
    main()
