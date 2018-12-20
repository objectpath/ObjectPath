import os
from setuptools import setup
import subprocess

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.rst')
    + '\n' +
    'Download\n'
    '********\n'
    )

version = None
try:
    version = subprocess.check_output('git describe --tags', shell=True, universal_newlines=True)
except:
    pass

if not version:
    raise Exception('Could not determine version from git')

version = version.lstrip('v')
version = version.strip()


setup(name='objectpath-ng',
            version=version,
            description='The agile query language for semi-structured data. #JSON',
            long_description=long_description,
            url='http://objectpath.github.io/ObjectPath',
            author='Chris Lapa',
            author_email='36723261+chris-lapa@users.noreply.github.com',
            license='MIT',
            packages=['objectpath','objectpath.utils','objectpath.core'],
            # package_dir={'': 'objectpath'},
            keywords="query, tree, JSON, nested structures",
            classifiers=[
                "Development Status :: 6 - Mature",
                "Intended Audience :: Developers",
                "Intended Audience :: Science/Research",
                "License :: OSI Approved :: MIT License",
                "Programming Language :: Python",
                "Topic :: Software Development :: Libraries :: Python Modules"
            ],
            zip_safe=True,
            entry_points = {
                'console_scripts': [
                    'objectpath = objectpath.shell:main'
                ]
            },
            test_suite="tests"
        )
