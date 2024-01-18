# from distutils.core import setup

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()


setup(
    name = 'eaglecore',
    version = '0.1',
    author = 'Jessy Khafif',
    author_email= 'khafifjessy.github@gmail.com',
    packages = find_packages(),
    # packages= [
    #     'eaglecore'
    # ],
    install_requires=requirements
)