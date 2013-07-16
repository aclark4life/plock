from setuptools import find_packages
from setuptools import setup


setup(
    description="Plock is Plone for the Python Crowd",
    entry_points={
        # "EntryPoint must be in 'name=module:attrs [extras]' format"
        'console_scripts': [
            'install-plone=plock.install:install',
        ],
    },
    install_requires=[
        'sh',
        'zc.buildout',
    ],
    license='Whatever license Plone is',
    long_description=(
        open('README.rst').read() + '\n' +
        open('HISTORY.txt').read()
    ),
    name='plock',
    packages=find_packages(),
    tests_require=[
        'nose',
    ],
    test_suite = 'nose.collector',
    version='0.0.1',
)
