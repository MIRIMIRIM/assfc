from setuptools import setup, find_packages

setup(
    name='assfc',
    version='0.1',
    py_modules=['assfc'],
    packages=find_packages(),
    data_files=[('', ['config.json'])],
    install_requires=[''],
)