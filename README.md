PassDB
===
PassDB (Password DB) for shared password management using GPG

Description
-----------

PassDB provides an interface to store and share secrets across a team. For example, a group of system adminstrators sharing admin or root passwords.

The secrets are key/value pairs, where the value can be any valid yaml document. The secret values are retrieved by referencing the key. The resultant file is stored and encrypted using gpg.

The idea is that every member has a gpg key pair encrypting the secret file. The file can then be stored on a server, retrieved by the client (passdb) and decrypted to show the corresponding secret value.

It is essentially a wrapper around gpg commands, with an easy to understand user interface.

Usage
-----
There are two commands provided :

`manage-passdb`
This is used to initialize and manage the password store. i.e. show/list/add/delete keys and users.

The public keys of the participating memebers can be made available on a gpg key server, either a public or [private](https://sks-keyservers.net/)

`passdb`
This is the client utility used by the client to fetch, update and show (copy to clipboard) the secrets. Programmatic access is also available.

Installation
------------
* Install `pip`
* Ensure you have [gnupg](https://www.gnupg.org/) installed
* Install the `passdb` package
```pip install passdb```

Optionally you can install `xerox` package which causes passdb to copy to clipboard by default.

```pip install xerox```

Note: For xerox on Linux you need to install `xclip` as well

Todo
----
* GPG agent support
* Update version on every change
