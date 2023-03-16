#!/usr/bin/env python

from setuptools import find_packages, setup

setup(name='vehikle',
      version='0.1.0',
      packages=find_packages(),
      description='search the best price for the cars on the second hand market with the help of artificial intelligence',
      author='Bertan Ulusoy',
      author_email='bertan_ulusoy@yahoo.com',
      url='https://github.com/egeai/vehikle',
      install_requires=['requests=2.27.1', 'pandas==1.4.0', 'numpy==1.22.1', 'scikit-learn==1.0.2'],
      license='MIT',
     )