from setuptools import setup, find_packages

setup(
    name="expense_tracker",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Flask>=3.0.0",
    ],
)