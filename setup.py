from setuptools import setup


setup(
    entry_points={
        # "EntryPoint must be in 'name=module:attrs [extras]' format"
        'console_scripts': 'install-plone=install:install',
    },
    tests_requires=[
        'nose',
    ],
    license='Whatever license Plone is',
    name='plock',
    test_suite = 'nose.collector',
)
