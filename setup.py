from setuptools import find_packages
from setuptools import setup


setup(
    entry_points={
        # "EntryPoint must be in 'name=module:attrs [extras]' format"
        'console_scripts': 'install-plone=install:install',
    },
    tests_require=[
        'nose',
    ],
    license='Whatever license Plone is',
    name='plock',
    packages=find_packages(),
    test_suite = 'nose.collector',
)
