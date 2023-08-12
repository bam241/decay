from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='decay',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/kennethreitz/samplemod',
)

