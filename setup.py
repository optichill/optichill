"""A setuptools-based setup module adapted from the Python Packaging Authority's
sample project.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    # Install this project using:
    # $ pip install chachies
    #
    # It lives on PyPI: https://pypi.org/project/chachies/
    name='optichill',

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    version='1.0',  # Required

    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description='Machine Learning Package for chiller plant efficiency',  # Required
    url='https://github.com/optichill/optichill',
    author='Optimum energy DIRECT team',
    packages=find_packages(),


    install_requires=[
        'numpy==1.14.2',
        'pandas==0.22.0',
        'scipy==1.0.0',
        'sklearn==0.19.1'
        'matplotlib==2.2.2'
        'seaborn==0.8.1'
    ]

)
