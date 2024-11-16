from setuptools import setup, find_packages

setup(
    name='pymsiapi',
    version='0.0.1',
    description='A library for msii.xyz/api',
    packages=find_packages(),
    install_requires=["requests"],
    test_suite='tests',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
)
