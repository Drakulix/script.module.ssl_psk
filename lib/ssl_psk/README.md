Modified Version of https://github.com/webgravel/common-ssl
===========================================================

Includes binary files for lin,osx,win. Instantly ready for use.
Used by https://github.com/drakulix/plugin.program.steam.streaming

Original Readme:
================

gravel-common-ssl
==========

OpenSSL TLS-PSK wrapper for Python

Use `ssl_psk.wrap_socket` instead of 'ssl.wrap_socket' with `psk` paramater set to PSK key string.

```
wrapper = ssl_psk.wrap_socket(sock, psk='really secret secret', ciphers='PSK-AES256-CBC-SHA',
                              ssl_version=ssl.PROTOCOL_TLSv1,
                              server_side=True)
```
