#!/usr/bin/env python

from setuptools import setup

setup(
      name='pdb',
      packages=['pdb'],
      version='0.1',
      description='PDB (Password DB) for shared password management',
      author='Raghu Udiyar',
      author_email='raghusiddarth@gmail.com',
      url='https://github.com/raags/pdb',
      download_url = 'https://github.com/raags/pdb/tarball/0.1',
      install_requires=['python-gnupg', 'argparse', 'pyyaml'],
      entry_points = {
        'console_scripts': [
        'pdb=pdb.pdb:main',
        'manage-pdb=pdb.manage_pdb:main'
        ],
      },
     )
