# Copyright (c) 2011-2023, The DART development contributors
# All rights reserved.

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="gym-dart",
    version="0.0.1",
    description="A Gym environment wrapper for the DART physics engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["dartpy", "gym", "numpy", "pytest"],
    packages=find_packages(),
    include_package_data=True,
)
