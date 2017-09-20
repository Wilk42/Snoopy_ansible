Role Name
=========

This role will gather the output of netstat of a host and output that data in a JSON format.

Requirements
------------

This role runs a custom module, the module listener must be in the library folder.
More information is contained in the module listener.py

A script version of the module that reads data in the file is in the listenerscript folder



Example Playbook
----------------
Sudo is required in order to get the correct output on netstat

    ---
    - hosts: localhost
      become: yes
      roles:
         - listener


License
-------

BSD

Author Information
------------------

Sean Sullivan (ssulliva@redhat.com)
Consultant
