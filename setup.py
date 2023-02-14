# Copyright (c) 2011-2023, The DART development contributors
# All rights reserved.

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_new_patch_number(package_name, default: int):
    import requests

    try:
        url = f"https://pypi.org/pypi/{package_name}/json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            version = data["info"]["version"]
            patch_number = version.split(".")[-1].split("post")[-1]
            return str(max(default, int(patch_number) + 1))
        else:
            return str(default)
    except requests.exceptions.RequestException:
        return str(default)


setup(
    name="gym-dart",
    version="0.0.1.post" + get_new_patch_number("gym-dart", 31),
    description="A Gym environment wrapper for the DART physics engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["dartpy", "gym", "numpy", "pytest"],
    packages=find_packages(),
    include_package_data=True,
)
