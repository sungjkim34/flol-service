from setuptools import setup, find_packages
import os

def requirements():
    with open('requirements.txt', 'r') as stream:
        reqs = stream.read()
    if reqs.startswith('--index-url'):
        reqs = reqs.split('\n', 1)[-1]
    return reqs

setup(
    name='flol-service',
    maintainer="Sungjae Kim",
    url='github.com/sungjkim34/flol-service',
    packages=find_packages(),
    setup_requires=['setuptools_scm'],
    include_package_data=True,
    install_requires=requirements(),
    extras_require={
        'dev': [
            'tox',
            'pycodestyle',
            'pydocstyle',
            'pylint',
            'pytest',
            'pytest-cov'
        ],
    },
    entry_points={
    }
)
