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
module: repolist
short_description: take output from yum repolist to json
version_added: "2.4"
author: Sean S <ssulliva@redhat.com>
description:
  - This module takes the input in for the from of output from the shell command:
  'yum repolist |  awk "{if (NR>3) {print}}" | head -n -1 '
  Optional this module will also work with DNF using hte following command for input
  'dnf repolist |  awk "{if (NR>3) {print}}"'
  It then takes the that data and converts it into a JSON format.
'''

EXAMPLES = '''
- name: get repolist
  shell: 'yum repolist |  awk "{if (NR>3) {print}}" | head -n -1 '
  register: repoList

- name: Convert repolist output to Json
  repolist:
    repolist: "{{repoList.stdout_lines | to_json}}"
  register: result
'''

RETURN = '''{
        "changed": false,
        "repos": [
            {
                "repo-id": "google-chrome",
                "repo-name": "google-chrome"
            }
        ]
    }
'''

import json
from ansible.module_utils.basic import *
from itertools import chain
import requests

entryList = []


def parserow(reposDatastr):
    # Split the string into a list
    reposData = reposDatastr.split()
    # Define Dicts for 8 entries
    tmpDict = {}

    # Define the 8 dicts based on their repos column names
    tmpDict["repo-id"] = reposData[0]
    tmpDict["repo-name"] = reposData[1]

    # append all items to the list
    entryList.append(tmpDict)


def main():
    module = AnsibleModule(
        argument_spec=dict(
            repolist=dict(required=True, type='str'),
        )
    )

    if module.check_mode:
        module.exit_json(changed=False)
    # import data from input
    repos = (module.params['repolist'])

    # Process each line of the input
    for i in range(len(json.loads(repos))):
        parserow(str(json.loads(repos)[i]))
    # Exit module with JSON output
    module.exit_json(repos=(entryList), changed=False)


if __name__ == '__main__':
    main()
