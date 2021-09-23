import sys
from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rpm',
    version='0.0.3',
    url='https://github.com/JaneSoo/rpm-dnf/',
    license='GPLv2+',
    author='RPM developers',
    maintainer='Nick Coghlan',
    maintainer_email='ncoghlan@gmail.com',
    home_page='https://github.com/JaneSoo/rpm-dnf/',
    description='Dummy RPM package. Please use python-rpm provided by your OS.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    platforms='any',
)
