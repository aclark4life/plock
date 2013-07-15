from setuptools import find_packages
from setuptools import setup


setup(
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
    name='plock',
    packages=find_packages(),
    tests_require=[
        'nose',
    ],
    test_suite = 'nose.collector',
    version='0.0.1',
)
