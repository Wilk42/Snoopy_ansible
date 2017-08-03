#!/usr/bin/python
import json
from ansible.module_utils.basic import *
from itertools import chain


def manipulate_json(module):

    return False


def main():
    fields = {
        "Base_Json": {"required": True, "type": "str"},
        "Target_Json": {"required": True, "type": "str"},
        "state": {
            "default": "present",
            "choices": ['present', 'absent'],
            "type": 'str'
        },
    }
    results = manipulate_json(module)
    module = AnsibleModule(argument_spec=fields)
    module.exit_json(**results)


if __name__ == '__main__':
    main()
