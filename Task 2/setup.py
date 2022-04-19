from setuptools import setup

setup(
   name='USerializer',
   version='1.0',
   description='JSON-YAML-TOML factory serializer',
   author='mddn41',
   install_requires=['PyYAML', 'toml', 'pytest'],
   packages=['USerializer'],
)
