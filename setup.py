from setuptools import setup

setup(
    name='Artifactory CLI',
    version='1.0',
    packages=['artcli', 'art'],
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        art=art:cli
    '''
)