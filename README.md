pdb
===
PDB (Password DB) for shared password management

Description
-----------

PDB provides an interface to store and share secrets across a team. For example, a group of system adminstrators sharing admin or root passwords.

The secrets are key/value pairs, where the value can be any valid yaml document. The secret values are retrived by referencing the key. The resultant file is stored and encrypted using gpg.

Each member needs to have a seperate gpg key pair, used to encrypt the secret file. The file can then be stored on an http server, which is fetched by the client and decrypted to show the corresponding secret value.

It is essentially a wrapper around gpg commands, with an easy to understand user interface.

Usage
-----
There are two commands provided :

`manage-pdb`
This is used to initialize and manage the password store. i.e. show/list/add/delete keys and users.

The public keys of the participating memeber can be made available on a gpg key server, either a public or [private](https://sks-keyservers.net/)

`pdb`
This is the client utility used by the client to fetch and show (copy to clipboard) the secrets.

Installation
------------
* Install `pip`
* Ensure you have [gnupg](https://www.gnupg.org/) installed
* Install the `pdb` package
```pip install pdb```

Optionally you can install `xerox` package which causes pdb to copy to clipboard by default.

```pip install xerox```

Note: For xerox on Linux you need to install `xclip` as well

Todo
----
* GPG agent support
* Update version on every change
