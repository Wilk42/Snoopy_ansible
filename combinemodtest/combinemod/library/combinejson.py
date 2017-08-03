#!/usr/bin/python
import json
from ansible.module_utils.basic import *
from itertools import chain
import requests


def main():
    module = AnsibleModule(
        argument_spec=dict(
            base=dict(required=True, type='str'),
            secondary=dict(required=True, type='str'),
        )
    )
    ## Remove extras to make a proper json dict

    base_json = ("[" + module.params['base'].split(': [', 1)[1].replace(']}', ']'))
    secondary_json = json.dumps("[" + module.params['secondary'].split(': [', 1)[1].replace(']}', ']'))

    result = dict(
        ping=base_json[0]
    )
    module.exit_json(changed=True, **result)

if __name__ == '__main__':
    main()
