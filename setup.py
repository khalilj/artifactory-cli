from setuptools import setup

setup(
    name='art',
    version='1.0',
    packages=['artcli'],
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        art=art:cli
    '''
)