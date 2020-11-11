Syncthing ![](https://travis-ci.com/rremizov/ansible-syncthing.svg?branch=master)
=========

Install [Syncthing](https://syncthing.net/).

Features
--------

- Integration with systemd and ufw using original config from the Syncthing package.

Requirements
------------

- Debian

Role Vars
---------

**[defaults/main.yml](defaults/main.yml)**

Example
-------

```yaml
    syncthing_ufw_enabled: yes
    syncthing_ufw_rule_state: enabled
    syncthing_users:
      - user0 
      - user1 
      - user1 
```
