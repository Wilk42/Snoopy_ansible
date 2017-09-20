Role Name
=========

This role will gather contents of the different cron directories and output them as a list


Example Playbook
----------------

---
- hosts: virtual
  roles:
     - cronlist_dirs_role


License
-------
BSD

Output
-------
When using the following format:
- debug: msg="{{ files.files | map(attribute='path') | list }}"-
{
    "msg": [
        "/etc/cron.hourly/mcelog.cron",
        "/etc/cron.hourly/inn-cron-nntpsend",
        "/etc/cron.hourly/inn-cron-rnews",
        "/etc/cron.weekly/99-raid-check",
        "/etc/cron.weekly/0anacron",
        "/etc/cron.weekly/makewhatis.cron",
        "/etc/cron.monthly/0anacron",
        "/etc/cron.d/sa-update"
    ]
}


Author Information
------------------

Sean Sullivan (ssulliva@redhat.com)
Consultant
