from distutils.core import setup
from setuptools import find_packages

setup(
    name='d100',
    version='0.1.dev0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    license='dowhatyouwantwithit license',
    long_description=open('README.md').read(),
)
