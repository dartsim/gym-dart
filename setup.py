# Copyright (c) 2011-2023, The DART development contributors
# All rights reserved.

from setuptools import setup, find_packages

setup(
    name="gym-dart",
    version="0.0.1",
    install_requires=["dartpy", "gymnasium", "numpy", "pytest"],
    packages=find_packages(),
    include_package_data=True,
)
