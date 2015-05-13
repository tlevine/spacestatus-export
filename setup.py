from setuptools import setup, find_packages

setup(
    name = 'spacestatus-export',
    version = '0.1',
    description = 'Get historical space API data',
    author = 'Thomas Levine',
    author_email = '_@thomaslevine.com',
    url = 'http://dada.pink/spacestatus-export',
    entry_points = {'console_scripts': ['spacestatus-export = spacestatus:cli']},
    license = 'AGPL',
    py_modules = ['spacestatus'],
    install_requires = [
        'requests>=2.3.0',
        'vlermv>=1.3.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.4',
    ],
)
