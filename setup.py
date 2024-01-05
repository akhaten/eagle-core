from distutils.core import setup


with open('requirements.txt') as f:
    requirements = f.readlines()


setup(
    name = 'eaglecore',
    version = '0.1',
    author = 'Jessy Khafif',
    author_email= 'khafifjessy.github@gmail.com',
    packages= [
        'eaglecore'
    ],
    install_requires=requirements
)