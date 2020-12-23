# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='benard_py',
    version='0.1.0',
    description='Python module for Solving Navier-Stokes equation and Energy equation in Benard cell flow',
    long_description=readme,
    author='Akira Shioyoke',
    author_email='s.akira2986@gmail.com',
    install_requires=['numpy', 'matplotlib'],
    url='https://github.com/syoukera/benard_py',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

