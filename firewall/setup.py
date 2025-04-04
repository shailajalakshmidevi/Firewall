# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# Try to read the README.rst file. If it doesn't exist, use a fallback description.
try:
    with open('README.rst') as f:
        readme = f.read()
except FileNotFoundError:
    readme = "No README file found, but this is the firewall project."

# Try to read the LICENSE file. If it doesn't exist, set an empty string.
try:
    with open('LICENSE') as f:
        license = f.read()
except FileNotFoundError:
    license = ""

setup(
    name='firewall',  # You can change this to the actual project name if necessary
    version='0.1.0',
    description='A software-based firewall to analyze network traffic and enforce inbound/outbound rules.',
    long_description=readme,  # This will use the README content or the fallback text
    author='Your Name',  # Update with the actual author's name
    author_email='your.email@example.com',  # Update with your email
    url='https://github.com/tharaka27/firewall',  # Update with the actual project URL
    license=license,  # License content or empty string if not available
    packages=find_packages(exclude=('tests', 'docs')),  # Exclude tests and docs folders if they exist
)
