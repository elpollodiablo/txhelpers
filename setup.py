"""A setuptools based setup module.
"""
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='txhelpers',
    version='0.1.0',
    description='Small module to make twisted a bit more comfortable',
    long_description=long_description,
    url='https://github.com/elpollodiablo/txhelpers',
    author='Philip Poten',
    author_email='philip.poten@gmail.com',
    license='Apache',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='twisted',
    py_modules=["txhelpers"],
    install_requires=['Twisted'],
    extras_require={
    },
    package_data={
    },
    data_files=[],
    entry_points={
    },
)