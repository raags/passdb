#!/usr/bin/env python

from setuptools import setup

setup(name='pdb',
      version='0.1.0',
      description='PDB (Password DB) for shared password management',
      author='Raghu Udiyar',
      author_email='raghusiddarth@gmail.com',
      url='https://github.com/raags/pdb',
      install_requires=['python-gnupg', 'argparse', 'pyyaml'],
      packages=['pdb'],
      entry_points = {
        'console_scripts': [
        'pdb=pdb.pdb:main',
        'manage-pdb=pdb.manage_pdb:main'
        ],
      },
     )
