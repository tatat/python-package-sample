from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name='greeting',
    version='0.0.1',
    description='Greeting',
    packages=find_packages(exclude=['tests*']),
    install_requires=install_requirements,
)
