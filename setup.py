from setuptools import setup, find_packages

setup(
    name='IsarnConnect-V2',
    version='0.1',
    author='C0MaE',
    author_email='jannis.koberg@icloud.com',
    packages=find_packages(),
    install_requires=[
        'psycopg2>=2.9.9',
        'sqlalchemy>=2.0.27',
    ],
    long_description=r"""
IsarnConncet
==========

This is a description of my package.

The interface to store and retrieve the data from the meters. For example, to evaluate this data.
"""
)
