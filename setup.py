"""
A setuptools based setup module.
Based on:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import sys

import yaml
from setuptools import setup, find_packages


def get_version(version_file_loc):
    with open(version_file_loc, 'r') as stream:
        data = yaml.load(stream, yaml.SafeLoader)
        return data.get('version')


def inject_custom_repository(repository_name):
    blacklist = ['register', 'upload']
    inject_arg = '--repository=%s' % repository_name

    for command in blacklist:
        try:
            index = sys.argv.index(command)
        except ValueError:
            continue

        sys.argv.insert(index + 1, inject_arg)


inject_custom_repository('vikash-oi')

EXCLUDE_FILES = ['tf_flow/*']

setup(
    name='test',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=get_version('ops/conda-recipe/conda_build_config.yaml'),

    description="sklearn test",

    scripts=[],

    # The project's main homepage.
    url='https://github.com/vikash-oi/test',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    package_dir={'': 'src/py/dms/cli'},
    packages=find_packages('src/py', exclude=EXCLUDE_FILES),

)
