from setuptools import setup, find_packages

setup(
    name="mysomepypackage",
    author="tombed",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "numpy"
    ],
    python_requires=">=3.6"
)