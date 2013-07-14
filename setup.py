from setuptools import setup


setup(
    entry_points={
        # "EntryPoint must be in 'name=module:attrs [extras]' format"
        'console_scripts': 'install-plone=install:install',
    },
    install_requires=[
        'nose',
    ],
    name='plock',
    license='Whatever license Plone is',
)
