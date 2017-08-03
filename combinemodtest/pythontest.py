#!/usr/bin/python
base= yum_packages_short.json.read()
secondary = yum_packages_short_2.json.read()
print base
print secondary


base_json = json.dumps(base.split(': [', 1)[1].replace(']}', ''))
secondary_json = json.dumps(secondary.split(': [', 1)[1].replace(']}', ''))

print base_json
print secondary_json
