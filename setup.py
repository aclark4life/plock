from setuptools import setup


setup(
    entry_points={
        # "EntryPoint must be in 'name=module:attrs [extras]' format"
        'console_scripts': 'install-plone',
    },
    name='plock',
    license='Whatever license Plone is',
)
