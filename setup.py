#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='cylinder_fitting',
    version='1.1.2',
    author='Xingjie Pan',
    author_email='xingjiepan@gmail.com',
    url='https://github.com/xingjiepan/cylinder_fitting',
    download_url='https://github.com/xingjiepan/cylinder_fitting/archive/1.1.2.tar.gz',
    keywords = ['geometry', 'fitting-algorithm'],
    packages=[
        'cylinder_fitting',
    ],
    install_requires=[
        'numpy',
        'scipy',
        'pytest',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
        ],
    },
    description='Fit a set of 3D points to a cylinder surface.',
    long_description=open('README.rst').read(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research',
    ],
)
