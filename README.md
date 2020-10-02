Syncthing
=========

Install [Syncthing](https://syncthing.net/).

Features
--------

- Integration with systemd and ufw using original config from the syncthing package.

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
    syncthing_users:
      - user0 
      - user1 
      - user1 
```
