from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of packages that need to be installed for running this project.
    
    params:
        file_path: requirements file path
    returns:
        list of required packages
    """
    req = []
    with open(file_path) as file:
        req = file.readlines()
        req = [r.replace("\n", "") for r in req]
        if HYPHEN_E_DOT in req:
            req.remove(HYPHEN_E_DOT)
    return req

setup(
    name='mlproject',
    version='0.0.1',
    author='Jayantha',
    author_email='nanduri.j@northeastern.edu',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)