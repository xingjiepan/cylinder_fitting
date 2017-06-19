#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='cylinder_fitting',
    version='0.0.1',
    author='Xingjie Pan',
    author_email='xingjiepan@gmail.com',
    url='https://github.com/xingjiepan/cylinder_fitting',
    packages=[
        'cylinder_fitting',
    ],
    install_requires=[
        'numpy',
        'scipy',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
        ],
    },
    description='Fit a set of 3D points ot a cylinder surface.',
    long_description=open('README.rst').read(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research',
    ],
)
