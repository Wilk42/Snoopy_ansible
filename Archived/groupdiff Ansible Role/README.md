# Group Difference module

Description
===========
Web Service for Project Snoopy.
*** Internal Only ***

Role Description
===========
This role uses bash to retrieve a list of group names and compares them against the groups.json in the variable folder.


TBD
===========
A task needs to be added to the role to upload this data to the web server. 

Default group var file
===========
Base group file is a list in json that has been generated on a vanilla machine.
In this case it is just a list of group names.
If you remove everything between " "stdout_lines": [" and "]}"
You will just need to put in a list of group names where the names are quoted such as:
"postfix", "nobody"
