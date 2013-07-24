#------------------------------------------------------------------------------
# Pyroma says:
# Final rating: 10/10
# Your cheese is so fresh most people think it's a cream: Mascarpone
#------------------------------------------------------------------------------
from setuptools import find_packages
from setuptools import setup


setup(
    author="Alex Clark",
    author_email="aclark@aclark.net",
    classifiers=[
        'Framework :: Plone :: 4.3',
        'Programming Language :: Python :: 2.7',
    ],
    description="Plock is a Plone Installer for the Pip-loving Crowd",
    entry_points={
        # "EntryPoint must be in 'name=module:attrs [extras]' format"
        'console_scripts': [
            'install-plone=plock.install:install',
        ],
    },
    install_requires=[
        'configparser',
        'sh',
        'yolk',
        'zc.buildout',
    ],
    keywords="pip plone",
    license='Whatever license Plone is',
    long_description=(
        open('README.rst').read() + '\n' +
        open('CHANGES.rst').read()
    ),
    name='plock',
    packages=find_packages(),
    tests_require=[
        'nose',
    ],
    test_suite = 'nose.collector',
    url='https://github.com/aclark4life/plock',
    version='0.0.6',
    zip_safe=False,
)
